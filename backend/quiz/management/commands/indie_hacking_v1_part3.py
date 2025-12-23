"""
Part 3 of indie_hacking_v1.py - Levels 15-19
DevOps, Deployment, and Professional Skills
"""

from django.core.management.base import BaseCommand
from quiz.models import Level, Question


class Command(BaseCommand):
    help = 'Seed database with indie hacking curriculum - Part 3 (Levels 15-19)'

    def handle(self, *args, **options):
        # LEVEL 15: Docker for Development
        level_15 = Level.objects.create(
            level_number=15,
            title="Docker for Development",
            description="Learn containerization, Docker basics, docker-compose, and when to use containers.",
            category="DevOps",
            difficulty="Intermediate",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_15 = [
            {
                'question': 'What is containerization and why is it useful?',
                'options': [
                    'A way to organize code',
                    'Package your app with all dependencies in isolated environment - same everywhere (laptop, server, teammate)',
                    'A type of database',
                    'Only for big companies'
                ],
                'correct_answer': 1,
                'explanation': 'Container = your app + Python + libraries + config. Guarantees same behavior everywhere. "It works on my machine" problem solved. DevOps standard now.'
            },
            {
                'question': 'What\'s the difference between VM (Virtual Machine) and Container?',
                'options': [
                    'Same thing',
                    'VM: full OS (slow, heavy). Container: lightweight, shares host OS kernel (fast, small)',
                    'Containers are always slower',
                    'VMs are obsolete'
                ],
                'correct_answer': 1,
                'explanation': 'VM: 5GB, takes minutes to start. Container: 100MB, starts instantly. Containers more efficient for microservices. VMs still used for full isolation.'
            },
            {
                'question': 'What goes in a Dockerfile?',
                'options': [
                    'HTML code',
                    'Instructions to build image: base image, install dependencies, copy code, expose ports',
                    'Database queries',
                    'Configuration only'
                ],
                'correct_answer': 1,
                'explanation': 'Dockerfile is recipe: FROM python:3.10 → COPY code → RUN pip install → EXPOSE 8000 → CMD start app. Each line is a layer. Build = image, run image = container.'
            },
            {
                'question': 'Image vs Container - what\'s the difference?',
                'options': [
                    'Same thing',
                    'Image: blueprint (static), Container: running instance (dynamic)',
                    'Image is slower',
                    'Container is blueprint'
                ],
                'correct_answer': 1,
                'explanation': 'Image = file blueprint (read-only). Container = running image (has state). Like: class vs object. One image can run multiple containers.'
            },
            {
                'question': 'What is docker-compose and when use it?',
                'options': [
                    'A programming language',
                    'Tool to run multiple containers together (app + database + redis) with docker-compose.yml',
                    'Only for production',
                    'Obsolete tool'
                ],
                'correct_answer': 1,
                'explanation': 'docker-compose.yml defines all services. Run `docker-compose up` → starts app, database, cache all together. Perfect for local development (mirrors production).'
            },
            {
                'question': 'Your container won\'t start. How do you debug?',
                'options': [
                    'Give up',
                    'Run `docker logs container_name` to see error messages',
                    'Restart computer',
                    'Rebuild from scratch'
                ],
                'correct_answer': 1,
                'explanation': '`docker logs` shows container output. See Python errors, missing packages, port conflicts. Essential debugging skill. `docker ps` lists running containers.'
            },
            {
                'question': 'Should you commit Docker images to git?',
                'options': [
                    'Yes, every image',
                    'No, commit Dockerfile (small text). Build image from Dockerfile when needed',
                    'Images are tiny',
                    'It doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Commit Dockerfile (10KB), not image (100MB+). Dockerfile is version control. Anyone can build image: `docker build -t myapp .`'
            },
            {
                'question': 'Volumes in Docker - what are they for?',
                'options': [
                    'Audio settings',
                    'Persist data across container restarts (database files, uploads)',
                    'Not important',
                    'Performance optimization'
                ],
                'correct_answer': 1,
                'explanation': 'Without volumes: container dies → data gone. Volumes persist on host machine. Database needs volume. Uploads need volume. Essential for stateful apps.'
            },
            {
                'question': 'Port mapping (8000:8000) - what does it mean?',
                'options': [
                    'Map 8000 containers to 1 port',
                    'Container port 8000 accessible at localhost:8000 on host',
                    'Not needed for local dev',
                    'For production only'
                ],
                'correct_answer': 1,
                'explanation': '`docker run -p 8000:8000 myapp` = container\'s port 8000 exposed to host\'s port 8000. Visit localhost:8000 to access app. Can map 3000:8000 if needed.'
            },
            {
                'question': 'Docker in production: Should you use it for MVPs?',
                'options': [
                    'Always use Docker',
                    'Docker is optional for MVPs but makes deployment easier. Try simpler hosting first',
                    'Never use Docker',
                    'Docker only for big apps'
                ],
                'correct_answer': 1,
                'explanation': 'Docker useful but adds complexity. For MVP: try Heroku, Railway, Render first (they manage Docker). If scaling becomes hard, Docker helps.'
            }
        ]

        for q in questions_level_15:
            Question.objects.create(
                level=level_15,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 16: Deployment & Hosting
        level_16 = Level.objects.create(
            level_number=16,
            title="Deployment & Hosting",
            description="Learn server hosting options, SSH, domain setup, SSL certificates, and choosing platforms.",
            category="DevOps",
            difficulty="Intermediate",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_16 = [
            {
                'question': 'What\'s the difference between shared hosting, VPS, and PaaS?',
                'options': [
                    'All the same',
                    'Shared: multiple sites on one server (cheap, limited). VPS: dedicated space on server (control, more setup). PaaS: managed platform (easiest, more expensive)',
                    'VPS is always best',
                    'Shared hosting is better'
                ],
                'correct_answer': 1,
                'explanation': 'Shared hosting: $5/mo but slow, limited. VPS (DigitalOcean): $5-15/mo, full control, you manage. PaaS (Heroku): $7+/mo, managed, no server setup. Choose based on control needs.'
            },
            {
                'question': 'Best hosting for indie hacker MVPs?',
                'options': [
                    'AWS - most powerful',
                    'DigitalOcean ($5 VPS), Railway (PaaS, $5 free tier), Render (PaaS, free tier)',
                    'Heroku - cheapest',
                    'All equally good'
                ],
                'correct_answer': 1,
                'explanation': 'DigitalOcean: cheapest VPS, great docs. Railway/Render: easiest deployment (push to git → live). Heroku got expensive. For MVP: try Railway/Render free first.'
            },
            {
                'question': 'What is SSH and why needed for servers?',
                'options': [
                    'Secure Socket Header',
                    'Secure Shell - encrypted remote access to server terminal',
                    'Simple Server Hub',
                    'Not important'
                ],
                'correct_answer': 1,
                'explanation': 'SSH login: `ssh user@server.com`. Encrypted connection to server terminal. Never use password - use SSH keys (public/private). Keys = access to your production server.'
            },
            {
                'question': 'Public key vs Private key in SSH - how to use?',
                'options': [
                    'Both encrypt the same way',
                    'Public key: shared with server (like lock). Private key: keep secret (like key). Only private key unlocks',
                    'Both must be secret',
                    'Don\'t need keys'
                ],
                'correct_answer': 1,
                'explanation': 'SSH key-pair: public key on server, private key on your computer. Server says "prove you have private key" → you sign with it → access granted. Safer than passwords.'
            },
            {
                'question': 'You buy domain myapp.com. How do you point it to your server?',
                'options': [
                    'It works automatically',
                    'Update DNS records: A record points domain to server IP address',
                    'Change server code',
                    'Domain doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Domain registrar (GoDaddy, Namecheap) → DNS settings → A record = your server IP. Propagation takes 24-48h. Test with: `dig yourdomain.com`'
            },
            {
                'question': 'What are SSL/TLS certificates and why required?',
                'options': [
                    'Optional encryption',
                    'Encryption for HTTPS - required for login, payments, modern browsers. Get free from Let\'s Encrypt',
                    'Only for big sites',
                    'Slow down websites'
                ],
                'correct_answer': 1,
                'explanation': 'SSL = encryption. HTTPS = HTTP over SSL. Modern browsers show warning for HTTP. Free certs from Let\'s Encrypt (auto-renew). Essential for any production site.'
            },
            {
                'question': 'Zero-downtime deployment - how to deploy without downtime?',
                'options': [
                    'Impossible',
                    'Blue-green: run old and new versions, switch traffic when new ready',
                    'Deploy at 3am when nobody uses it',
                    'Take site down briefly'
                ],
                'correct_answer': 1,
                'explanation': 'Blue-green: 2 identical production servers. Deploy to green, test, switch traffic. If issue, revert to blue instantly. More complex but no downtime.'
            },
            {
                'question': 'Your server runs out of disk space. What happened?',
                'options': [
                    'Buy new server',
                    'Check logs, database size, uploads folder. Delete old logs, unused files',
                    'Ignore it',
                    'Cloud storage unlimited'
                ],
                'correct_answer': 1,
                'explanation': 'Logs grow forever (rotate and delete). Uploads accumulate. Database grows. Monitor disk usage. Keep 20% free. Set up log rotation (delete logs older than 30 days).'
            },
            {
                'question': 'Database backups - how often should you backup?',
                'options': [
                    'Never needed',
                    'Daily minimum. Automated backups with daily+weekly+monthly retention',
                    'Once a month',
                    'Only when you remember'
                ],
                'correct_answer': 1,
                'explanation': 'Daily backups protect from data loss (hacks, bugs, accidental deletion). Automated = you don\'t forget. DigitalOcean, Railway handle this. If self-hosted, use pg_dump nightly.'
            },
            {
                'question': 'What platform scales best for indie SaaS growth?',
                'options': [
                    'All platforms equal',
                    'Start with PaaS (Railway/Render), scale to VPS (DigitalOcean) if needed. AWS later if massive',
                    'Jump to AWS immediately',
                    'Stick with first choice'
                ],
                'correct_answer': 1,
                'explanation': 'Railway → DigitalOcean → AWS progression. Each step adds control/responsibility. Start simple, scale when you hit limits (usually 10K+ users).'
            }
        ]

        for q in questions_level_16:
            Question.objects.create(
                level=level_16,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 17: CI/CD & Automation
        level_17 = Level.objects.create(
            level_number=17,
            title="CI/CD & Automation",
            description="Learn continuous integration, continuous deployment, GitHub Actions, and automation benefits.",
            category="DevOps",
            difficulty="Intermediate",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_17 = [
            {
                'question': 'What is CI/CD?',
                'options': [
                    'Computer Interface / Design',
                    'Continuous Integration/Deployment - automatically test and deploy on every code push',
                    'Only for big teams',
                    'Not useful for MVPs'
                ],
                'correct_answer': 1,
                'explanation': 'CI: every git push → run tests automatically. CD: if tests pass → auto-deploy. Catches bugs early, deploys fast. GitHub Actions makes it free/easy.'
            },
            {
                'question': 'Should you set up CI/CD for an MVP?',
                'options': [
                    'Yes, immediately',
                    'No, too complex',
                    'Yes if you have tests. Even simple CI (run tests) catches bugs early',
                    'Only for production'
                ],
                'correct_answer': 2,
                'explanation': 'CI is worth it even for MVPs. Catch bugs before production. GitHub Actions is free. Setup takes 30min. Auto-run tests = confidence in deploys.'
            },
            {
                'question': 'What does a GitHub Actions workflow do?',
                'options': [
                    'Organizes your issues',
                    'Runs automated tasks on events: push → run tests, build, deploy',
                    'Manages team permissions',
                    'Tracks deployments'
                ],
                'correct_answer': 1,
                'explanation': 'Workflow = YAML file in .github/workflows/. Triggered by: push, pull request, schedule. Run: npm test, npm build, deploy.sh. Free for public repos.'
            },
            {
                'question': 'Your test suite takes 20 minutes to run. How to speed up deploys?',
                'options': [
                    'Skip tests',
                    'Parallelize tests across jobs (GitHub can run multiple tests simultaneously)',
                    'Only test on production',
                    'Tests slow things down'
                ],
                'correct_answer': 1,
                'explanation': 'GitHub Actions parallelization: run 4 test files at once = 20min → 5min. Matrix builds: test on Node 14, 16, 18 simultaneously. Fast feedback.'
            },
            {
                'question': 'Deployment fails. How to rollback quickly?',
                'options': [
                    'Restore from backup',
                    'Revert last commit, redeploy. Rollback = git revert + push',
                    'Manual fix on production',
                    'Hope it fixes itself'
                ],
                'correct_answer': 1,
                'explanation': 'Bad deployment? `git revert HEAD` undoes it, push, auto-deploy old working version. Faster than fixing forward. This is why automation valuable.'
            },
            {
                'question': 'Environment variables in CI/CD - how to keep secrets safe?',
                'options': [
                    'Commit .env to git',
                    'Add API keys directly to workflow file',
                    'Store secrets in GitHub Secrets, access via ${{ secrets.API_KEY }}',
                    'Email them to yourself'
                ],
                'correct_answer': 2,
                'explanation': 'GitHub Secrets: encrypted at rest, not shown in logs, accessible in workflow. Never commit API keys. Security best practice for CI/CD.'
            },
            {
                'question': 'Should MVPs have automated tests?',
                'options': [
                    'No, too slow',
                    'Yes, even basic tests (critical paths) prevent regressions and confidence in deploys',
                    'Only for large apps',
                    'Tests are expensive'
                ],
                'correct_answer': 1,
                'explanation': 'Start with integration tests for critical paths (auth, payment). Not 100% coverage, but catch big bugs. Pays for itself in saved debugging time.'
            },
            {
                'question': 'Database migrations in deployment - how to handle?',
                'options': [
                    'Run migrations manually after deploy',
                    'Auto-run migrations before deployment (database updated, code updated together)',
                    'Skip migrations',
                    'Do migrations on weekends'
                ],
                'correct_answer': 1,
                'explanation': 'Deployment script: run migrations, then restart app. Coordinated changes ensure database and code match. Prevents errors from schema mismatches.'
            },
            {
                'question': 'CI/CD for indie hackers: What\'s the minimal setup?',
                'options': [
                    'Complex enterprise tools',
                    'GitHub Actions: 1 workflow to run tests, 1 to deploy on success. Free, sufficient for MVPs',
                    'Skip automation',
                    'Need dedicated DevOps team'
                ],
                'correct_answer': 1,
                'explanation': 'GitHub Actions free tier is enough. 2000 minutes/month. Simple: run tests, deploy on green. Scale to more complex workflows later if needed.'
            },
            {
                'question': 'How to preview changes before deploying to production?',
                'options': [
                    'Deploy directly to production',
                    'Create preview/staging deployment on every PR to test before merging',
                    'Only test locally',
                    'Previews too complex'
                ],
                'correct_answer': 1,
                'explanation': 'Preview deployments: PR → auto-deploy to staging URL → test → merge. Catches issues before production. Netlify/Vercel do this automatically.'
            }
        ]

        for q in questions_level_17:
            Question.objects.create(
                level=level_17,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 18: Production Best Practices
        level_18 = Level.objects.create(
            level_number=18,
            title="Production Best Practices",
            description="Learn monitoring, logging, error tracking, backups, and keeping production systems healthy.",
            category="DevOps",
            difficulty="Intermediate",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_18 = [
            {
                'question': 'Why monitor production apps?',
                'options': [
                    'Not necessary',
                    'Catch issues before users do: CPU spikes, memory leaks, database slowness',
                    'Only for enterprises',
                    'Monitoring is expensive'
                ],
                'correct_answer': 1,
                'explanation': 'Monitoring = early warning system. See CPU at 80% → scale before hitting 100%. See slow queries → optimize. Proactive beats reactive.'
            },
            {
                'question': 'What should you monitor in production?',
                'options': [
                    'Nothing, trust it works',
                    'CPU, memory, disk, database connection pool, error rate, response time',
                    'Only when problems occur',
                    'Monitoring costs too much'
                ],
                'correct_answer': 1,
                'explanation': 'Key metrics: CPU (scale if high), Memory (memory leaks), Disk (backups fail if full), Errors (app issues), Response time (performance). Free tools: DataDog, Sentry, New Relic.'
            },
            {
                'question': 'Error tracking - why important?',
                'options': [
                    'Not important, ignore errors',
                    'Catch production errors automatically: stack traces, user context, affected users',
                    'Only for testing',
                    'Too slow for production'
                ],
                'correct_answer': 1,
                'explanation': 'Sentry (error tracking): Python crashes → auto-report with stack trace. Know exactly where bug is. Email alerts for critical errors. Essential for reliability.'
            },
            {
                'question': 'User reports "my account disappeared!" How to investigate?',
                'options': [
                    'Apologize and restore manually',
                    'Check logs (when deleted?), error tracking (any errors?), database backups (when last backup?)',
                    'Give up',
                    'Blame user'
                ],
                'correct_answer': 1,
                'explanation': 'Logs answer: when/what happened. Errors show if bug caused it. Backups show what was deleted. Always have monitoring/backups for these investigations.'
            },
            {
                'question': 'Web server Nginx - what\'s its role?',
                'options': [
                    'Database',
                    'Reverse proxy: handles HTTP requests, routes to app, caches responses, handles SSL',
                    'A programming language',
                    'Not needed'
                ],
                'correct_answer': 1,
                'explanation': 'Nginx sits in front of app: receives HTTP → routes to app → returns response. Handles SSL termination, compression, caching. App focuses on business logic.'
            },
            {
                'question': 'Load balancing - when needed?',
                'options': [
                    'For MVPs immediately',
                    'When single server can\'t handle traffic. Load balancer splits requests across multiple servers',
                    'Never needed',
                    'For databases only'
                ],
                'correct_answer': 1,
                'explanation': 'Single server fine until ~100 concurrent users. Then: multiple servers + load balancer. Railway/Render handle this automatically. DigitalOcean needs manual setup.'
            },
            {
                'question': 'Logs growing too large. How to manage?',
                'options': [
                    'Ignore them',
                    'Log rotation: keep recent logs, delete old ones. Archive to S3. Keep 7-30 days',
                    'Turn off logging',
                    'Logs don\'t take space'
                ],
                'correct_answer': 1,
                'explanation': 'Logs grow daily. Rotate: keep last 7 days local, archive older to cloud. Prevent disk full. Most hosting handles rotation. Check if yours doesn\'t.'
            },
            {
                'question': 'Database backup best practices?',
                'options': [
                    'No backups needed',
                    'Daily automated backups, store in separate region, test restores periodically',
                    'Manual backups once a month',
                    'Backups are optional'
                ],
                'correct_answer': 1,
                'explanation': 'Automated daily backups (24h RPO acceptable). Multi-region (if datacenter fails, have backup elsewhere). Test restores (backups useless if can\'t restore).'
            },
            {
                'question': 'Site is slow. How to find the bottleneck?',
                'options': [
                    'Buy faster server immediately',
                    'Check: CPU/memory usage, database query times, API response times. Profile to find actual problem',
                    'Add more features',
                    'Slow sites just happen'
                ],
                'correct_answer': 1,
                'explanation': 'Measure first: is it CPU? Memory? Database? API calls? Each has different solution. Premature optimization wastes time. Data drives decisions.'
            },
            {
                'question': 'How to prevent database connection leaks?',
                'options': [
                    'Not possible',
                    'Use connection pooling: limit connections, reuse them. Monitor pool exhaustion',
                    'Create new connection per request',
                    'Connections don\'t leak'
                ],
                'correct_answer': 1,
                'explanation': 'Connection pool: max 10 connections to database. Each request gets connection, returns when done. Without pooling: 1000 requests = 1000 connections → out of memory.'
            }
        ]

        for q in questions_level_18:
            Question.objects.create(
                level=level_18,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 19: Git, GitHub & Open Source
        level_19 = Level.objects.create(
            level_number=19,
            title="Git, GitHub & Open Source",
            description="Master version control, GitHub workflows, collaborating with code, and open source contributions.",
            category="Professional",
            difficulty="Beginner",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_19 = [
            {
                'question': 'Why use version control (Git)?',
                'options': [
                    'Not necessary',
                    'Track changes, collaborate, rollback mistakes, understand history of code',
                    'Only for teams',
                    'Git is slow'
                ],
                'correct_answer': 1,
                'explanation': 'Git = code history. See who changed what, when, why. Rollback bad changes. Essential for solo work too (recover mistakes, document decisions).'
            },
            {
                'question': 'What does a commit do?',
                'options': [
                    'Sends code to server',
                    'Saves code snapshot with message describing changes',
                    'Deletes old code',
                    'Commits are optional'
                ],
                'correct_answer': 1,
                'explanation': 'Commit = checkpoint. "Fixed login bug" + code changes. View history: `git log`. Each commit is revertible. Good commits = clear history, easy debugging.'
            },
            {
                'question': 'Branches - why use them?',
                'options': [
                    'Unnecessary complexity',
                    'Separate features: main = stable, feature branches = safe to break, merge when ready',
                    'Only for teams',
                    'Slow things down'
                ],
                'correct_answer': 1,
                'explanation': 'Feature branch: `git checkout -b login-page`. Work safely. When done: merge to main. Main always deployable. This workflow prevents production breaks.'
            },
            {
                'question': 'Merge conflict - what causes it?',
                'options': [
                    'Network error',
                    'Two branches changed same lines differently. Git doesn\'t know which to keep',
                    'Database issue',
                    'Conflicts are impossible'
                ],
                'correct_answer': 1,
                'explanation': 'You edit line 10, teammate edits line 10. Merge → conflict. Resolve: choose your version, their version, or combine. Rebasing avoids some conflicts.'
            },
            {
                'question': 'What should go in .gitignore?',
                'options': [
                    'Nothing, commit everything',
                    '.env, node_modules, __pycache__, .DS_Store (generated/secret files)',
                    'Only code files',
                    'Gitignore optional'
                ],
                'correct_answer': 1,
                'explanation': '.gitignore prevents committing: secrets (.env), generated files (node_modules), OS files (.DS_Store). Standard for every language. Never commit what can be regenerated.'
            },
            {
                'question': 'Pull request (PR) - what\'s the purpose?',
                'options': [
                    'Pulls code from internet',
                    'Code review: propose changes, team reviews before merging to main',
                    'Automatic merge tool',
                    'PRs are unnecessary'
                ],
                'correct_answer': 1,
                'explanation': 'PR workflow: push feature branch → create PR → describe changes → team reviews → approve/request changes → merge. Quality gate. For solo: still useful (review your own work).'
            },
            {
                'question': 'You pushed to main by mistake. How to fix?',
                'options': [
                    'Delete repository',
                    'Revert: `git revert bad_commit` creates new commit undoing changes',
                    'Force delete commit history',
                    'Can\'t be fixed'
                ],
                'correct_answer': 1,
                'explanation': '`git revert` is safe (new commit undoing old one). `git reset --hard` is dangerous (erases history). Revert if pushed (others might have pulled), reset only if local.'
            },
            {
                'question': 'Commit message best practices?',
                'options': [
                    'Write anything',
                    'Clear, concise: "Fix login redirect bug" not "stuff"',
                    'Don\'t need messages',
                    'Messages are optional'
                ],
                'correct_answer': 1,
                'explanation': 'Good message: "Add email verification" = clear what changed. Bad: "update" = no context. Future you (or teammates) reading history thanks clear messages.'
            },
            {
                'question': 'Contributing to open source - what\'s the process?',
                'options': [
                    'Submit code without asking',
                    'Fork repo → make changes → create PR → maintainer reviews → merge if approved',
                    'Only for maintainers',
                    'Too complicated'
                ],
                'correct_answer': 1,
                'explanation': 'Open source: fork → branch → changes → PR. Maintainer might request changes. If approved, merged and credited. Great for learning and portfolio.'
            },
            {
                'question': 'Why build in public on GitHub?',
                'options': [
                    'Not necessary',
                    'Attract users, get feedback early, prove you\'re shipping, learn in public builds audience',
                    'Code theft risk',
                    'GitHub is just for coding'
                ],
                'correct_answer': 1,
                'explanation': 'GitHub = portfolio + progress tracker. Public repos show what you\'ve built. Regular commits show consistency. Indie hackers build in public = community, feedback, users.'
            }
        ]

        for q in questions_level_19:
            Question.objects.create(
                level=level_19,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Part 3 (Levels 15-19)'))
