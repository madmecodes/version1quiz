"""
Part 1 of indie_hacking_v1.py - Levels 1-7
Linux, Networking, and Frontend Basics
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from quiz.models import Level, Question

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed database with indie hacking curriculum - Part 1 (Levels 1-7)'

    def handle(self, *args, **options):
        # Clear existing data for clean slate
        Level.objects.all().delete()

        # LEVEL 1: Linux Essentials & Why It Matters
        level_1 = Level.objects.create(
            level_number=1,
            title="Linux Essentials & Why It Matters",
            description="Learn why Linux matters for developers and master essential commands for server management.",
            category="Linux",
            difficulty="Beginner",
            xp_reward=100,
            passing_percentage=40
        )

        questions_level_1 = [
            {
                'question': 'You want to deploy your indie SaaS. Why would you choose Linux for your server?',
                'options': [
                    'It\'s the only operating system available',
                    'Most servers worldwide run on Linux; it\'s free, open-source, and gives you full control',
                    'Windows Server is too expensive',
                    'macOS works better for servers'
                ],
                'correct_answer': 1,
                'explanation': 'Linux powers ~96% of web servers worldwide. It\'s free, open-source, stable, and gives indie hackers full control without licensing costs. This is critical for bootstrapped businesses.'
            },
            {
                'question': 'You\'re new to Linux. Which distribution should you start with for learning?',
                'options': [
                    'Arch Linux - minimalist and educational',
                    'Gentoo - highly customizable',
                    'Ubuntu - beginner-friendly, large community, great documentation',
                    'Fedora - cutting edge but unstable'
                ],
                'correct_answer': 2,
                'explanation': 'Ubuntu is the best starting point. It has massive community support, excellent documentation, and most tutorials assume Ubuntu. Once comfortable, you can explore others.'
            },
            {
                'question': 'You need to create a new directory for your project files. Which command do you use?',
                'options': [
                    'ls',
                    'mkdir myproject',
                    'touch myproject',
                    'cd myproject'
                ],
                'correct_answer': 1,
                'explanation': '`mkdir` creates directories. `ls` lists files, `touch` creates empty files, `cd` changes directories. Knowing the right tool for the job is essential for terminal efficiency.'
            },
            {
                'question': 'You want to see all files in a directory including hidden ones. What flag do you add to ls?',
                'options': [
                    'ls -l',
                    'ls -a',
                    'ls -r',
                    'ls -s'
                ],
                'correct_answer': 1,
                'explanation': '`ls -a` shows all files including hidden ones (starting with dot). `-l` shows detailed listing, `-r` reverses order, `-s` shows sizes. Common flags solve real problems.'
            },
            {
                'question': 'A config file got corrupted. You want to delete it permanently. What command?',
                'options': [
                    'touch corrupted.conf',
                    'rm corrupted.conf',
                    'mv corrupted.conf trash',
                    'cp corrupted.conf backup'
                ],
                'correct_answer': 1,
                'explanation': '`rm` removes files permanently. `touch` creates, `mv` moves, `cp` copies. Be careful with `rm` - there\'s no undo. Never use `rm -rf /` unless you want to destroy your system.'
            },
            {
                'question': 'You need to view the contents of a text file. Which command shows it?',
                'options': [
                    'ls config.txt',
                    'cat config.txt',
                    'mkdir config.txt',
                    'pwd config.txt'
                ],
                'correct_answer': 1,
                'explanation': '`cat` displays file contents. `ls` lists files, `mkdir` creates directories, `pwd` shows current path. `cat` is essential for reading configuration and log files.'
            },
            {
                'question': 'You\'re overwhelmed by typing long commands. What shortcuts make terminal faster?',
                'options': [
                    'Press Ctrl+C to cancel and restart',
                    'Use up arrow for history, Tab for autocomplete',
                    'Type everything slowly and carefully',
                    'Use only short commands with no flags'
                ],
                'correct_answer': 1,
                'explanation': 'Up arrow scrolls through command history, Tab autocompletes commands and filenames. These simple shortcuts save hours per year. Mastering them makes you faster at everything.'
            },
            {
                'question': 'You accidentally typed the wrong command. How do you stop it before it executes?',
                'options': [
                    'Press Enter to execute it',
                    'Close the terminal',
                    'Press Ctrl+C to interrupt',
                    'Wait for it to finish'
                ],
                'correct_answer': 2,
                'explanation': 'Ctrl+C stops the currently running command. This saves you from destructive commands. Essential safety skill for anyone working in terminals.'
            }
        ]

        for q in questions_level_1:
            Question.objects.create(
                level=level_1,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 2: File Navigation & System Management
        level_2 = Level.objects.create(
            level_number=2,
            title="File Navigation & System Management",
            description="Master file paths, permissions, and process management for production servers.",
            category="Linux",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_2 = [
            {
                'question': 'Your Node.js app is located at /var/www/myapp. You\'re in /home/user. What\'s the command to navigate there?',
                'options': [
                    'cd myapp',
                    'cd /var/www/myapp',
                    'cd ./var/www/myapp',
                    'mkdir /var/www/myapp'
                ],
                'correct_answer': 1,
                'explanation': 'Use absolute paths starting with / when you need to go to a specific location from anywhere. Relative paths (./myapp) only work from nearby directories. Absolute paths are more reliable in scripts.'
            },
            {
                'question': 'What does the tilde (~) represent in file paths?',
                'options': [
                    'Root directory (/)',
                    'Current directory (.)',
                    'Home directory (/home/username)',
                    'Parent directory (..)'
                ],
                'correct_answer': 2,
                'explanation': '~ is a shortcut to your home directory. Instead of typing /home/themadme, you can use ~. Very useful for navigating quickly to personal directories and dotfiles.'
            },
            {
                'question': 'You want to copy a directory with all its contents. What flag do you need?',
                'options': [
                    'cp oldfolder newfolder',
                    'cp -r oldfolder newfolder',
                    'mv -c oldfolder newfolder',
                    'touch -copy oldfolder newfolder'
                ],
                'correct_answer': 1,
                'explanation': '`cp -r` copies recursively (including all subdirectories). Without `-r`, cp only works on single files. This is crucial when backing up project folders.'
            },
            {
                'question': 'A process is consuming 100% CPU and freezing your server. How do you see running processes?',
                'options': [
                    'ls all',
                    'ps aux',
                    'cat processes',
                    'show running'
                ],
                'correct_answer': 1,
                'explanation': '`ps aux` shows all running processes with details (PID, CPU%, memory%). Once you find the problematic process ID, you can kill it with `kill PID`. Essential for troubleshooting production issues.'
            },
            {
                'question': 'You found the problematic process (PID 1234). How do you stop it?',
                'options': [
                    'rm 1234',
                    'delete PID 1234',
                    'kill 1234',
                    'stop process 1234'
                ],
                'correct_answer': 2,
                'explanation': '`kill PID` terminates a process gracefully. If it doesn\'t work, use `kill -9 PID` for forced termination. This is how you stop runaway processes on production servers.'
            },
            {
                'question': 'Your web server file permissions need to be writable by the server. Which chmod value allows this?',
                'options': [
                    'chmod 444 filename',
                    'chmod 644 filename',
                    'chmod 755 filename',
                    'chmod 777 filename'
                ],
                'correct_answer': 2,
                'explanation': '755 = owner can read/write/execute, group/others can read/execute. Appropriate for web server files. 777 gives everyone everything (security risk). 644 is read-only for others (blocks execution).'
            },
            {
                'question': 'You need sudo (superuser) access to deploy. Why is using `sudo` carefully important?',
                'options': [
                    'It\'s faster to run commands',
                    'It bypasses permissions - one wrong command can destroy your system',
                    'It\'s a Linux requirement',
                    'It\'s just a formality'
                ],
                'correct_answer': 1,
                'explanation': 'sudo bypasses all permission checks. `sudo rm -rf /` would delete your entire system. Never use sudo unless absolutely necessary. Always double-check commands before running with sudo.'
            },
            {
                'question': 'You want to run a script in the background and free up your terminal. What symbol do you use?',
                'options': [
                    'command &&',
                    'command |',
                    'command &',
                    'command >'
                ],
                'correct_answer': 2,
                'explanation': 'The & at the end runs a process in the background. Perfect for long-running tasks like backups or data processing. You get your terminal back while the task continues running.'
            }
        ]

        for q in questions_level_2:
            Question.objects.create(
                level=level_2,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 3: How the Internet Works
        level_3 = Level.objects.create(
            level_number=3,
            title="How the Internet Works",
            description="Understand IP addresses, DNS, HTTP/HTTPS, and cloud platforms for deploying your apps.",
            category="Networking",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_3 = [
            {
                'question': 'What is an IP address and why do servers need one?',
                'options': [
                    'Internet Protocol address - a unique identifier for a device on the internet',
                    'Instant Proxy service for hiding your location',
                    'Internal Processing unit on your computer',
                    'Internet Protection agreement you sign'
                ],
                'correct_answer': 0,
                'explanation': 'IP addresses (like 192.168.1.1 or 8.8.8.8) are unique identifiers. Every device on the internet needs one. Servers need fixed IPs so users can always find them at the same address.'
            },
            {
                'question': 'You buy a domain myapp.com. How does a user\'s browser know where your server is?',
                'options': [
                    'The browser magically finds it',
                    'DNS translates the domain name to your server\'s IP address',
                    'The domain name IS the IP address',
                    'The user types the IP address instead'
                ],
                'correct_answer': 1,
                'explanation': 'DNS (Domain Name System) is like the internet\'s phonebook. When someone types myapp.com, DNS looks up the IP address (like 192.0.2.1) and directs them there. This is why domains are more user-friendly than IPs.'
            },
            {
                'question': 'What\'s the difference between HTTP and HTTPS?',
                'options': [
                    'HTTPS is faster',
                    'HTTP is encrypted, HTTPS is not',
                    'HTTPS is encrypted (secure), HTTP sends data in plain text',
                    'They\'re the same thing'
                ],
                'correct_answer': 2,
                'explanation': 'HTTPS encrypts data between browser and server. HTTP is plain text - anyone on the network can see passwords, credit cards, etc. HTTPS is mandatory for login pages and payment processing.'
            },
            {
                'question': 'What port does HTTP traffic use by default?',
                'options': [
                    '80',
                    '443',
                    '3000',
                    '5000'
                ],
                'correct_answer': 0,
                'explanation': 'Port 80 = HTTP, Port 443 = HTTPS. Ports are like doors on your server. Most web traffic goes through these. Other apps use different ports (3000 for dev, 5432 for databases).'
            },
            {
                'question': 'You\'re choosing a cloud platform for your first SaaS. Which is best for indie hackers?',
                'options': [
                    'AWS - most features but complex pricing',
                    'DigitalOcean - simple pricing, VPS from $4/month, great for beginners',
                    'Google Cloud - enterprise-focused',
                    'Heroku - expensive but easiest'
                ],
                'correct_answer': 1,
                'explanation': 'DigitalOcean offers transparent pricing, simple setup, and excellent documentation for indie hackers. AWS is powerful but overwhelming initially. Heroku was great for MVPs but is expensive for long-term.'
            },
            {
                'question': 'What is localhost and why do developers use it?',
                'options': [
                    'A free hosting service',
                    'The IP address 127.0.0.1 pointing to your own computer for local testing',
                    'A type of server',
                    'A domain you register'
                ],
                'correct_answer': 1,
                'explanation': 'localhost (127.0.0.1) is your machine\'s loopback address. Running your app on localhost lets you test without deploying to a real server. Essential for development - you break things here, not on production.'
            },
            {
                'question': 'DNS propagation is taking hours. Your new site still shows old content. What\'s happening?',
                'options': [
                    'The internet is broken',
                    'DNS changes take 24-48 hours to fully propagate across servers worldwide',
                    'You need to restart your computer',
                    'You didn\'t pay enough for hosting'
                ],
                'correct_answer': 1,
                'explanation': 'DNS changes don\'t happen instantly. Different servers around the world cache old DNS records. Propagation usually takes 24-48 hours. This is why you change DNS well before launch.'
            },
            {
                'question': 'Your indie SaaS processes payments. Which protocol MUST you use?',
                'options': [
                    'HTTP is fine',
                    'FTP for security',
                    'HTTPS - encryption is mandatory for payment data',
                    'Any protocol works'
                ],
                'correct_answer': 2,
                'explanation': 'HTTPS is non-negotiable for payments. PCI compliance requires encryption. Users expect the green lock icon. Any site processing credit cards without HTTPS is committing security malpractice.'
            }
        ]

        for q in questions_level_3:
            Question.objects.create(
                level=level_3,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 4: Network Security & Debugging
        level_4 = Level.objects.create(
            level_number=4,
            title="Network Security & Debugging",
            description="Learn browser DevTools, CORS, and how to debug network issues in your apps.",
            category="Networking",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_4 = [
            {
                'question': 'Your login page shows "Cannot read cookies". How do you debug this in the browser?',
                'options': [
                    'Restart the browser',
                    'Open DevTools (F12), go to Console tab to see JavaScript errors',
                    'Delete all browser data',
                    'Switch browsers'
                ],
                'correct_answer': 1,
                'explanation': 'F12 (or Cmd+Option+I on Mac) opens DevTools. Console tab shows JavaScript errors and warnings. This is your first stop for debugging client-side issues. Network tab shows API calls.'
            },
            {
                'question': 'Your API request is blocked with "CORS error". What\'s happening?',
                'options': [
                    'Your server is down',
                    'Browser security is blocking requests from a different domain',
                    'The API doesn\'t exist',
                    'Your firewall is broken'
                ],
                'correct_answer': 1,
                'explanation': 'CORS (Cross-Origin Resource Sharing) is browser security. If your frontend (myapp.com) calls an API on another domain, the browser blocks it unless the API server explicitly allows it.'
            },
            {
                'question': 'You need to allow your frontend to call your API. What header must your API send?',
                'options': [
                    'Content-Type: application/json',
                    'Access-Control-Allow-Origin: *',
                    'Authorization: Bearer token',
                    'Cache-Control: no-cache'
                ],
                'correct_answer': 1,
                'explanation': 'Access-Control-Allow-Origin header tells the browser which domains can access your API. * allows all (good for MVPs), or specify your domain (better for production).'
            },
            {
                'question': 'You want to see every HTTP request your app makes. Which DevTools tab?',
                'options': [
                    'Console tab',
                    'Elements tab',
                    'Network tab',
                    'Application tab'
                ],
                'correct_answer': 2,
                'explanation': 'Network tab shows every HTTP request/response. See status codes, response times, headers. Perfect for debugging slow APIs or finding failed requests. Filter by XHR to see API calls only.'
            },
            {
                'question': 'Where should you store JWT tokens for maximum security?',
                'options': [
                    'localStorage - easy to access from JavaScript',
                    'sessionStorage - cleared when tab closes',
                    'httpOnly cookies - JavaScript can\'t access them, protected from XSS',
                    'Plain text in HTML'
                ],
                'correct_answer': 2,
                'explanation': 'httpOnly cookies are safest - even if hacked via JavaScript, attackers can\'t read them. localStorage is convenient but vulnerable to XSS. For production auth, use httpOnly cookies.'
            },
            {
                'question': 'What\'s the difference between localStorage and sessionStorage?',
                'options': [
                    'localStorage clears when you close the browser, sessionStorage stays',
                    'localStorage persists forever, sessionStorage is cleared when tab closes',
                    'They\'re the same',
                    'sessionStorage is encrypted'
                ],
                'correct_answer': 1,
                'explanation': 'localStorage persists until manually deleted (good for preferences). sessionStorage clears when you close the tab (good for temporary data). Both are insecure for sensitive data.'
            },
            {
                'question': 'An API request is taking 5 seconds. How do you identify the bottleneck?',
                'options': [
                    'Blame the hosting provider',
                    'Use Network tab in DevTools - see where time is spent (network, server processing)',
                    'Buy faster internet',
                    'Restart your app'
                ],
                'correct_answer': 1,
                'explanation': 'Network tab shows: time waiting for server response vs time downloading. If waiting time is high, your server/database is slow. If download time is high, the response is huge (optimize payload).'
            },
            {
                'question': 'Your API returns 401 Unauthorized. What does this mean?',
                'options': [
                    'The server is down',
                    'You need authentication (login) to access this endpoint',
                    'You don\'t have permission to access',
                    'The request format is wrong'
                ],
                'correct_answer': 1,
                'explanation': '401 means not authenticated (missing/invalid login). 403 means authenticated but not authorized (no permission). Know the difference when building secure APIs.'
            },
            {
                'question': 'How do you safely send sensitive data like API keys to your frontend?',
                'options': [
                    'Put them directly in HTML',
                    'Never send them - use backend to make API calls, send results to frontend',
                    'Send them in localStorage',
                    'Include them in the URL'
                ],
                'correct_answer': 1,
                'explanation': 'Never expose API keys on frontend. Users can see them in Network tab or localStorage. Instead, create backend endpoints that safely call third-party APIs. Frontend calls your backend, backend calls external APIs.'
            }
        ]

        for q in questions_level_4:
            Question.objects.create(
                level=level_4,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 5: APIs & HTTP Methods
        level_5 = Level.objects.create(
            level_number=5,
            title="APIs & HTTP Methods",
            description="Master REST API fundamentals, HTTP methods, status codes, and JSON for building modern web applications.",
            category="APIs",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_5 = [
            {
                'question': 'What is an API and why do you need it for SaaS?',
                'options': [
                    'Advanced Programming Interface - complex math library',
                    'Application Programming Interface - set of rules for software to communicate',
                    'Another Programming Invention',
                    'Automated Page Interface for websites'
                ],
                'correct_answer': 1,
                'explanation': 'APIs let your frontend communicate with your backend. They\'re contracts: "If you send this request, you get this response". Essential for building full-stack applications.'
            },
            {
                'question': 'You want to fetch a user\'s profile from your backend. Which HTTP method?',
                'options': [
                    'POST - creates data',
                    'GET - retrieves data (read-only)',
                    'DELETE - removes data',
                    'PUT - updates everything'
                ],
                'correct_answer': 1,
                'explanation': 'GET retrieves data without changing anything. Safe and idempotent (can call multiple times, same result). GET requests are cached by browsers, improving performance.'
            },
            {
                'question': 'A user signs up with username and password. Which HTTP method?',
                'options': [
                    'GET /signup',
                    'POST /users with email and password in body',
                    'DELETE /register',
                    'PUT /newuser'
                ],
                'correct_answer': 1,
                'explanation': 'POST creates new resources. Send data in the body, not the URL. Never send passwords in URLs (they appear in logs/history). POST should return 201 Created.'
            },
            {
                'question': 'What\'s the difference between PUT and PATCH?',
                'options': [
                    'PUT replaces entire object, PATCH updates specific fields',
                    'PUT is faster',
                    'PATCH is safer',
                    'They\'re the same'
                ],
                'correct_answer': 0,
                'explanation': 'PUT: Send full user object, replaces everything. PATCH: Send only changed fields, updates partially. Use PATCH for APIs (more efficient), PUT for complete replacements.'
            },
            {
                'question': 'You want to delete a user account. Which method and URL structure?',
                'options': [
                    'POST /delete?id=123',
                    'DELETE /users/123',
                    'PUT /users/123/delete',
                    'GET /remove/123'
                ],
                'correct_answer': 1,
                'explanation': 'DELETE /users/123 is RESTful. Resource is in URL path, not query parameters. Only use DELETE for destructive operations. Require confirmation and proper authorization.'
            },
            {
                'question': 'Your API returns status 200 OK after creating a new product. Is this correct?',
                'options': [
                    'Yes, 200 is always correct',
                    'No, should be 201 Created for new resources',
                    'No, should be 204 No Content',
                    'No, should be 202 Accepted'
                ],
                'correct_answer': 1,
                'explanation': '200 OK for successful retrieval/update. 201 Created for successful creation. 204 No Content for successful deletion. Use the right code - clients depend on it.'
            },
            {
                'question': 'A user tries to access another user\'s data. What status code?',
                'options': [
                    '400 Bad Request',
                    '401 Unauthorized',
                    '403 Forbidden',
                    '404 Not Found'
                ],
                'correct_answer': 2,
                'explanation': '403 Forbidden means authenticated but not authorized for that resource. 401 means not logged in. 404 is for "doesn\'t exist". Returning 404 for forbidden data leaks information.'
            },
            {
                'question': 'What is JSON and why is it standard for APIs?',
                'options': [
                    'Java Serialized Object Notation',
                    'JavaScript Object Notation - text format that\'s easy to read, parse, and language-agnostic',
                    'Just Some Object Named',
                    'Java Source Code Notation'
                ],
                'correct_answer': 1,
                'explanation': 'JSON is the web standard. {"name": "John", "age": 30} is readable and works in any language. Much better than XML for APIs.'
            },
            {
                'question': 'Your API client sends JSON but gets an error. What header might be missing?',
                'options': [
                    'Content-Type: text/plain',
                    'Accept: application/json',
                    'Content-Type: application/json',
                    'Authorization: Basic auth'
                ],
                'correct_answer': 2,
                'explanation': 'Content-Type: application/json tells the server what format you\'re sending. Without it, the server might reject or misparse your data. Always include this header.'
            },
            {
                'question': 'You\'re building an API endpoint for filtering users. Which is more RESTful?',
                'options': [
                    'GET /getActiveUsers',
                    'POST /search with filters in body',
                    'GET /users?status=active&role=admin',
                    'PUT /filterusers'
                ],
                'correct_answer': 2,
                'explanation': 'GET /users?status=active uses query parameters for filtering. RESTful = use nouns (users) not verbs (getUsers). Filters go in query string, not the URL path.'
            }
        ]

        for q in questions_level_5:
            Question.objects.create(
                level=level_5,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 6: HTML & CSS Fundamentals
        level_6 = Level.objects.create(
            level_number=6,
            title="HTML & CSS Fundamentals",
            description="Learn semantic HTML, CSS layouts (Flexbox/Grid), and responsive design for building modern UIs.",
            category="Frontend",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_6 = [
            {
                'question': 'Why use semantic HTML tags like <article>, <nav>, <header> instead of <div>?',
                'options': [
                    'They\'re faster',
                    'They improve SEO and accessibility for screen readers',
                    '<div> doesn\'t exist',
                    'It doesn\'t matter'
                ],
                'correct_answer': 1,
                'explanation': 'Semantic HTML helps search engines understand content (better SEO). Screen readers announce structure. <header>, <nav>, <article> are better than generic <div> wrappers.'
            },
            {
                'question': 'Your form asks for email. What input type should you use?',
                'options': [
                    '<input type="text">',
                    '<input type="email">',
                    '<input type="string">',
                    '<textarea>'
                ],
                'correct_answer': 1,
                'explanation': '<input type="email"> validates format, shows email keyboard on mobile, and provides browser validation. Better UX than generic text input.'
            },
            {
                'question': 'Your dashboard looks perfect on desktop but broken on mobile. What CSS approach?',
                'options': [
                    'Build separate desktop and mobile websites',
                    'Use responsive design: Flexbox/Grid + media queries',
                    'Hope users visit on desktop',
                    'Disable mobile viewing'
                ],
                'correct_answer': 1,
                'explanation': 'Mobile-first responsive design is standard now. Flexbox and Grid adapt to screen size. Media queries (@media) adjust styles for small screens. Mobile traffic often exceeds desktop.'
            },
            {
                'question': 'When should you use CSS Grid vs Flexbox?',
                'options': [
                    'Grid for single rows, Flexbox for layouts',
                    'Flexbox for 1D (row/column), Grid for 2D (complex layouts)',
                    'Grid is always better',
                    'Flexbox is always better'
                ],
                'correct_answer': 1,
                'explanation': 'Flexbox excels at: navigation bars, centered content, flexible spacing. Grid excels at: dashboard layouts, photo galleries, page structure. Use the right tool.'
            },
            {
                'question': 'Your buttons are 400px wide on mobile. How do you fix this responsively?',
                'options': [
                    'Make HTML buttons smaller',
                    'Use media queries: @media (max-width: 600px) { button { width: 100%; } }',
                    'Force users to landscape mode',
                    'Remove buttons on mobile'
                ],
                'correct_answer': 1,
                'explanation': 'Media queries adjust styles based on screen size. @media (max-width: 600px) applies styles only on small screens. Essential for responsive design.'
            },
            {
                'question': 'What\'s the CSS box model order from inside out?',
                'options': [
                    'Border, Margin, Padding, Content',
                    'Content, Padding, Border, Margin',
                    'Padding, Content, Border, Margin',
                    'Margin, Padding, Border, Content'
                ],
                'correct_answer': 1,
                'explanation': 'Content (inner text/image) → Padding (space inside border) → Border (outline) → Margin (space outside). Understanding this prevents spacing bugs.'
            },
            {
                'question': 'A button has padding: 10px. Is this padding inside or outside the button?',
                'options': [
                    'Outside (around the button)',
                    'Inside (space between text and border)',
                    'Replaces the button',
                    'Changes button color'
                ],
                'correct_answer': 1,
                'explanation': 'Padding is inside, margin is outside. This distinction matters for clickable areas. Larger padding makes buttons easier to click on mobile.'
            },
            {
                'question': 'Your site needs better accessibility for color-blind users. What\'s important?',
                'options': [
                    'Use only bright colors',
                    'Don\'t rely on color alone - use patterns, labels, contrast',
                    'Disable color styling',
                    'It doesn\'t matter for indie apps'
                ],
                'correct_answer': 1,
                'explanation': 'Color contrast matters (WCAG standards). Don\'t use red/green alone for status. Add icons, patterns, text. Accessibility isn\'t just good ethics - it\'s good business (larger audience).'
            },
            {
                'question': 'What does the meta viewport tag do?',
                'options': [
                    'Shows a preview of your site',
                    'Sets viewport width to device width, enables responsive design',
                    'Controls how many users see your site',
                    'It\'s optional'
                ],
                'correct_answer': 1,
                'explanation': '<meta name="viewport" content="width=device-width"> is essential. Without it, mobile browsers zoom out and your site looks tiny. This single line makes mobile experience good.'
            },
            {
                'question': 'Your hero image looks blurry on high-DPI phones. How do you fix this?',
                'options': [
                    'Use higher resolution images',
                    'Use srcset to provide different images for different screen densities',
                    'Reduce image quality',
                    'Images don\'t need optimization'
                ],
                'correct_answer': 1,
                'explanation': 'srcset attribute lets browsers choose the right image size. <img srcset="img-1x.jpg 1x, img-2x.jpg 2x"> loads crisp images on retina screens without wasting bandwidth on regular screens.'
            }
        ]

        for q in questions_level_6:
            Question.objects.create(
                level=level_6,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        # LEVEL 7: JavaScript Essentials
        level_7 = Level.objects.create(
            level_number=7,
            title="JavaScript Essentials",
            description="Master JavaScript fundamentals: variables, functions, DOM manipulation, and event handling.",
            category="Frontend",
            difficulty="Beginner",
            xp_reward=150,
            passing_percentage=40
        )

        questions_level_7 = [
            {
                'question': 'What\'s the difference between let, const, and var?',
                'options': [
                    'They\'re all the same',
                    'let and const are block-scoped, var is function-scoped. Prefer const by default',
                    'const is faster',
                    'var is always safe'
                ],
                'correct_answer': 1,
                'explanation': 'const prevents reassignment (prefer this). let allows reassignment in block scope. var is legacy - has confusing scope rules. Use const by default, let only if you need reassignment.'
            },
            {
                'question': 'You need to check if a user is logged in. What JavaScript condition?',
                'options': [
                    'if (user = "loggedIn")',
                    'if (user === "loggedIn")',
                    'if user == "loggedIn"',
                    'if (user != "loggedIn")'
                ],
                'correct_answer': 1,
                'explanation': '=== is strict equality (checks type and value). == is loose equality (can cause bugs). Always use === unless you have a specific reason not to.'
            },
            {
                'question': 'You have an array of numbers and need to double each. Which method?',
                'options': [
                    'array.forEach(n => n * 2)',
                    'array.map(n => n * 2)',
                    'array.filter(n => n * 2)',
                    'array.reduce(n => n * 2)'
                ],
                'correct_answer': 1,
                'explanation': '.map() transforms array elements and returns new array. .forEach() just loops (no return). .filter() keeps only matching elements. .reduce() combines elements into one value.'
            },
            {
                'question': 'How do you remove the first element from an array?',
                'options': [
                    'array.remove(0)',
                    'array.pop()',
                    'array.shift()',
                    'array.delete(0)'
                ],
                'correct_answer': 2,
                'explanation': '.shift() removes first element. .pop() removes last. Both modify original array. These are fundamental array methods you use constantly.'
            },
            {
                'question': 'You want to select a button with id "submit-btn" in JavaScript. How?',
                'options': [
                    'document.getElementById("submitbtn")',
                    'document.getElementById("submit-btn")',
                    'document.getElement("submit-btn")',
                    'document.querySelector("submitBtn")'
                ],
                'correct_answer': 1,
                'explanation': 'getElementById() selects by ID. querySelector() is more flexible (can use CSS selectors). Both are ways to grab DOM elements from JavaScript.'
            },
            {
                'question': 'After selecting a button, how do you run code when clicked?',
                'options': [
                    'button.onclick = () => console.log("clicked")',
                    'button.addEventListener("click", () => console.log("clicked"))',
                    'button.onClick = () => console.log("clicked")',
                    'All of the above'
                ],
                'correct_answer': 1,
                'explanation': 'addEventListener is the modern way (supports multiple listeners). onclick works but is outdated. addEventListener is more flexible and standard practice.'
            },
            {
                'question': 'You need to fetch data from your API. What does fetch return?',
                'options': [
                    'The data directly',
                    'A Promise that resolves to the Response',
                    'undefined',
                    'A boolean'
                ],
                'correct_answer': 1,
                'explanation': 'fetch() returns a Promise. Use .then() or async/await to handle the response. This is why async/await is so useful - it makes async code look synchronous.'
            },
            {
                'question': 'The correct way to handle errors in async/await:',
                'options': [
                    'try { await fetch() } catch (err) { handle error }',
                    'Errors are impossible in async/await',
                    'Use .catch() on every fetch',
                    'Ignore errors'
                ],
                'correct_answer': 0,
                'explanation': 'try/catch wraps async code. If anything throws an error, catch handles it. Always use try/catch or .catch() to prevent unhandled promise rejections.'
            },
            {
                'question': 'What does this do: const user = JSON.parse(userString)?',
                'options': [
                    'Converts JavaScript object to JSON string',
                    'Converts JSON string to JavaScript object',
                    'Deletes the user',
                    'Validates JSON'
                ],
                'correct_answer': 1,
                'explanation': 'JSON.parse() converts JSON string to object. JSON.stringify() does opposite. Essential for working with APIs that return JSON.'
            },
            {
                'question': 'You need to stop form submission and run custom code. How?',
                'options': [
                    'form.submit()',
                    'event.preventDefault() in submit handler',
                    'return false',
                    'location.reload()'
                ],
                'correct_answer': 1,
                'explanation': 'event.preventDefault() stops default behavior. Essential for form validation (check data before sending to server). Prevents page reload on submit.'
            }
        ]

        for q in questions_level_7:
            Question.objects.create(
                level=level_7,
                question=q['question'],
                options=q['options'],
                correct_answer=q['correct_answer'],
                explanation=q['explanation']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Part 1 (Levels 1-7)'))
