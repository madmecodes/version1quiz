"""
Part 2 of indie_hacking_v1.py - Levels 8-14
Frontend Advanced, Backend Development
"""

from django.core.management.base import BaseCommand
from quiz.models import Level, Question


class Command(BaseCommand):
    help = 'Seed database with indie hacking curriculum - Part 2 (Levels 8-14)'

    def handle(self, *args, **options):
        # LEVEL 8: Async JavaScript & Modern Patterns
        level_8 = Level.objects.create(
            level_number=8,
            title="Async JavaScript & Modern Patterns",
            description="Master Promises, async/await, array methods, and error handling for building responsive apps.",
            category="Frontend",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_8 = [
            {
                'question': 'What\'s the difference between Promises and async/await?',
                'options': [
                    'Promises and async/await are completely different',
                    'async/await is syntactic sugar over Promises - same thing, different syntax',
                    'async/await is faster',
                    'Promises are outdated'
                ],
                'correct_answer': 1,
                'explanation': 'async/await makes asynchronous code look synchronous. Under the hood, it\'s using Promises. Both work, but async/await is more readable. Modern JavaScript prefers async/await.'
            },
            {
                'question': 'You fetch user data but it\'s slow. How do you prevent blocking the UI?',
                'options': [
                    'Use synchronous fetch',
                    'Use async/await - it doesn\'t block the main thread',
                    'Disable JavaScript',
                    'Use setTimeout'
                ],
                'correct_answer': 1,
                'explanation': 'async/await is non-blocking. While waiting for the API, JavaScript can handle user clicks, animations, etc. This is why async is essential for responsive apps.'
            },
            {
                'question': 'When filtering an array, which method is most appropriate?',
                'options': [
                    'array.map(item => item.active)',
                    'array.filter(item => item.active)',
                    'array.forEach(item => item.active)',
                    'array.reduce(item => item.active)'
                ],
                'correct_answer': 1,
                'explanation': '.filter() returns new array with only matching items. .map() transforms all items. .forEach() just loops. Choose the right method for cleaner code.'
            },
            {
                'question': 'You have an array of user IDs and need to sum them. Which method?',
                'options': [
                    'array.map()',
                    'array.filter()',
                    'array.reduce((sum, id) => sum + id, 0)',
                    'array.forEach()'
                ],
                'correct_answer': 2,
                'explanation': '.reduce() combines array elements into one value. Start with 0, add each element. Perfect for sums, averages, or building objects from arrays.'
            },
            {
                'question': 'How do you handle errors in async/await code?',
                'options': [
                    'Errors are impossible',
                    'Use try/catch blocks',
                    'Ignore them',
                    'Use .catch() only'
                ],
                'correct_answer': 1,
                'explanation': 'try { await something } catch (error) { handle }. Any error in the try block triggers catch. Essential for preventing app crashes from network/server errors.'
            },
            {
                'question': 'Multiple API calls in sequence take too long. How do you parallelize?',
                'options': [
                    'Call them one after another',
                    'Use Promise.all([api1(), api2(), api3()]) to call simultaneously',
                    'Increase timeout',
                    'Skip some calls'
                ],
                'correct_answer': 1,
                'explanation': 'Promise.all() runs multiple Promises in parallel. If each takes 1s, all together take ~1s (not 3s). Much faster than sequential calls. Returns array of results in same order.'
            },
            {
                'question': 'You call Promise.all() with 3 requests. One fails. What happens?',
                'options': [
                    'Other 2 succeed anyway',
                    'Entire Promise.all fails immediately',
                    'It waits forever',
                    'Returns partial results'
                ],
                'correct_answer': 1,
                'explanation': 'Promise.all fails fast - if any Promise fails, whole thing fails. Use Promise.allSettled() if you want results regardless of failures. Know the difference for robust code.'
            },
            {
                'question': 'A function is marked async but doesn\'t use await. Is this a problem?',
                'options': [
                    'It\'s fine, async makes it return a Promise',
                    'It wastes resources',
                    'It always errors',
                    'It should be removed'
                ],
                'correct_answer': 0,
                'explanation': 'async functions always return Promises, even without await. Useful if you might add async logic later. No performance penalty, but it signals "this may be async."'
            },
            {
                'question': 'You need to validate email format. What\'s the best approach?',
                'options': [
                    'Use regex pattern /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/',
                    'Send email and check if it bounces',
                    'Ask the user if it\'s correct',
                    'Skip validation'
                ],
                'correct_answer': 0,
                'explanation': 'Regex pattern validates format client-side (fast feedback). But always validate on backend too (security). Real validation needs confirmation email.'
            },
            {
                'question': 'How do you convert a comma-separated string to an array?',
                'options': [
                    'string.split(",")',
                    'string.toArray()',
                    'Array.from(string)',
                    'string.parse()'
                ],
                'correct_answer': 0,
                'explanation': '.split(",") splits string by delimiter. "a,b,c".split(",") → ["a", "b", "c"]. Opposite of .join(). Essential string/array conversion method.'
            }
        ]

        for q in questions_level_8:
            Question.objects.create(
                level=level_8,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 9: Modern Frontend Stack
        level_9 = Level.objects.create(
            level_number=9,
            title="Modern Frontend Stack",
            description="Learn package managers, CSS frameworks, build tools, and rendering strategies (CSR/SSR/SSG).",
            category="Frontend",
            difficulty="Intermediate",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_9 = [
            {
                'question': 'What\'s the difference between package.json and package-lock.json?',
                'options': [
                    'They\'re the same file',
                    'package.json lists dependencies, package-lock.json locks exact versions for consistency',
                    'package-lock.json is optional',
                    'Only one needed'
                ],
                'correct_answer': 1,
                'explanation': 'package.json lists required packages. package-lock.json records exact versions (including sub-dependencies). Commit both to git for reproducible installs across team.'
            },
            {
                'question': 'Should you install packages globally (-g) or locally?',
                'options': [
                    'Always global for speed',
                    'Always local for project isolation',
                    'Global for tools (npm, typescript), local for project dependencies',
                    'Doesn\'t matter'
                ],
                'correct_answer': 2,
                'explanation': 'Global: command-line tools you use everywhere (like `npm` itself). Local: libraries your project needs (React, lodash). Local is safer (no version conflicts between projects).'
            },
            {
                'question': 'Your dependency has a known vulnerability. What command checks?',
                'options': [
                    'npm check',
                    'npm audit',
                    'npm security',
                    'npm vulnerability'
                ],
                'correct_answer': 1,
                'explanation': '`npm audit` scans dependencies for known vulnerabilities. `npm audit fix` auto-fixes some. Always check before deploying to production.'
            },
            {
                'question': 'Tailwind CSS vs Bootstrap: What\'s the trade-off?',
                'options': [
                    'Tailwind is always better',
                    'Bootstrap is always better',
                    'Tailwind utility-first (customizable), Bootstrap pre-built components (faster for MVPs)',
                    'They\'re identical'
                ],
                'correct_answer': 2,
                'explanation': 'Tailwind gives complete control, smaller final bundle if optimized. Bootstrap has pre-built components, faster MVP. For indie hackers starting: Bootstrap gets you launched faster.'
            },
            {
                'question': 'CSR (Client-Side Rendering) vs SSR (Server-Side Rendering)?',
                'options': [
                    'CSR renders in browser, SSR renders on server before sending HTML',
                    'They\'re the same',
                    'CSR is always better',
                    'SSR is always better'
                ],
                'correct_answer': 0,
                'explanation': 'CSR: Fast after initial load, bad SEO, good interactivity. SSR: Better SEO, slower initial load. Next.js and Nuxt use SSR. Choose based on your app\'s needs.'
            },
            {
                'question': 'What is SSG (Static Site Generation)?',
                'options': [
                    'Server Side Garbage collection',
                    'Pre-rendering pages at build time into static HTML files',
                    'A security protocol',
                    'Not used anymore'
                ],
                'correct_answer': 1,
                'explanation': 'SSG pre-builds HTML at build time. Perfect for blogs, documentation, marketing sites. Super fast (CDN + static files). Not suitable for real-time data.'
            },
            {
                'question': 'Your React app bundle is 500KB. This is too large. How do you optimize?',
                'options': [
                    'Buy faster hosting',
                    'Code splitting (lazy load routes), tree shaking (remove unused code), minification',
                    'Delete features',
                    'It\'s fine'
                ],
                'correct_answer': 1,
                'explanation': 'Code splitting: load only needed code per route. Tree shaking: remove unused functions. Minify: compress code. These cut bundle size dramatically. Fast load = better conversions.'
            },
            {
                'question': 'What does minification do?',
                'options': [
                    'Minimizes the number of features',
                    'Removes whitespace, shortens variable names, reduces file size',
                    'Minifies only in production',
                    'Makes code harder to understand'
                ],
                'correct_answer': 1,
                'explanation': 'Minification removes unnecessary characters without changing functionality. `let userName = "John";` becomes `let u="John";`. Smaller files = faster downloads.'
            },
            {
                'question': 'Should you commit node_modules to git?',
                'options': [
                    'Yes, always',
                    'No, add to .gitignore. Re-install with npm install',
                    'Only sometimes',
                    'It doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'node_modules is huge and auto-generated. Never commit it. Add to .gitignore. Team members run `npm install` to get same versions from package-lock.json.'
            },
            {
                'question': 'You\'re building a blog. Which rendering strategy is best?',
                'options': [
                    'CSR - most interactive',
                    'SSR - good for dynamic content',
                    'SSG - pre-render static posts, incredible performance and SEO',
                    'None matter for blogs'
                ],
                'correct_answer': 2,
                'explanation': 'Blog posts don\'t change per user. SSG is perfect: build once, deploy everywhere. Posts appear instantly (static HTML), perfect SEO, minimal server resources.'
            }
        ]

        for q in questions_level_9:
            Question.objects.create(
                level=level_9,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 10: React for Indie Hackers
        level_10 = Level.objects.create(
            level_number=10,
            title="React for Indie Hackers",
            description="Master React fundamentals, hooks, component patterns, and common pitfalls for building UI.",
            category="Frontend",
            difficulty="Intermediate",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_10 = [
            {
                'question': 'What\'s the difference between Props and State?',
                'options': [
                    'Props are data from parent, State is internal component data',
                    'Props and State are the same',
                    'State is immutable, Props are mutable',
                    'Props are only for functions'
                ],
                'correct_answer': 0,
                'explanation': 'Props flow down from parent (immutable in child). State belongs to component (mutable). Props change → component re-renders. State changes → component re-renders. Know the difference!'
            },
            {
                'question': 'When does useEffect run if dependencies array is empty []?',
                'options': [
                    'Every render',
                    'Only once when component mounts',
                    'Never',
                    'After every state change'
                ],
                'correct_answer': 1,
                'explanation': 'Empty dependencies [] = runs once after mount. No dependency array = runs every render. [value] = runs when value changes. Critical for API calls, subscriptions, cleanup.'
            },
            {
                'question': 'You\'re fetching user data in useEffect. But it keeps fetching infinitely. Why?',
                'options': [
                    'Network is slow',
                    'Missing dependency array - useEffect runs on every render, triggering more fetches',
                    'API is broken',
                    'Browser cache issue'
                ],
                'correct_answer': 1,
                'explanation': 'Always include dependency array! useEffect with no [] runs every render. If that fetch sets state, that triggers re-render, useEffect runs again. Infinite loop. Use [].'
            },
            {
                'question': 'You have deeply nested props: page → sidebar → nav → button. This is bad because?',
                'options': [
                    'Props should be passed deeply',
                    'Prop drilling: hard to maintain, hard to track data flow',
                    'It\'s actually optimal',
                    'No downside'
                ],
                'correct_answer': 1,
                'explanation': 'Prop drilling makes refactoring painful. Solution: use Context API or state management (Redux, Zustand). For indie apps, Context usually enough.'
            },
            {
                'question': 'Why do you need a key prop in lists?',
                'options': [
                    'It\'s optional, doesn\'t matter',
                    'Key helps React identify which items changed, improving performance and correctness',
                    'Key is for security',
                    'All lists need same key'
                ],
                'correct_answer': 1,
                'explanation': 'Without keys, React matches by index. Add/remove items → wrong data/behavior. Use unique ID as key. "Don\'t use array index as key" because index changes.'
            },
            {
                'question': 'What\'s controlled vs uncontrolled components?',
                'options': [
                    'Same thing',
                    'Controlled: React manages input value. Uncontrolled: DOM manages it via ref',
                    'Uncontrolled is better',
                    'Controlled is deprecated'
                ],
                'correct_answer': 1,
                'explanation': 'Controlled: <input value={state} onChange={setState} /> = React owns data. Uncontrolled: <input ref={ref} /> = DOM owns data. Controlled is standard for forms.'
            },
            {
                'question': 'A component re-renders too often. How do you prevent unnecessary renders?',
                'options': [
                    'You can\'t',
                    'Use React.memo for function components, useCallback for functions, useMemo for values',
                    'Disable React',
                    'Delete useEffect'
                ],
                'correct_answer': 1,
                'explanation': 'React.memo memoizes component (skip render if props identical). useCallback memoizes functions. useMemo memoizes values. Use when render is expensive.'
            },
            {
                'question': 'Why do closures in useEffect sometimes cause stale data?',
                'options': [
                    'Closures are broken',
                    'useEffect callback closes over variables at run time, not update time. Add to dependencies if needed',
                    'No such issue',
                    'Network issue'
                ],
                'correct_answer': 1,
                'explanation': 'useEffect captures values when it runs. If state changes but useEffect doesn\'t re-run, it uses old state. Solution: add to dependency array.'
            },
            {
                'question': 'You\'re building a big form. Should each field be its own state or one object?',
                'options': [
                    'Each field separate state',
                    'One object with all fields is cleaner, easier to validate and submit',
                    'Depends on form size',
                    'React doesn\'t support object state'
                ],
                'correct_answer': 1,
                'explanation': 'One state object {name, email, message} is easier than 3 separate useState. Better validation (all fields at once), easier to clear form, cleaner submit.'
            },
            {
                'question': 'How do you handle conditional rendering in React?',
                'options': [
                    'Use if/else statements in JSX',
                    'Use ternary: {condition ? <Component /> : null}',
                    'Use && operator: {condition && <Component />}',
                    'All of the above'
                ],
                'correct_answer': 3,
                'explanation': 'All work! Ternary for yes/no branches. && for "show if true, hide if false". if/else only outside JSX. Choose clearest syntax for your case.'
            }
        ]

        for q in questions_level_10:
            Question.objects.create(
                level=level_10,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 11: Backend Fundamentals
        level_11 = Level.objects.create(
            level_number=11,
            title="Backend Fundamentals",
            description="Understand server-side programming, frameworks, REST APIs, and tech stack selection.",
            category="Backend",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_11 = [
            {
                'question': 'What\'s the main difference between frontend and backend?',
                'options': [
                    'No difference',
                    'Frontend = browser (client-side). Backend = server (handles business logic, database)',
                    'Frontend is easier',
                    'Backend doesn\'t need security'
                ],
                'correct_answer': 1,
                'explanation': 'Frontend = what users see/interact with. Backend = hidden logic (auth, payments, database). Users can\'t hack frontend (JS visible), but can hack bad backend. Backend security is critical.'
            },
            {
                'question': 'Should you put sensitive logic on the frontend?',
                'options': [
                    'Yes, it\'s faster',
                    'No, JavaScript is visible to users. Always put auth/payments/secrets on backend',
                    'It doesn\'t matter',
                    'Only sometimes'
                ],
                'correct_answer': 1,
                'explanation': 'Frontend is public. Users can inspect Network tab, see API keys, modify localStorage. Never trust frontend. Backend validates everything.'
            },
            {
                'question': 'Why use environment variables for secrets?',
                'options': [
                    'They make code faster',
                    'Never commit secrets to git. Environment variables keep them out of code',
                    'They\'re optional',
                    'Secrets don\'t need protection'
                ],
                'correct_answer': 1,
                'explanation': 'API keys, database passwords, secret keys in .env files. Never commit .env to git. Use .env.example as template. Load via process.env.API_KEY in code.'
            },
            {
                'question': 'What does REST mean in REST API?',
                'options': [
                    'Really Easy System Transfer',
                    'Representational State Transfer - architecture using HTTP methods on resources',
                    'A relaxation protocol',
                    'Random Exchange State Token'
                ],
                'correct_answer': 1,
                'explanation': 'REST uses: HTTP methods (GET/POST/PUT/DELETE) on resource endpoints (/users, /products). Stateless (no session required). Predictable and standardized.'
            },
            {
                'question': 'Choosing between Django (Python) and Express (Node.js)?',
                'options': [
                    'Django is always better',
                    'Express is always better',
                    'Django: batteries included, great ORM. Express: lightweight, flexible. Choose based on your preference',
                    'They\'re identical'
                ],
                'correct_answer': 2,
                'explanation': 'Django: Python, ORM, admin panel, lots of built-in features. Express: JavaScript, minimal, you choose libraries. For solo founders, Django\'s batteries included is great.'
            },
            {
                'question': 'What is middleware?',
                'options': [
                    'A type of database',
                    'Functions that process requests before reaching your route handler',
                    'A security protocol',
                    'Only for big applications'
                ],
                'correct_answer': 1,
                'explanation': 'Middleware: auth checks, logging, CORS headers, request parsing. They run before handlers. Essential for cross-cutting concerns (affects all routes).'
            },
            {
                'question': 'API returns {user: {id: 1, name: "John"}}. Should it be wrapped?',
                'options': [
                    'Yes, always wrap in object',
                    'Sometimes wrap, sometimes not',
                    'No, return array directly {id: 1, name: "John"}',
                    'It doesn\'t matter'
                ],
                'correct_answer': 0,
                'explanation': 'Wrap response in object for extensibility. Instead of {id: 1}, return {user: {id: 1}, meta: {timestamp: ...}}. Allows adding pagination, metadata without breaking clients.'
            },
            {
                'question': 'How do you handle errors in API responses?',
                'options': [
                    'Always return 200 OK even for errors',
                    'Return proper status code + error object {error: "message", code: "INVALID_EMAIL"}',
                    'Errors crash the server',
                    'Just return error text'
                ],
                'correct_answer': 1,
                'explanation': 'Consistent error format helps client handle errors. Return status code (400, 500) + structured error {error, code}. Frontend can show user-friendly messages.'
            },
            {
                'question': 'What\'s the difference between monolith and microservices?',
                'options': [
                    'Same thing',
                    'Monolith: one codebase, one database. Microservices: separate services, separate databases',
                    'Microservices are always better',
                    'Monoliths are better'
                ],
                'correct_answer': 1,
                'explanation': 'Monolith: simple to start, easier to debug, easier to deploy. Microservices: scalable, complex, overkill for MVPs. Start monolith, split later if needed.'
            },
            {
                'question': 'You\'re building your MVP backend. Should you choose monolith?',
                'options': [
                    'Always choose microservices',
                    'Monolith is perfect for MVPs - simple, fast to build, easy to maintain',
                    'Choose based on coin flip',
                    'Use all three approaches'
                ],
                'correct_answer': 1,
                'explanation': 'Monolith = faster MVP. Easier debugging, deployment, scaling. Microservices overhead isn\'t worth it until you hit real scaling problems. Start simple.'
            }
        ]

        for q in questions_level_11:
            Question.objects.create(
                level=level_11,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 12: Databases for Indie Hackers
        level_12 = Level.objects.create(
            level_number=12,
            title="Databases for Indie Hackers",
            description="Learn SQL vs NoSQL, database design, ORMs, migrations, and performance optimization.",
            category="Backend",
            difficulty="Intermediate",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_12 = [
            {
                'question': 'What\'s the key difference between SQL and NoSQL?',
                'options': [
                    'SQL is older, NoSQL is new',
                    'SQL: structured tables, relationships. NoSQL: flexible documents, no schema',
                    'NoSQL is always faster',
                    'They\'re the same'
                ],
                'correct_answer': 1,
                'explanation': 'SQL (PostgreSQL, MySQL): tables with defined columns, strong relationships. NoSQL (MongoDB): documents without fixed schema, flexible. Choice depends on data structure.'
            },
            {
                'question': 'Building a SaaS with users, subscriptions, and payments. SQL or NoSQL?',
                'options': [
                    'NoSQL - it\'s newer',
                    'SQL - relationships matter. User has many subscriptions, subscriptions have payments',
                    'Doesn\'t matter',
                    'Both equally good'
                ],
                'correct_answer': 1,
                'explanation': 'SQL excels at relationships. Foreign keys ensure data integrity. Transactions ensure consistency. For structured business data, SQL is better.'
            },
            {
                'question': 'What is an ORM and why use it?',
                'options': [
                    'Only Rarely Mandatory',
                    'Object-Relational Mapping - write code (Python objects) instead of SQL queries',
                    'A type of database',
                    'Unnecessary complexity'
                ],
                'correct_answer': 1,
                'explanation': 'ORM (Django ORM, SQLAlchemy) lets you write Python code instead of raw SQL. Safer (prevents SQL injection), faster to develop. Learn SQL basics first, then ORM.'
            },
            {
                'question': 'You have 1 million users. Querying all users takes 10 seconds. How to optimize?',
                'options': [
                    'Buy faster hardware',
                    'Add index to frequently searched columns (email, username)',
                    'Switch databases',
                    'It\'s fine'
                ],
                'correct_answer': 1,
                'explanation': 'Indexes speed up WHERE queries dramatically. CREATE INDEX on email, username. Trade: indexes slow writes (must update index too). Use wisely on frequently queried columns.'
            },
            {
                'question': 'What is the N+1 query problem?',
                'options': [
                    'A mathematical issue',
                    '1 query to fetch users + N queries to fetch each user\'s posts. Inefficient!',
                    'Normal and expected',
                    'Not a real problem'
                ],
                'correct_answer': 1,
                'explanation': 'Fetch 100 users (1 query) then loop fetching each user\'s posts (100 queries) = 101 total. Bad! Solution: eager loading (fetch users with posts in 1 query).'
            },
            {
                'question': 'What are migrations and why important?',
                'options': [
                    'Moving data between servers',
                    'Version control for database schema. Track column additions, deletions over time',
                    'Optional for databases',
                    'Only for big apps'
                ],
                'correct_answer': 1,
                'explanation': 'Migrations = database version control. Add column → migration. Delete table → migration. Reversible (rollback). Essential for teamwork and deployment.'
            },
            {
                'question': 'Your migration failed in production. What do you do?',
                'options': [
                    'Hope it fixes itself',
                    'Rollback to previous migration, diagnose issue, create new migration, redeploy',
                    'Delete database',
                    'Keep broken state'
                ],
                'correct_answer': 1,
                'explanation': 'Rollback: go back to working state. Write new migration fixing the bug. Deploy new migration. This is why migrations matter - allows recovery from mistakes.'
            },
            {
                'question': 'Should you denormalize data (store redundant data)?',
                'options': [
                    'Never denormalize',
                    'Generally normalize for consistency. Denormalize only when query performance matters more',
                    'Always denormalize',
                    'Irrelevant'
                ],
                'correct_answer': 1,
                'explanation': 'Normalized: one place to update. Denormalized: faster reads, but must update in multiple places (error-prone). Cache or views often better than denormalization.'
            },
            {
                'question': 'You need to store many-to-many relationships (users to groups). How?',
                'options': [
                    'Store IDs in array field',
                    'Create junction/pivot table with user_id and group_id',
                    'Duplicate data',
                    'Store JSON objects'
                ],
                'correct_answer': 1,
                'explanation': 'user_groups table: user_id + group_id. Allows efficient queries. A user can belong to many groups, group can have many users. Standard relational database pattern.'
            },
            {
                'question': 'What does ACID mean in databases?',
                'options': [
                    'A type of password',
                    'Atomicity, Consistency, Isolation, Durability - guarantees data integrity',
                    'A new database feature',
                    'Not important'
                ],
                'correct_answer': 1,
                'explanation': 'ACID = reliable databases. Atomicity: all or nothing. Consistency: valid state. Isolation: concurrent transactions don\'t interfere. Durability: survives crashes. SQL databases guarantee ACID.'
            }
        ]

        for q in questions_level_12:
            Question.objects.create(
                level=level_12,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 13: Authentication & Security
        level_13 = Level.objects.create(
            level_number=13,
            title="Authentication & Security",
            description="Learn password hashing, tokens, JWT, OAuth, and security best practices.",
            category="Backend",
            difficulty="Intermediate",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_13 = [
            {
                'question': 'Should you store passwords as plain text?',
                'options': [
                    'Yes, easier to debug',
                    'Absolutely not! Hash passwords with bcrypt or argon2',
                    'Only for small apps',
                    'Plain text is fast'
                ],
                'correct_answer': 1,
                'explanation': 'Never store plain passwords. If database leaks, attackers have all passwords. Hash = one-way function. Even you can\'t see original. bcrypt/argon2 are industry standard.'
            },
            {
                'question': 'What\'s the difference between password hashing and encryption?',
                'options': [
                    'Same thing',
                    'Encryption is reversible (decrypt to original), hashing is one-way (can\'t recover original)',
                    'Hashing is faster',
                    'Encryption is obsolete'
                ],
                'correct_answer': 1,
                'explanation': 'Hashing: input → fixed-length fingerprint (impossible to reverse). Encryption: encrypt → decrypt to original. For passwords, hashing is correct (you never need original).'
            },
            {
                'question': 'User logs in with correct password. How do you verify without storing plaintext?',
                'options': [
                    'You can\'t verify',
                    'Hash the provided password with same salt, compare hashes',
                    'Store plaintext and compare',
                    'Ask user to confirm'
                ],
                'correct_answer': 1,
                'explanation': '1. User provides password. 2. Hash it with salt from database. 3. Compare hash to stored hash. If match, password correct. bcrypt handles this automatically.'
            },
            {
                'question': 'What\'s the difference between JWT and session-based authentication?',
                'options': [
                    'Same thing',
                    'Sessions: store state on server. JWT: stateless token, server doesn\'t store anything',
                    'JWT is always better',
                    'Sessions are always better'
                ],
                'correct_answer': 1,
                'explanation': 'Sessions: server remembers who you are (needs database lookup). JWT: token contains encrypted info, server just verifies. JWT is stateless (scales better), sessions are simpler.'
            },
            {
                'question': 'JWT has 3 parts: Header.Payload.Signature. What\'s in Payload?',
                'options': [
                    'Password',
                    'User claims: user_id, email, roles (not secrets!)',
                    'Secret key',
                    'Timestamp only'
                ],
                'correct_answer': 1,
                'explanation': 'JWT Payload contains user info (user_id, email, exp time). Not secrets - anyone can decode. Signature proves it wasn\'t tampered with. Never put passwords in JWT.'
            },
            {
                'question': 'Where should you store JWT tokens on frontend for security?',
                'options': [
                    'localStorage - convenient',
                    'sessionStorage',
                    'httpOnly cookies - JavaScript can\'t access, protected from XSS',
                    'HTML element'
                ],
                'correct_answer': 2,
                'explanation': 'httpOnly cookies are safest - even XSS attack can\'t read them. localStorage is vulnerable if JavaScript is compromised. For production auth, use httpOnly.'
            },
            {
                'question': 'What is OAuth and when do you use it?',
                'options': [
                    'Encryption protocol',
                    'Allows login via Google/GitHub - user logs in with their account, app gets permission',
                    'Same as JWT',
                    'Outdated security'
                ],
                'correct_answer': 1,
                'explanation': 'OAuth: "Login with Google" button. User enters Google password on Google\'s site (not yours). Google tells your app "this is valid user". Safer than storing passwords.'
            },
            {
                'question': 'Your API has no rate limiting. What\'s the risk?',
                'options': [
                    'No risk',
                    'Attackers can brute force (try million password combinations) or DDoS (overwhelm server)',
                    'Rate limiting only for public APIs',
                    'Performance doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Rate limiting: max 10 requests per minute per IP. Prevents brute force attacks on login, API abuse. Essential for any production app.'
            },
            {
                'question': 'When should passwords be validated on backend vs frontend?',
                'options': [
                    'Only frontend (faster)',
                    'Only backend (secure)',
                    'Both - frontend for UX, backend for security',
                    'Validation is optional'
                ],
                'correct_answer': 2,
                'explanation': 'Frontend validation for user experience (instant feedback). Backend validation for security (users can bypass frontend). Always validate on server.'
            },
            {
                'question': 'A user account is compromised. What should the platform do?',
                'options': [
                    'Nothing, tell them to change password',
                    'Force password change, invalidate all sessions, allow 2FA setup',
                    'Delete account',
                    'Lock account forever'
                ],
                'correct_answer': 1,
                'explanation': 'Force password change (weak password was vulnerability). Invalidate existing sessions (log out everywhere). Offer 2FA for future security. Minimize damage.'
            }
        ]

        for q in questions_level_13:
            Question.objects.create(
                level=level_13,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 14: Payments & Monetization Tech
        level_14 = Level.objects.create(
            level_number=14,
            title="Payments & Monetization Tech",
            description="Learn payment processing, subscription models, webhooks, and monetization strategies.",
            category="Backend",
            difficulty="Intermediate",
            xp_reward=200,
            passing_percentage=40
        )

        questions_level_14 = [
            {
                'question': 'What payment gateway is best for indie SaaS?',
                'options': [
                    'Stripe - industry standard, great documentation, flexible pricing',
                    'PayPal - older, more complicated',
                    'Square - good for retail',
                    'All equally good'
                ],
                'correct_answer': 0,
                'explanation': 'Stripe: $0.30 + 2.9% per transaction, excellent docs, test mode. Perfect for MVP. Paddle and LemonSqueezy are Stripe alternatives with better indie positioning.'
            },
            {
                'question': 'One-time purchase vs subscription: Which is easier?',
                'options': [
                    'Both equally easy',
                    'One-time: simpler. Subscription: requires recurring billing, handling failures',
                    'Subscription: simpler',
                    'Neither matters'
                ],
                'correct_answer': 1,
                'explanation': 'One-time: charge once, done. Subscription: charge monthly, handle failed cards, refunds, cancellations. More complex but recurring revenue is more predictable.'
            },
            {
                'question': 'What is a webhook and why needed for payment processing?',
                'options': [
                    'Website hook (decoration)',
                    'HTTP callback from Stripe when payment events occur (charge succeeded, subscription cancelled)',
                    'A type of database',
                    'Not important'
                ],
                'correct_answer': 1,
                'explanation': 'Webhook: Stripe calls your endpoint → "payment_intent.succeeded". You update database (mark as paid), send email, grant access. Webhooks trigger business logic.'
            },
            {
                'question': 'A user pays and you activate their account. But webhook fails silently. How to prevent?',
                'options': [
                    'Hope it doesn\'t happen',
                    'Idempotency keys + webhook retries. Stripe retries failed webhooks. Your code should handle duplicate notifications gracefully',
                    'Don\'t use webhooks',
                    'Ignore failures'
                ],
                'correct_answer': 1,
                'explanation': 'Idempotency: same request twice = same result. If webhook fires twice, you activate once. Stripe retries webhooks if your server fails. Design for failures.'
            },
            {
                'question': 'Customer upgrades from $10/mo to $20/mo plan. How to handle billing?',
                'options': [
                    'Charge immediately for full month',
                    'Pro-rate: charge difference for remaining days of cycle',
                    'Ignore, upgrade next month',
                    'Give free upgrade'
                ],
                'correct_answer': 1,
                'explanation': 'Pro-rating is fair: customer paid for $10 plan, now getting $20 plan. Calculate $20 - $10 for remaining days, charge difference. Better customer satisfaction.'
            },
            {
                'question': 'What is PCI compliance for payment processing?',
                'options': [
                    'Personal Computer Interface',
                    'Payment Card Industry - standards requiring encryption, security, audits for credit card handling',
                    'Not important',
                    'Only for big companies'
                ],
                'correct_answer': 1,
                'explanation': 'PCI DSS requires: HTTPS, strong auth, secure development. Never handle credit card details directly - Stripe handles it. Never store raw card numbers. Use tokens.'
            },
            {
                'question': 'Your SaaS charges $29/month. Should price be $29 or $30?',
                'options': [
                    'Doesn\'t matter',
                    '$30 - rounder number',
                    '$29 - psychological pricing, feels cheaper, slightly higher conversion',
                    'Use $19.99'
                ],
                'correct_answer': 2,
                'explanation': 'Charm pricing: $29 converts better than $30 (even though $1 difference is tiny). Brain reads $2X as significantly cheaper than $3X. Works for indie products.'
            },
            {
                'question': 'A failed subscription payment. How many times should you retry?',
                'options': [
                    'Once only',
                    'Retry 2-3 times over days (card might have temporary issue). Send email reminder. Cancel if all fail.',
                    'Retry forever',
                    'Don\'t retry'
                ],
                'correct_answer': 1,
                'explanation': 'Stripe auto-retries 3 times over days. You send dunning emails ("Update payment method"). After failures, cancel and follow up. Recover many customers this way.'
            },
            {
                'question': 'You\'re implementing refunds. What should you check?',
                'options': [
                    'No checks needed',
                    'Check if payment succeeded, refund was not already issued, not outside refund window',
                    'Refund anyone',
                    'Don\'t allow refunds'
                ],
                'correct_answer': 1,
                'explanation': 'Refund validation: payment succeeded, not already refunded, within policy (7-30 days), charge was not disputed. Stripe handles some checks, you handle business logic.'
            },
            {
                'question': 'How do you test payment integration without processing real transactions?',
                'options': [
                    'Test on production with real card',
                    'Use test card numbers in test mode (e.g., 4242 4242 4242 4242)',
                    'Don\'t test',
                    'Ask users to test'
                ],
                'correct_answer': 1,
                'explanation': 'Stripe test mode uses fake card numbers that don\'t charge. 4242 4242 4242 4242 = success. 4000 0000 0000 0002 = decline. Test thoroughly before launch.'
            }
        ]

        for q in questions_level_14:
            Question.objects.create(
                level=level_14,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Part 2 (Levels 8-14)'))
