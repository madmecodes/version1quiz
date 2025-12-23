from django.core.management.base import BaseCommand
from quiz.models import UserProgress
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


class Command(BaseCommand):
    help = 'Diagnose and fix duplicate UserProgress records'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fix',
            action='store_true',
            help='Automatically fix duplicates by keeping the oldest record',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Diagnosing Duplicate UserProgress Records ===\n'))

        # Find all users with more than one UserProgress record
        # Note: Due to OneToOneField constraint, this shouldn't normally happen,
        # but we'll check anyway for orphaned records or constraint violations

        all_progress = UserProgress.objects.all()
        self.stdout.write(f"Total UserProgress records: {all_progress.count()}")

        # Count unique users
        unique_users = User.objects.filter(progress__isnull=False).distinct().count()
        self.stdout.write(f"Unique users with progress: {unique_users}")

        if all_progress.count() > unique_users:
            self.stdout.write(
                self.style.ERROR(
                    f"\n⚠️  DUPLICATE RECORDS DETECTED!"
                )
            )
            self.stdout.write(f"Expected: {unique_users} records, Got: {all_progress.count()}\n")

            # Show which users have duplicates
            users_with_progress = User.objects.filter(progress__isnull=False)
            for user in users_with_progress:
                progress_count = UserProgress.objects.filter(user=user).count()
                if progress_count > 1:
                    self.stdout.write(self.style.WARNING(f"  {user.email}: {progress_count} records"))
                    # List their details
                    for i, progress in enumerate(UserProgress.objects.filter(user=user).order_by('id'), 1):
                        self.stdout.write(
                            f"    [{i}] ID: {progress.id}, XP: {progress.total_xp}, "
                            f"Level: {progress.current_level.level_number if progress.current_level else 'N/A'}, "
                            f"Created: {progress.created_at}"
                        )

            if options['fix']:
                self.stdout.write(self.style.SUCCESS('\n🔧 Fixing duplicates...\n'))
                fixed_count = 0

                for user in users_with_progress:
                    progress_records = UserProgress.objects.filter(user=user).order_by('id')
                    if progress_records.count() > 1:
                        # Keep the oldest (first) record, delete the rest
                        keep = progress_records.first()
                        to_delete = progress_records[1:]

                        # Merge XP and completed_levels if needed
                        for duplicate in to_delete:
                            # Add any completed levels from duplicate to keeper
                            for level in duplicate.completed_levels.all():
                                keep.completed_levels.add(level)

                            # Update XP if duplicate has more
                            if duplicate.total_xp > keep.total_xp:
                                keep.total_xp = duplicate.total_xp

                            # Update current_level if needed
                            if duplicate.current_level and (not keep.current_level or
                                    duplicate.current_level.level_number > keep.current_level.level_number):
                                keep.current_level = duplicate.current_level

                        keep.save()

                        # Delete duplicates
                        delete_count = to_delete.count()
                        to_delete.delete()

                        self.stdout.write(
                            self.style.SUCCESS(
                                f"✓ Fixed {user.email}: kept record ID {keep.id}, deleted {delete_count} duplicate(s)"
                            )
                        )
                        fixed_count += to_delete.count()

                self.stdout.write(
                    self.style.SUCCESS(f'\n✅ Successfully fixed {fixed_count} duplicate record(s)!')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        '\n💡 Run with --fix flag to automatically fix these duplicates:\n'
                        '   python manage.py diagnose_duplicates --fix\n'
                    )
                )
        else:
            self.stdout.write(self.style.SUCCESS('✅ No duplicate records found!\n'))
