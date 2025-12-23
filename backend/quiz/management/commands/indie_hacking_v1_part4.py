"""
Part 4 of indie_hacking_v1.py - Levels 20-21
Indie Hacking: Building & Growing Your Business
"""

from django.core.management.base import BaseCommand
from quiz.models import Level, Question


class Command(BaseCommand):
    help = 'Seed database with indie hacking curriculum - Part 4 (Levels 20-21)'

    def handle(self, *args, **options):
        # LEVEL 20: Building Your Indie Business (Idea → Launch)
        level_20 = Level.objects.create(
            level_number=20,
            title="Building Your Indie Business (Idea → Launch)",
            description="Master idea validation, MVP development, pricing strategies, and launching your indie product.",
            category="Indie Hacking",
            difficulty="Intermediate",
            xp_reward=250,
            passing_percentage=40
        )

        questions_level_20 = [
            {
                'question': 'What\'s the key difference between indie hacking and traditional startups?',
                'options': [
                    'Indie hackers need investors',
                    'Indie hacking: bootstrapped, profitability-focused, solo/small team. Traditional: VC-funded, growth-focused',
                    'Indie hacking is less serious',
                    'No real difference'
                ],
                'correct_answer': 1,
                'explanation': 'Indie: your money, your rules, profitable from day 1. VC startup: investors\' money, chase growth, burn cash for years. Both valid paths with different goals.'
            },
            {
                'question': 'You have an idea for a SaaS. First step before coding?',
                'options': [
                    'Start coding immediately',
                    'Validate problem: interview 10-20 potential customers, confirm they care',
                    'Build minimal MVP',
                    'Start marketing'
                ],
                'correct_answer': 1,
                'explanation': 'Most MVPs fail because they solve wrong problem. Talk to users first (5 coffee chats). "Would you pay for this?" reveals real interest. Validation prevents wasted months.'
            },
            {
                'question': 'Customer interview - what question reveals if problem is real?',
                'options': [
                    '"Do you like my idea?"',
                    '"How much money would you pay?" - reveals willingness to pay, true problem depth',
                    '"Is this cool?"',
                    'No single question works'
                ],
                'correct_answer': 1,
                'explanation': 'People say "yes, cool idea" but don\'t pay. Money question = skin in game. "Would you pay $10/month?" reveals real vs polite interest.'
            },
            {
                'question': 'Pre-selling before building - how useful?',
                'options': [
                    'Impossible',
                    'Very useful: 5-10 paying customers = proof problem is real, capital to build, customer feedback',
                    'Unethical',
                    'Only for proven founders'
                ],
                'correct_answer': 1,
                'explanation': 'Pre-sell: "I\'m building X for $10/month, beta access next month." 5 paying pre-orders = validation + $50 fund. This is how many successful indie apps started.'
            },
            {
                'question': 'What makes an MVP actually "minimum"?',
                'options': [
                    'Bare minimum = broken product',
                    'Do core feature ONLY that solves main problem. Cut 80% of ideas. Ship in weeks not months',
                    'More features = better MVP',
                    'MVP quality doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'MVP for issue tracking: create/assign/close tasks. Skip: notifications, integrations, advanced reports. Ship core, iterate with users. Faster learning.'
            },
            {
                'question': 'No-code vs code for MVP - what\'s the trade-off?',
                'options': [
                    'Always use code',
                    'No-code: faster launch, limited scaling. Code: more control, slower to start. Choose based on idea complexity',
                    'No-code is worse',
                    'Both identical'
                ],
                'correct_answer': 1,
                'explanation': 'No-code (Bubble, Glide): validating business idea fast. Code: more complex, unlimited. No-code for idea validation, code if scaling beyond platform limits.'
            },
            {
                'question': 'Feature prioritization for MVP - how to decide what to build?',
                'options': [
                    'Build everything equally',
                    'Impact x Effort matrix: high impact + low effort first. Skip nice-to-haves',
                    'User vote on all features',
                    'Random selection'
                ],
                'correct_answer': 1,
                'explanation': 'High impact (solves main problem) + low effort (quick build) = first. Low effort + low impact = nice-to-have (build later). Ruthlessly cut scope.'
            },
            {
                'question': 'Timeline for MVP: realistic or "move fast"?',
                'options': [
                    'One year is normal',
                    'Three months for MVP. Too long = old technology, changed market. Fast iteration > perfection',
                    'One month always',
                    'Time doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': '3-month MVP sweet spot: fast enough to validate quickly, slow enough to build something real. 6mo+ = too long, market changes. 2 weeks = probably too minimal.'
            },
            {
                'question': 'Getting first 10 users for MVP - best approach?',
                'options': [
                    'Paid ads immediately',
                    'Organic: personal network, communities, cold email. Free > paid for MVP',
                    'Wait for organic growth',
                    'Doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'First 10: personal network (friends, Twitter followers). Next 100: communities (Reddit, Discord, Indie Hackers). Cold email to problem-suffers. Paid later after conversion proof.'
            },
            {
                'question': 'Pricing: when should you charge?',
                'options': [
                    'Never charge, freemium only',
                    'Charge from MVP launch. Money = commitment, feedback quality improves',
                    'Only after 1000 users',
                    'Charge in year 2'
                ],
                'correct_answer': 1,
                'explanation': 'Charge day 1 (even $5/month). Users who pay give feedback, use more, care more. Free users = vanity metrics. Price validates product-market fit.'
            },
            {
                'question': 'SaaS pricing: $9 vs $29 vs $99 - how to choose?',
                'options': [
                    'All equally valid',
                    'Test with $29 first (middle). If many upgrade to higher, raise. If all downgrade, lower',
                    'Start at $99',
                    'Copy competitor pricing'
                ],
                'correct_answer': 1,
                'explanation': '$29 is good starting point for B2B SaaS. Watch: upgrade rate tells if overpriced/underpriced. Underpriced = many upgrades. Overpriced = many cancels. Adjust quarterly.'
            },
            {
                'question': 'Charging from day 1 vs freemium then paywall?',
                'options': [
                    'Both equally good',
                    'Paid MVP: filter non-serious users, faster revenue. Freemium: larger user base but hard to convert. Start paid for MVP',
                    'Freemium always better',
                    'Doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Paid MVP = pure focus (best 100 users > 10K inactive). Money validates. Freemium = scale problem (convert 1% of 10K = harder than selling 100 directly).'
            },
            {
                'question': 'You hit product-market fit. What does that look like?',
                'options': [
                    'Any users at all',
                    'Users return without marketing, pay happily, refer friends. Growth feels inevitable',
                    '50 users',
                    'Designer approves it'
                ],
                'correct_answer': 1,
                'explanation': 'PMF: 40%+ monthly active retention (users come back). Positive NPS (net promoter score 50+). Growth from word-of-mouth. You\'ll feel it.'
            },
            {
                'question': 'MVPs fail despite traction. When should you pivot?',
                'options': [
                    'After 1 user gives negative feedback',
                    'Pivot after clear signal: declining retention, churn, bad metrics despite marketing effort',
                    'Never pivot',
                    'Always pivot'
                ],
                'correct_answer': 1,
                'explanation': 'Pivot signals: retention drops, churn high, users say "wrong problem solved". Don\'t pivot for one complaint. Need 10+ users confirming misalignment before pivot.'
            },
            {
                'question': 'Post-launch: focus on features or marketing?',
                'options': [
                    'Only marketing',
                    'Both: improve core product (retention), then marketing. Better product = easier marketing',
                    'Only features',
                    'Neither matters'
                ],
                'correct_answer': 1,
                'explanation': 'Product first: 40% retention before heavy marketing (waste of money). Once retention good, marketing works. Good product = word-of-mouth > paid ads.'
            },
            {
                'question': 'Staying motivated during slow growth - how?',
                'options': [
                    'Quit if growth slow',
                    'Remember: 1% daily growth compounds to 37x/year. Track small metrics (retention, NPS). Build in public for accountability',
                    'Wait for overnight success',
                    'Motivation doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Slow growth is normal. Track: daily active users, retention, churn. Celebrate small wins. Build in public (share progress weekly). Community = motivation.'
            },
            {
                'question': 'Should you quit job to pursue indie project full-time?',
                'options': [
                    'Immediately quit',
                    'Keep job until: MVP customers paying $X/mo (living expense covered). Quit with runway',
                    'Never pursue while employed',
                    'Doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Stay employed while validating. 3-6mo side project. If revenue covers 3mo living expenses + has growth trend, quit. De-risk: don\'t jump without proof.'
            }
        ]

        for q in questions_level_20:
            Question.objects.create(
                level=level_20,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 21: Growing & Sustaining Your Business (Launch → Success)
        level_21 = Level.objects.create(
            level_number=21,
            title="Growing & Sustaining Your Business (Launch → Success)",
            description="Master marketing, growth strategies, metrics, scaling, and long-term sustainability of indie products.",
            category="Indie Hacking",
            difficulty="Intermediate",
            xp_reward=250,
            passing_percentage=40
        )

        questions_level_21 = [
            {
                'question': 'What type of marketing works for indie products?',
                'options': [
                    'Paid ads only',
                    'Content marketing: blog, Twitter, video sharing knowledge. Cost: time. ROI: amazing if consistent',
                    'Direct mail',
                    'No marketing'
                ],
                'correct_answer': 1,
                'explanation': 'Indie hackers excel at content. Write 2-3 posts/week about your niche. Twitter threads explaining problems. YouTube tutorials. This attracts people with same problem.'
            },
            {
                'question': 'Building in public - what should you share?',
                'options': [
                    'Share everything',
                    'Share learning + progress: what you learned building, metrics (not secretive), user feedback',
                    'Share only success',
                    'Don\'t share anything'
                ],
                'correct_answer': 1,
                'explanation': 'Authentic building in public: "Launched yesterday, 10 signups. Learned X." Not: "Amazing! 10 millionaires use it!" Authenticity > hype. Community connects with realness.'
            },
            {
                'question': 'SEO for indie hackers - realistic or hype?',
                'options': [
                    'SEO doesn\'t work',
                    'Long-term SEO works: experience-based content ranks. "How I built X" → "How to build X". 6mo+ payoff',
                    'Instant SEO traffic',
                    'All hype'
                ],
                'correct_answer': 1,
                'explanation': 'SEO is valuable but slow. Indie hackers advantage: deep expertise (write authentic guides others can\'t). "Building in public" articles often rank. 6-12mo timeline.'
            },
            {
                'question': 'Email list: why more valuable than social followers?',
                'options': [
                    'Not more valuable',
                    'Email = 4x engagement, you control it. Social: algorithm changes, platform risk. Build email first',
                    'Email is old',
                    'Both equal'
                ],
                'correct_answer': 1,
                'explanation': '1000 email subscribers > 10K Twitter followers. Email: you own, direct, personal. Twitter: algorithm hides, platform risk (Elon changes rules). Build email early.'
            },
            {
                'question': 'When launching, where should you post?',
                'options': [
                    'All platforms simultaneously',
                    'Pick 1-2 platforms where audience is: Product Hunt + Indie Hackers OR Twitter + relevant communities',
                    'Random selection',
                    'Only one platform'
                ],
                'correct_answer': 1,
                'explanation': 'Focus beats spreading thin. For SaaS: Product Hunt launch day (upvotes = visibility). For content: Twitter daily (indie hacker audience). Pick where your customers hang out.'
            },
            {
                'question': 'Launch on Product Hunt - effective for indie MVPs?',
                'options': [
                    'Waste of time',
                    'Very effective: 500-2000 visitors in 24h. First day revenue/signups crucial',
                    'Only for VC-backed',
                    'Doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Product Hunt: upvote = visibility (algorithms favor highly upvoted). Good launch = #1 → 1000+ signups. Bad launch = lost forever. Optimize: tagline, screenshots, video.'
            },
            {
                'question': 'You have 100 users paying $30/mo ($3K MRR). How to grow?',
                'options': [
                    'Blast ads',
                    'Improve retention (losing users = wasted acquisition). Then scale: 100 users → 200. Retention first',
                    'Raise prices',
                    'Feature overload'
                ],
                'correct_answer': 1,
                'explanation': 'Retention = lifetime value. Keep 50% users = sustainable. Lose 100 users/mo = hamster wheel (acquire, churn). Fix retention (1% retention increase = 37x lifetime value).'
            },
            {
                'question': 'Key metrics for indie SaaS: which matter most?',
                'options': [
                    'Total users ever',
                    'MRR (revenue), churn rate, retention, CAC (acquisition cost), LTV (lifetime value)',
                    'Random metrics',
                    'Metrics are useless'
                ],
                'correct_answer': 1,
                'explanation': 'MRR: revenue health. Churn: retention health. CAC vs LTV: profitability. If CAC > LTV, can\'t profitably acquire. These 4 metrics tell full story.'
            },
            {
                'question': 'Churn rate 20% monthly. Is this normal?',
                'options': [
                    'Expected',
                    'High. Target: 2-5% monthly. 20% = half users gone every 5 months',
                    'Irrelevant',
                    'Good sign'
                ],
                'correct_answer': 1,
                'explanation': '5% churn = 19mo average customer lifetime. 20% churn = 5mo lifetime (need constant new users to stay flat). Lower churn = more valuable.'
            },
            {
                'question': 'Scaling from $1K MRR to $10K MRR - realistic timeline?',
                'options': [
                    'One month',
                    '1-2 years. Requires: product improvements, marketing, retention optimization, team/delegation',
                    'Impossible',
                    'Three months'
                ],
                'correct_answer': 1,
                'explanation': '10x growth realistic but slow. Each step (1K→2K→5K→10K) gets harder (market saturation, competition). Requires sustained focus. Many indie apps reach this, fewer go beyond.'
            },
            {
                'question': 'Should you focus on one product or multiple?',
                'options': [
                    'Multiple from day 1',
                    'One product to $5K MRR. Then: build adjacent product (leverage audience) or add features',
                    'Only one forever',
                    'Doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'One product = focus = better quality. At $5K+ MRR: consider portfolio approach (second product reuses infrastructure, audience, expertise). Diversifies revenue.'
            },
            {
                'question': 'Customer support: DIY or hire?',
                'options': [
                    'Hire immediately',
                    'DIY at first (learn customer problems). Hire when support takes 20hrs/week',
                    'Never respond',
                    'Outsource everything'
                ],
                'correct_answer': 1,
                'explanation': 'Support = learning. You hear real problems. Hire (VA or contractor) when it scales. Early DIY support improves product (fix real issues vs guessed ones).'
            },
            {
                'question': 'Burnout warning signs - how to prevent?',
                'options': [
                    'Push harder',
                    'Track: do you dread opening app? Skip exercise? Can\'t focus? Take breaks, take full days off, 50hr/week max',
                    'Burnout isn\'t real',
                    'Work harder'
                ],
                'correct_answer': 1,
                'explanation': 'Burnout is common for indie hackers. Prevent: day off weekly (actually off), exercise, hobby, social time. Broken indie hacker < rested sustainable one.'
            },
            {
                'question': 'When to hire your first employee?',
                'options': [
                    'Immediately at MVP',
                    'When you\'re overwhelmed + have $10K+ MRR to pay them. Start with contractor/VA',
                    'Never hire',
                    'Only at $100K MRR'
                ],
                'correct_answer': 1,
                'explanation': 'Hire signals: you work 60+ hours, can\'t do everything. Contractor first (test fit). Employee needs $10K+ MRR for salary + benefits. Scaling enabler, not early hire.'
            },
            {
                'question': 'Should you raise venture capital for indie app?',
                'options': [
                    'Always raise',
                    'Only if: need speed (market timing), can\'t bootstrap (heavy infrastructure), want to scale fast. Most indie apps bootstrap profitably',
                    'Never raise',
                    'Personal choice'
                ],
                'correct_answer': 1,
                'explanation': 'VC = growth pressure, dilution, board oversight. Indie benefit: keep 100%, no pressure. Raise only if: founders prefer it or specific opportunity requires it.'
            },
            {
                'question': 'What\'s a realistic "success" for indie hacker?',
                'options': [
                    'Unicorn status',
                    '$5K-50K MRR, control, freedom, sustainable income. Success = your definition (profit, impact, lifestyle)',
                    'Only massive scale',
                    'Impossible'
                ],
                'correct_answer': 1,
                'explanation': '$5K MRR = you quit job. $20K MRR = comfortable lifestyle. $100K MRR = very comfortable. Success isn\'t scale, it\'s what you want from it.'
            }
        ]

        for q in questions_level_21:
            Question.objects.create(
                level=level_21,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Part 4 (Levels 20-21)'))
