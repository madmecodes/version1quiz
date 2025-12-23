from django.core.management.base import BaseCommand
from quiz.models import UserProgress
from django.db import connection

class Command(BaseCommand):
    help = 'Fix duplicate UserProgress records in the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Fixing Duplicate UserProgress Records ===\n'))

        # Get raw database records to see actual duplicates
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT user_id, COUNT(*) as count
                FROM quiz_userprogress
                GROUP BY user_id
                HAVING COUNT(*) > 1
            """)
            duplicates = cursor.fetchall()

        if not duplicates:
            self.stdout.write(self.style.SUCCESS('✅ No duplicate records found!\n'))
            return

        self.stdout.write(self.style.WARNING(f'Found {len(duplicates)} users with duplicate records:\n'))

        for user_id, count in duplicates:
            self.stdout.write(f'  User ID: {user_id}, Duplicate records: {count}')

        self.stdout.write(self.style.WARNING('\n⚠️  Removing duplicates...\n'))

        # For each user with duplicates, keep only the first one
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT user_id, COUNT(*) as count
                FROM quiz_userprogress
                GROUP BY user_id
                HAVING COUNT(*) > 1
            """)
            users_with_dupes = cursor.fetchall()

        total_deleted = 0
        for user_id, count in users_with_dupes:
            # Get all records for this user, ordered by id
            records = UserProgress.objects.filter(user_id=user_id).order_by('id')
            keep = records.first()
            to_delete = records[1:]

            deleted_count = to_delete.count()
            to_delete.delete()

            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ User ID {user_id}: Kept record ID {keep.id}, deleted {deleted_count} duplicate(s)'
                )
            )
            total_deleted += deleted_count

        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully deleted {total_deleted} duplicate record(s)!\n'))

        # Verify
        with connection.cursor() as cursor:
            cursor.execute('SELECT COUNT(*) FROM quiz_userprogress')
            remaining = cursor.fetchone()[0]

        self.stdout.write(f'Total UserProgress records remaining: {remaining}\n')
