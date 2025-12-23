"""
Part 5 of indie_hacking_v1.py - Level 22
DSA Fundamentals: Essential Data Structures & Algorithms
"""

from django.core.management.base import BaseCommand
from quiz.models import Level, Question


class Command(BaseCommand):
    help = 'Seed database with indie hacking curriculum - Part 5 (Level 22 - DSA)'

    def handle(self, *args, **options):
        # LEVEL 22: Data Structures & Algorithms Essentials
        level_22 = Level.objects.create(
            level_number=22,
            title="Data Structures & Algorithms Essentials",
            description="Understand why DSA matters, essential data structures, and when to use each for building scalable products.",
            category="Professional",
            difficulty="Beginner",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_22 = [
            {
                'question': 'What are data structures and why do they matter for indie hackers?',
                'options': [
                    'Useless academic theory',
                    'Organized ways to store data: choosing right structure = faster apps + less memory + better scaling',
                    'Only for competitive programming',
                    'All data structures identical'
                ],
                'correct_answer': 1,
                'explanation': 'Data structure choice directly impacts performance. Search list of 1M items: wrong structure = 10 seconds, right structure = instant. Matters for user experience and scaling.'
            },
            {
                'question': 'What is Big-O notation in plain terms?',
                'options': [
                    'A type of database',
                    'Measure of efficiency: O(n) checks each item, O(1) instant, O(n²) nested loops (slow)',
                    'Only theoretical',
                    'Doesn\'t matter for code'
                ],
                'correct_answer': 1,
                'explanation': 'Big-O = "how does speed change as data grows?" O(1) = always same speed. O(n) = speed grows with data. O(n²) = quadratic slowdown. Understand impact of growth.'
            },
            {
                'question': 'Array data structure: when is it best?',
                'options': [
                    'Never use arrays',
                    'Fast access by index, store ordered lists (user list, products, posts)',
                    'Always use arrays',
                    'For databases only'
                ],
                'correct_answer': 1,
                'explanation': 'Arrays = index-based access O(1). "Give me user #5" = instant. Good for: storing collections, iterating. Bad: inserting in middle (slow), no fast lookup by property.'
            },
            {
                'question': 'You need to find user by email instantly. Which data structure?',
                'options': [
                    'Array (loop all users)',
                    'Hash table/dictionary: email → user. Instant lookup O(1)',
                    'Linked list',
                    'Slow search is fine'
                ],
                'correct_answer': 1,
                'explanation': 'Hash table (object/dict) = perfect for lookups. {user@email: {id, name, ...}}. Users > emails = instant find by email. Trade: uses more memory for speed.'
            },
            {
                'question': 'Website undo feature: which data structure?',
                'options': [
                    'Array (too slow)',
                    'Stack (LIFO: Last action undone first). Push action, pop to undo',
                    'Queue',
                    'No structure needed'
                ],
                'correct_answer': 1,
                'explanation': 'Undo = stack. Actions: [type, delete, move]. Hit undo → pop (move). Hit again → pop (delete). Perfect LIFO fit. Browser back button works same way.'
            },
            {
                'question': 'Background job queue (upload image, send email, process data): which structure?',
                'options': [
                    'Stack (wrong order)',
                    'Queue (FIFO: First job done first). Fair, prevents starvation',
                    'Random',
                    'No structure needed'
                ],
                'correct_answer': 1,
                'explanation': 'Queue = fair ordering. First job enqueued = first job done. First one waiting = first one processed. "First come, first served." Redis uses this.'
            },
            {
                'question': 'File system (files in folders in subfolders): which structure?',
                'options': [
                    'Array (flat)',
                    'Tree (hierarchical: root → directories → files). Each node has parent/children',
                    'Queue',
                    'Linked list'
                ],
                'correct_answer': 1,
                'explanation': 'Trees = hierarchical. OS: /home/user/projects/app. Each directory is node with children. DOM in browser = tree (html has body which has divs which have paragraphs).'
            },
            {
                'question': 'Social network (users connected as friends): which structure?',
                'options': [
                    'Array (can\'t represent connections)',
                    'Graph (nodes = users, edges = friendships). Can find mutual friends, shortest path',
                    'Tree (wrong)',
                    'Hash table'
                ],
                'correct_answer': 1,
                'explanation': 'Graphs = connections between entities. Social: find friends. Maps: shortest route. Recommendations: item similarities. Most flexible, most complex structure.'
            },
            {
                'question': 'Performance issue: finding product by SKU in 1M items takes too long. Solution?',
                'options': [
                    'Buy faster server',
                    'Use hash table: {SKU: product}. Instant lookup vs linear search',
                    'Delete products',
                    'Accept slow performance'
                ],
                'correct_answer': 1,
                'explanation': 'Linear search O(n) on 1M items = 500K average comparisons. Hash table O(1) = one lookup. 500K times slower without proper structure. Critical for scale.'
            },
            {
                'question': 'Sorting product list by price then rating: what should you understand?',
                'options': [
                    'Sorting is always same speed',
                    'Sorting algorithms vary O(n log n) efficient vs O(n²) slow. Use language\'s built-in (optimized). Manual sorting rarely needed',
                    'Manual sorting required',
                    'No algorithm chosen'
                ],
                'correct_answer': 1,
                'explanation': 'Python .sort() uses Timsort (highly optimized). Don\'t write own sorting. Understand: sorting has cost O(n log n), indexes can avoid sorting by ordering access.'
            },
            {
                'question': 'SQL database finding users by name: how to speed up?',
                'options': [
                    'No way to speed up',
                    'Index on name column: database uses structure (B-tree) for O(log n) search instead of full scan O(n)',
                    'Delete indexes',
                    'Database doesn\'t need optimization'
                ],
                'correct_answer': 1,
                'explanation': 'Database indexes = B-trees (balanced trees). Searching 1M rows: no index = full scan slow, indexed = binary search O(log n) = ~20 comparisons. Query instant.'
            },
            {
                'question': 'Caching API responses: which data structure fits?',
                'options': [
                    'Array (slow lookup)',
                    'Hash table: {request_url: response}. Instant cache hit',
                    'Linked list',
                    'No structure'
                ],
                'correct_answer': 1,
                'explanation': 'Cache = hash map. "Have I computed this before?" Instant check. Redis (in-memory cache) is basically optimized hash table. Speeds up apps dramatically.'
            },
            {
                'question': 'You design database schema. When to use relationships vs denormalizing?',
                'options': [
                    'Always normalize',
                    'Normalize for consistency, denormalize only if query performance requires it (measured, not guessed)',
                    'Never normalize',
                    'Relationships don\'t exist'
                ],
                'correct_answer': 1,
                'explanation': 'Normalized: user→posts (clean, one place to update). Denormalized: user object has post_count field (fast read, hard to update). Choose based on bottleneck.'
            },
            {
                'question': 'Comment thread (nested comments under comments): which structure?',
                'options': [
                    'Array (flat)',
                    'Tree (each comment can have children, recursively nested)',
                    'Queue',
                    'Graph'
                ],
                'correct_answer': 1,
                'explanation': 'Comment tree: root comment (node) → replies (children). Each reply can have replies (recursive). Display: recursively render children. Natural fit for hierarchy.'
            },
            {
                'question': 'Autocomplete search (matching user email): how to implement efficiently?',
                'options': [
                    'Linear search on every keystroke',
                    'Prefix tree (Trie) or sorted index: "joh" matches "john@..." instantly, not all emails',
                    'No optimization possible',
                    'Accept lag'
                ],
                'correct_answer': 1,
                'explanation': 'Trie = tree of prefixes. Searching for emails starting with "j" = follow j node → children. Instant without scanning all emails. Used everywhere (autocomplete).'
            },
            {
                'question': 'Why understand DSA if libraries do it for all us?',
                'options': [
                    'No reason, don\'t study DSA',
                    'Know when to use what: choose hash table vs array, recognize O(n²) bottlenecks, design efficient schema',
                    'Libraries handle everything',
                    'DSA is useless'
                ],
                'correct_answer': 1,
                'explanation': 'Libraries implement structures but you choose which to use. Know: arrays vs dicts, indexed vs unindexed, cache vs no cache. Good choices = fast app without rewriting libraries.'
            }
        ]

        for q in questions_level_22:
            Question.objects.create(
                level=level_22,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Part 5 (Level 22 - DSA)'))
