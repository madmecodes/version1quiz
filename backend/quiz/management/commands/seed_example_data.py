from django.core.management.base import BaseCommand
from quiz.models import Level, Question


class Command(BaseCommand):
    help = 'Populate example data with 5 levels for demonstration'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\nPopulating example data (5 levels)...\n'))

        levels_data = [
            {
                'level_number': 1,
                'title': 'Linux Basics',
                'description': 'Learn essential Linux commands and terminal navigation',
                'category': 'Technical',
                'difficulty': 'beginner',
                'xp_reward': 50,
                'passing_percentage': 70,
                'questions': [
                    {
                        'question': 'What command lists files in the current directory?',
                        'options': ['cd', 'ls', 'mkdir', 'pwd'],
                        'correct_answer': 1,
                        'explanation': 'The "ls" command lists files and directories in the current directory.'
                    },
                    {
                        'question': 'How do you change to the home directory?',
                        'options': ['cd home', 'cd ~', 'home', 'cd .'],
                        'correct_answer': 1,
                        'explanation': 'The tilde (~) represents your home directory. "cd ~" changes to it.'
                    },
                    {
                        'question': 'What does "pwd" command do?',
                        'options': ['Change password', 'Print working directory', 'Print web directory', 'Pause working directory'],
                        'correct_answer': 1,
                        'explanation': '"pwd" stands for Print Working Directory. It shows your current location in the file system.'
                    },
                    {
                        'question': 'Which command creates a new directory?',
                        'options': ['touch', 'mkdir', 'mkfile', 'newdir'],
                        'correct_answer': 1,
                        'explanation': '"mkdir" stands for make directory. It creates a new folder.'
                    },
                    {
                        'question': 'How do you view the contents of a file?',
                        'options': ['see file.txt', 'cat file.txt', 'show file.txt', 'read file.txt'],
                        'correct_answer': 1,
                        'explanation': 'The "cat" command displays the contents of a file in the terminal.'
                    },
                ]
            },
            {
                'level_number': 2,
                'title': 'Git & GitHub Fundamentals',
                'description': 'Master version control with Git and GitHub',
                'category': 'Technical',
                'difficulty': 'beginner',
                'xp_reward': 50,
                'passing_percentage': 70,
                'questions': [
                    {
                        'question': 'What does "git commit" do?',
                        'options': ['Uploads to GitHub', 'Saves changes to local repository', 'Deletes files', 'Merges branches'],
                        'correct_answer': 1,
                        'explanation': 'A commit saves your changes to the local Git repository with a message describing the changes.'
                    },
                    {
                        'question': 'What command initializes a new Git repository?',
                        'options': ['git start', 'git init', 'git new', 'git create'],
                        'correct_answer': 1,
                        'explanation': '"git init" initializes a new local Git repository in the current directory.'
                    },
                    {
                        'question': 'What is a branch used for?',
                        'options': ['Storing backups', 'Working on features independently', 'Deleting code', 'Testing servers'],
                        'correct_answer': 1,
                        'explanation': 'Branches allow you to work on features independently from the main codebase.'
                    },
                    {
                        'question': 'What does "git push" do?',
                        'options': ['Merges code', 'Uploads commits to remote repository', 'Deletes branches', 'Creates backups'],
                        'correct_answer': 1,
                        'explanation': '"git push" uploads your local commits to a remote repository like GitHub.'
                    },
                    {
                        'question': 'What is a pull request used for?',
                        'options': ['Pulling files locally', 'Requesting to merge code into main branch', 'Downloading repositories', 'Deleting branches'],
                        'correct_answer': 1,
                        'explanation': 'A pull request is a request to merge your branch code into the main branch, allowing code review.'
                    },
                ]
            },
            {
                'level_number': 3,
                'title': 'JavaScript Fundamentals',
                'description': 'Learn core JavaScript concepts and syntax',
                'category': 'Technical',
                'difficulty': 'intermediate',
                'xp_reward': 75,
                'passing_percentage': 70,
                'questions': [
                    {
                        'question': 'What is the correct way to declare a variable in modern JavaScript?',
                        'options': ['var x = 5;', 'let x = 5;', 'variable x = 5;', 'x = 5;'],
                        'correct_answer': 1,
                        'explanation': '"let" is the modern way to declare variables with block scope. "var" is outdated.'
                    },
                    {
                        'question': 'What does "const" mean?',
                        'options': ['Create optional variable', 'Constant (cannot be reassigned)', 'Create constructor', 'Copy variable'],
                        'correct_answer': 1,
                        'explanation': '"const" declares a constant variable that cannot be reassigned after initialization.'
                    },
                    {
                        'question': 'What is a function?',
                        'options': ['A variable', 'A reusable block of code', 'A loop', 'An object property'],
                        'correct_answer': 1,
                        'explanation': 'A function is a reusable block of code that performs a specific task.'
                    },
                    {
                        'question': 'What is an arrow function?',
                        'options': ['A pointing comment', 'Modern syntax for declaring functions using =>', 'A looping structure', 'A comparison operator'],
                        'correct_answer': 1,
                        'explanation': 'Arrow functions (=>) are a concise syntax for writing functions introduced in ES6.'
                    },
                    {
                        'question': 'What is the difference between == and ===?',
                        'options': ['No difference', '== checks value, === checks value and type', '=== is outdated', '== is faster'],
                        'correct_answer': 1,
                        'explanation': '=== is strict equality (checks both value and type), == is loose equality (only checks value).'
                    },
                ]
            },
            {
                'level_number': 4,
                'title': 'React Basics',
                'description': 'Introduction to React components and state management',
                'category': 'Technical',
                'difficulty': 'intermediate',
                'xp_reward': 75,
                'passing_percentage': 70,
                'questions': [
                    {
                        'question': 'What is a React component?',
                        'options': ['A JavaScript file', 'A reusable UI element', 'A styling tool', 'A database connection'],
                        'correct_answer': 1,
                        'explanation': 'A React component is a reusable piece of the UI, can be a function or class.'
                    },
                    {
                        'question': 'What is JSX?',
                        'options': ['A styling language', 'JavaScript XML syntax for writing UI', 'A database query', 'A server framework'],
                        'correct_answer': 1,
                        'explanation': 'JSX allows you to write HTML-like syntax in JavaScript for defining components.'
                    },
                    {
                        'question': 'What are props in React?',
                        'options': ['Component properties passed from parent to child', 'Programming proposals', 'Styling properties', 'State variables'],
                        'correct_answer': 0,
                        'explanation': 'Props are read-only data passed from parent components to child components.'
                    },
                    {
                        'question': 'What is the useState hook used for?',
                        'options': ['Making API calls', 'Managing component state (reactive data)', 'Styling components', 'Routing pages'],
                        'correct_answer': 1,
                        'explanation': 'useState allows function components to have state. It returns current state and a function to update it.'
                    },
                    {
                        'question': 'What is the difference between state and props?',
                        'options': ['No difference', 'Props are mutable, state is not', 'State is local and mutable, props are passed and immutable', 'State is for styling'],
                        'correct_answer': 2,
                        'explanation': 'State is local and can change, props are passed from parents and are read-only.'
                    },
                ]
            },
            {
                'level_number': 5,
                'title': 'Django Basics',
                'description': 'Learn Django framework fundamentals for backend development',
                'category': 'Technical',
                'difficulty': 'intermediate',
                'xp_reward': 75,
                'passing_percentage': 70,
                'questions': [
                    {
                        'question': 'What is Django?',
                        'options': ['A JavaScript framework', 'A Python web framework', 'A database', 'A CSS library'],
                        'correct_answer': 1,
                        'explanation': 'Django is a high-level Python web framework for building web applications.'
                    },
                    {
                        'question': 'What does the "models" layer do in Django?',
                        'options': ['Displays data to users', 'Defines database structure and business logic', 'Handles routing', 'Manages CSS'],
                        'correct_answer': 1,
                        'explanation': 'Models define the database schema and contain the business logic of your application.'
                    },
                    {
                        'question': 'What is a Django view?',
                        'options': ['A template file', 'A function/class that processes requests and returns responses', 'A form', 'A database migration'],
                        'correct_answer': 1,
                        'explanation': 'A view is a Python function or class that receives a request and returns a response.'
                    },
                    {
                        'question': 'What is a Django URL pattern used for?',
                        'options': ['Styling links', 'Mapping URLs to views', 'Creating email addresses', 'Database queries'],
                        'correct_answer': 1,
                        'explanation': 'URL patterns route incoming HTTP requests to the appropriate views.'
                    },
                    {
                        'question': 'What does "python manage.py migrate" do?',
                        'options': ['Starts the server', 'Applies database schema changes', 'Creates new projects', 'Deletes the database'],
                        'correct_answer': 1,
                        'explanation': 'Migrations apply pending database schema changes based on your models.'
                    },
                ]
            },
        ]

        for level_data in levels_data:
            questions = level_data.pop('questions')
            level, created = Level.objects.get_or_create(
                level_number=level_data['level_number'],
                defaults=level_data
            )

            if created:
                for q in questions:
                    Question.objects.create(
                        level=level,
                        question=q['question'],
                        options=q['options'],
                        correct_answer=q['correct_answer'],
                        explanation=q['explanation']
                    )
                self.stdout.write(
                    self.style.SUCCESS(f'Created Level {level.level_number}: {level.title} ({len(questions)} questions)')
                )
            else:
                self.stdout.write(f'Level {level.level_number} already exists')

        self.stdout.write(self.style.SUCCESS('\nExample data populated successfully!\n'))
