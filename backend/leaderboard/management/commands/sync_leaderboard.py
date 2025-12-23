from django.core.management.base import BaseCommand
from leaderboard.models import Leaderboard
from quiz.models import UserProgress, QuizSubmission
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Sync leaderboard from UserProgress and QuizSubmission data'

    def handle(self, *args, **options):
        self.stdout.write('Syncing leaderboard...')

        # Get all users with progress
        all_progress = UserProgress.objects.all()

        # Get current max rank to avoid conflicts
        max_rank = Leaderboard.objects.count()
        temp_rank = max_rank + 1

        for progress in all_progress:
            user = progress.user

            # Calculate stats
            passed_submissions = QuizSubmission.objects.filter(user=user, result='passed')
            total_xp = sum(s.xp_earned for s in passed_submissions)
            completed_count = progress.completed_levels.count()
            current_level_num = progress.current_level.level_number if progress.current_level else 1

            # Create or update leaderboard entry
            leaderboard_entry, created = Leaderboard.objects.get_or_create(
                user=user,
                defaults={
                    'rank': temp_rank,
                    'total_xp': total_xp,
                    'current_level': current_level_num,
                    'completed_levels': completed_count
                }
            )

            if not created:
                leaderboard_entry.total_xp = total_xp
                leaderboard_entry.current_level = current_level_num
                leaderboard_entry.completed_levels = completed_count
                leaderboard_entry.save()

            temp_rank += 1

            action = 'Created' if created else 'Updated'
            self.stdout.write(
                self.style.SUCCESS(
                    f'{action} leaderboard entry for {user.email}: {total_xp} XP, Level {current_level_num}, {completed_count} completed'
                )
            )
        
        # Recalculate ranks
        self.stdout.write('Recalculating ranks...')
        all_leaderboard = list(Leaderboard.objects.all().order_by('-total_xp', '-completed_levels', 'updated_at'))

        # First, set all ranks to temporary high values to avoid unique constraint conflicts
        for i, entry in enumerate(all_leaderboard):
            entry.rank = 10000 + i
            entry.save(update_fields=['rank'])

        # Then update to correct ranks (1, 2, 3...)
        for rank, entry in enumerate(all_leaderboard, 1):
            entry.rank = rank
            entry.save(update_fields=['rank'])
            self.stdout.write(f'  #{rank}: {entry.user.email} - {entry.total_xp} XP')

        self.stdout.write(self.style.SUCCESS('Leaderboard sync completed!'))
