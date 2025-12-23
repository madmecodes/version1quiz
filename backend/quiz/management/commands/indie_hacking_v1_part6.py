from django.core.management.base import BaseCommand
from quiz.models import Level, Question


class Command(BaseCommand):
    help = 'Populate Level 23: Launch & Marketing Mastery for indie hackers'

    def handle(self, *args, **options):
        # Create Level 23
        level, created = Level.objects.get_or_create(
            level_number=23,
            defaults={
                'title': 'Launch & Marketing Mastery',
                'description': 'Master product launches and marketing strategies. Learn Product Hunt optimization, platform selection, analytics tracking, and post-launch growth tactics for indie products.',
                'category': 'Indie Hacking',
                'difficulty': 'intermediate',
                'xp_reward': 100,
                'passing_percentage': 70,
            }
        )

        if not created:
            self.stdout.write(f'Level 23 already exists, skipping creation')
            return

        questions = [
            # Pre-Launch Preparation (4 questions)
            {
                'question': 'What is the primary purpose of building an email list BEFORE launching your product?',
                'options': [
                    'To spam potential customers with marketing emails',
                    'To have guaranteed initial traffic and early feedback on day 1 of launch',
                    'To build a social media following',
                    'To collect payment information early',
                ],
                'correct_answer': 1,
                'explanation': 'An email list of 100-500 people interested in your solution provides guaranteed day-1 traffic. This is crucial for Product Hunt visibility and momentum. Building the list 4-6 weeks before launch allows you to validate interest and get early feedback.',
            },
            {
                'question': 'When should you start preparing for your product launch?',
                'options': [
                    'The night before launch',
                    '1 week before launch',
                    '4-6 weeks before launch for optimal results',
                    'Right when you have the first commit in Git',
                ],
                'correct_answer': 2,
                'explanation': 'Product launches are most successful with 4-6 weeks of preparation. This includes: landing page creation, email list building, community feedback, beta testing, messaging refinement, and coordination planning.',
            },
            {
                'question': 'Which of these is NOT an effective pre-launch community building strategy?',
                'options': [
                    'Engaging in relevant Indie Hackers threads about similar problems',
                    'Building a Discord community to get early feedback from users',
                    'Spamming Reddit subreddits with "coming soon" messages',
                    'Tweeting about your building journey to attract early adopters',
                ],
                'correct_answer': 2,
                'explanation': 'Spamming Reddit is forbidden and will get you banned. Reddit communities value genuine participation and value-first approaches. Effective strategies are building communities (Discord), genuine engagement (Indie Hackers), and building in public (Twitter).',
            },
            {
                'question': 'What is "building in public"?',
                'options': [
                    'Making your GitHub repo public before launch',
                    'Sharing your progress, challenges, and learnings on Twitter/social media during development',
                    'Publishing blog posts about your product before launch',
                    'Broadcasting your product on video streaming platforms',
                ],
                'correct_answer': 1,
                'explanation': '"Building in public" means regularly sharing your progress, challenges, wins, and lessons learned on social media (especially Twitter). This builds an audience, gets feedback, and creates momentum before launch. Examples: tweet your architecture decisions, user feedback, milestone updates.',
            },

            # Product Hunt Launch (5 questions)
            {
                'question': 'What is the optimal time to launch on Product Hunt?',
                'options': [
                    'Monday at 9am PST for maximum week momentum',
                    'Tuesday-Thursday at 12:01am PST (just after midnight)',
                    'Friday for weekend visibility',
                    'Sunday for weekend users',
                ],
                'correct_answer': 1,
                'explanation': 'Product Hunt resets the leaderboard daily at 12:01am PST. Launching then gives you the entire 24-hour cycle to accumulate upvotes. Tuesday-Thursday is ideal (more active users). Friday-Sunday launches get less visibility. The first 4-6 hours are critical for momentum.',
            },
            {
                'question': 'What makes a great Product Hunt tagline?',
                'options': [
                    'As long as possible to describe all features',
                    'Under 60 characters, benefit-focused, clear value proposition',
                    'Funny or clever wordplay to stand out',
                    'Technical jargon to attract engineers',
                ],
                'correct_answer': 1,
                'explanation': 'Effective taglines are concise (under 60 chars), focus on the benefit (not features), and are immediately clear. Examples: "Notion for designers" or "Loom for code". Users should understand your product in 3 seconds. Bad: "A comprehensive solution for managing data workflows efficiently" (too long, vague).',
            },
            {
                'question': 'Should you launch on Product Hunt yourself or hire a "Hunter"?',
                'options': [
                    'Always hire a Hunter for 5-15% equity',
                    'Self-launch if you can, hire a Hunter if you lack connections',
                    'Always self-launch to maintain control',
                    'Never hire Hunters, they dilute your vision',
                ],
                'correct_answer': 1,
                'explanation': 'Self-launching is preferred if you have existing Product Hunt audience (followers). Hunters (experienced PH users) help if you don\'t have an audience—they provide followers and guidance. Equity is negotiable (often 1-5% commission, not equity). Choose based on your PH credibility and audience size.',
            },
            {
                'question': 'What is the "first comment" strategy on Product Hunt?',
                'options': [
                    'Wait for users to comment first',
                    'Post a lengthy feature breakdown',
                    'Post a thoughtful maker comment within the first hour answering "What? Why? How?"',
                    'Only respond to negative comments',
                ],
                'correct_answer': 2,
                'explanation': 'The maker should post a thoughtful first comment answering: What is this? Why did you build it? How does it solve a real problem? This sets the tone, shows you\'re engaged, and helps potential users understand your value. It should be honest, personal, and humble—not promotional.',
            },
            {
                'question': 'How important are screenshots and videos for Product Hunt success?',
                'options': [
                    'Not important, description is what matters',
                    'Moderately important, nice to have',
                    'Critical—60-70% of users decide based on visuals before reading',
                    'Only important for design tools',
                ],
                'correct_answer': 2,
                'explanation': 'Visuals are crucial. Most users decide in 3 seconds based on thumbnail image. Screenshots should show the product solving the problem clearly. Videos (20-30 sec demo) increase engagement 3-5x. A polished demo is the difference between 50 and 500 upvotes.',
            },

            # Other Launch Platforms (4 questions)
            {
                'question': 'What is the key difference between launching on Hacker News vs Product Hunt?',
                'options': [
                    'Hacker News has more technical users and is invitation-only',
                    'HN values authenticity and technical depth; PH values marketing and visuals',
                    'HN only accepts open-source projects',
                    'PH has no moderation, HN has strict rules',
                ],
                'correct_answer': 1,
                'explanation': 'Hacker News (HN) audience is highly technical and values substance over marketing. Avoid overly polished marketing speak; be authentic. Posts must follow the "Show HN" guideline. Product Hunt is more marketing-friendly. HN can drive 5000+ technical users; less useful for consumer products.',
            },
            {
                'question': 'Why is Reddit considered risky for self-promotion?',
                'options': [
                    'Reddit has no active users',
                    'Most subreddits ban self-promotion; violating this results in permanent bans',
                    'Reddit is only for entertainment, not products',
                    'Reddit moderation is too strict on all posts',
                ],
                'correct_answer': 1,
                'explanation': 'Reddit communities have strict rules against self-promotion. Violating these gets you banned and marked as a spammer. Smart strategy: provide value first (answer questions in your niche), build credibility, then mention your product naturally. Follow subreddit rules carefully.',
            },
            {
                'question': 'What makes a successful Twitter launch thread?',
                'options': [
                    'A single tweet about your product',
                    'A 50-tweet thread with every detail',
                    'A 5-10 tweet narrative thread: problem → journey → solution, encouraging engagement',
                    'Just a link to your product with no context',
                ],
                'correct_answer': 2,
                'explanation': 'Effective Twitter threads tell a story. Start with the problem (pain point), share your journey (how you built it), reveal the solution, and call-to-action. 5-10 tweets is ideal. Encourage retweets/replies. Use this before PH launch to warm up your audience and build momentum.',
            },
            {
                'question': 'What is Indie Hackers, and why is it valuable for indie product launches?',
                'options': [
                    'A competitor to Product Hunt',
                    'A community of indie developers and makers; highly engaged audience interested in building',
                    'Only for non-technical people',
                    'A job board for freelancers',
                ],
                'correct_answer': 1,
                'explanation': 'Indie Hackers is a community of founders, makers, and bootstrapped businesses. Sharing your launch there generates engaged traffic from people who understand indie hacker challenges. Many IH members also use Product Hunt, creating a powerful one-two punch.',
            },

            # Analytics & Tracking (3 questions)
            {
                'question': 'What should you track immediately after launch?',
                'options': [
                    'Only total revenue',
                    'Traffic source, conversion funnel, signup rate, where visitors come from',
                    'Just wait and check revenue after 30 days',
                    'Only social media mentions',
                ],
                'correct_answer': 1,
                'explanation': 'Post-launch, track: Where is traffic coming from? (Product Hunt, HN, Twitter) What% convert to signups? What% of signups become customers? Which traffic sources are highest quality? This data guides where to focus and reveals what messaging resonates.',
            },
            {
                'question': 'What are UTM parameters used for?',
                'options': [
                    'Tracking server uptime',
                    'Measuring user engagement within your app',
                    'Tagging links to track which marketing channel/campaign drove traffic',
                    'Setting user timezone preferences',
                ],
                'correct_answer': 2,
                'explanation': 'UTM parameters are tags in URLs (e.g., ?utm_source=twitter&utm_campaign=launch) that help you track which channel/campaign drove traffic. Example: Share different links on Twitter vs Reddit to see which performs better. Helps answer "what marketing actually works?"',
            },
            {
                'question': 'What is a conversion funnel, and why does it matter?',
                'options': [
                    'A marketing email template',
                    'The path users take: Landing page → Signup → Trial → Customer. Track drop-off rates at each step.',
                    'A sales script for calls',
                    'An analytics dashboard tool',
                ],
                'correct_answer': 1,
                'explanation': 'A conversion funnel shows how many users complete each step. Example: 1000 visitors → 500 signups (50%) → 50 trials (10%) → 10 customers (2%). If signup rate is low, landing page copy is the problem. If trial-to-customer is low, your product needs work. Fix the biggest leak.',
            },

            # Post-Launch Growth (4 questions)
            {
                'question': 'What is a realistic timeline for SEO to drive traffic to your indie product?',
                'options': [
                    '2-4 weeks',
                    '2-3 months',
                    '6-12 months minimum, often 12+ months',
                    'SEO doesn\'t work for indie products',
                ],
                'correct_answer': 2,
                'explanation': 'SEO is a long-term strategy. Expect 6-12+ months for top rankings. Google trusts established sites. For quick growth post-launch, focus on: content marketing (blog posts), email list, partnerships, community engagement. Use SEO as future passive income, not short-term growth.',
            },
            {
                'question': 'What is content marketing for indie hackers?',
                'options': [
                    'Paid ads on social media',
                    'Creating valuable blog posts, videos, or guides that solve customer problems and attract organic traffic',
                    'Writing product announcements',
                    'Only for large companies with marketing budgets',
                ],
                'correct_answer': 1,
                'explanation': 'Content marketing means creating useful content (tutorials, guides, case studies) around the problems your product solves. A guide "How to Optimize SQL Queries" attracts people to your database product. Long-term, content drives organic traffic and positions you as an expert.',
            },
            {
                'question': 'What is a referral program and why do indie hackers use them?',
                'options': [
                    'Paying customers to refer friends',
                    'Offering rewards when customers refer others; low-cost, high-impact growth',
                    'A discount for bulk purchases',
                    'Only for SaaS products, not applicable elsewhere',
                ],
                'correct_answer': 1,
                'explanation': 'Referral programs (e.g., "refer a friend, both get $10 credit") incentivize word-of-mouth. Cost: only pay when referral converts. Benefit: highest-quality customers (warm introductions). Example: Dropbox referral program gave both users extra storage, driving explosive growth.',
            },
            {
                'question': 'After launch, how should you prioritize your time between building features, marketing, and customer support?',
                'options': [
                    '90% features, 10% marketing',
                    '50% features, 40% marketing, 10% support',
                    '70% support/features, 20% marketing, 10% learning. Focus on retention first.',
                    '100% marketing until revenue reaches $1k MRR',
                ],
                'correct_answer': 2,
                'explanation': 'Post-launch priority: Support current customers (retention > acquisition), fix bugs in core product, then market. If you spend 100% on marketing but product is buggy, you\'ll lose customers. Happy customers refer 3-5 new customers. Quality > quantity of growth.',
            },
        ]

        # Create questions
        for q in questions:
            Question.objects.get_or_create(
                level=level,
                question=q['question'],
                defaults={
                    'options': q['options'],
                    'correct_answer': q['correct_answer'],
                    'explanation': q['explanation'],
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Successfully populated Level 23: Launch & Marketing Mastery with {len(questions)} questions!\n'
            )
        )
