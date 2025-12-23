"""
Complete Indie Hacking Curriculum v1 - All 23 Levels Combined
This script imports and runs all 6 parts to seed the complete curriculum.
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Seed database with complete indie hacking curriculum v1 (23 levels)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('=' * 60))
        self.stdout.write(self.style.WARNING('SEEDING INDIE HACKING CURRICULUM V1 (23 LEVELS)'))
        self.stdout.write(self.style.WARNING('=' * 60))

        try:
            # Part 1: Levels 1-7
            self.stdout.write(self.style.SUCCESS('\n[1/6] Seeding Part 1 (Levels 1-7: Linux, Networking, Frontend Basics)...'))
            call_command('indie_hacking_v1_part1')

            # Part 2: Levels 8-14
            self.stdout.write(self.style.SUCCESS('\n[2/6] Seeding Part 2 (Levels 8-14: Frontend Advanced, Backend)...'))
            call_command('indie_hacking_v1_part2')

            # Part 3: Levels 15-19
            self.stdout.write(self.style.SUCCESS('\n[3/6] Seeding Part 3 (Levels 15-19: DevOps, Professional)...'))
            call_command('indie_hacking_v1_part3')

            # Part 4: Levels 20-21
            self.stdout.write(self.style.SUCCESS('\n[4/6] Seeding Part 4 (Levels 20-21: Indie Hacking)...'))
            call_command('indie_hacking_v1_part4')

            # Part 5: Level 22
            self.stdout.write(self.style.SUCCESS('\n[5/6] Seeding Part 5 (Level 22: DSA Fundamentals)...'))
            call_command('indie_hacking_v1_part5')

            # Part 6: Level 23
            self.stdout.write(self.style.SUCCESS('\n[6/6] Seeding Part 6 (Level 23: Launch & Marketing Mastery)...'))
            call_command('indie_hacking_v1_part6')

            self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
            self.stdout.write(self.style.SUCCESS('✓ COMPLETE INDIE HACKING CURRICULUM SEEDED SUCCESSFULLY'))
            self.stdout.write(self.style.SUCCESS('=' * 60))
            self.stdout.write(self.style.WARNING('\nCURRICULUM SUMMARY:'))
            self.stdout.write('  • Total Levels: 23')
            self.stdout.write('  • Total Questions: ~238')
            self.stdout.write('  • Technical Foundations: 19 levels')
            self.stdout.write('  • Indie Hacking: 3 levels')
            self.stdout.write('  • DSA Fundamentals: 1 level')
            self.stdout.write('\nTRACK BREAKDOWN:')
            self.stdout.write('  Track 1 - Technical (Levels 1-19):')
            self.stdout.write('    - Linux & Command Line: 2 levels')
            self.stdout.write('    - Networking & Internet: 3 levels')
            self.stdout.write('    - Frontend Development: 5 levels')
            self.stdout.write('    - Backend Development: 4 levels')
            self.stdout.write('    - DevOps & Deployment: 4 levels')
            self.stdout.write('    - Professional Skills: 1 level')
            self.stdout.write('\n  Track 2 - Indie Hacking (Levels 20-23):')
            self.stdout.write('    - Building Your Indie Business: 1 level (18 questions)')
            self.stdout.write('    - Growing & Sustaining: 1 level (18 questions)')
            self.stdout.write('    - Launch & Marketing Mastery: 1 level (20 questions)')
            self.stdout.write('\n  Track 3 - DSA Fundamentals (Level 22):')
            self.stdout.write('    - Data Structures & Algorithms: 1 level (16 questions)')
            self.stdout.write('\n' + '=' * 60 + '\n')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error seeding curriculum: {str(e)}'))
            raise
