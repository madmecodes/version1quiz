from django.core.management.base import BaseCommand
from quiz.models import UserProgress, Level


class Command(BaseCommand):
    help = 'Fix user progress by unlocking next levels based on completed levels'

    def handle(self, *args, **options):
        all_progress = UserProgress.objects.all()
        
        for progress in all_progress:
            completed_level_numbers = progress.completed_levels.values_list('level_number', flat=True)
            
            if completed_level_numbers:
                max_completed = max(completed_level_numbers)
                next_level = Level.objects.filter(level_number=max_completed + 1).first()
                
                if next_level and progress.current_level.level_number <= max_completed:
                    old_level = progress.current_level.level_number
                    progress.current_level = next_level
                    progress.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Updated {progress.user.email}: current_level {old_level} -> {next_level.level_number}'
                        )
                    )
                else:
                    self.stdout.write(f'{progress.user.email}: Already up to date')
            else:
                self.stdout.write(f'{progress.user.email}: No completed levels')
        
        self.stdout.write(self.style.SUCCESS('Progress fix completed!'))
