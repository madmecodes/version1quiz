from django.core.management.base import BaseCommand
from quiz.models import Level, Question


class Command(BaseCommand):
    help = 'Seed database with comprehensive tech indie hacking curriculum'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database with 33 levels...')

        # Clear existing data
        Question.objects.all().delete()
        Level.objects.all().delete()

        levels_data = []

        # ==================== LINUX FUNDAMENTALS (Levels 1-4) ====================

        levels_data.append({
            'level_number': 1,
            'title': 'Why Linux & The Story of Linux',
            'description': 'Understand why Linux is essential for tech and how to dual boot',
            'category': 'Linux',
            'difficulty': 'beginner',
            'xp_reward': 100,
            'passing_percentage': 40,
            'questions': [
                ('Why is Linux important for developers?', ['It is free', 'Most servers run on Linux', 'It has better games', 'It is easier than Windows'], 1, 'Most web servers and production systems run on Linux.'),
                ('What is dual booting?', ['Running two OSes on one computer', 'Using two computers', 'Having two hard drives', 'Running Linux in cloud'], 0, 'Dual booting lets you install multiple operating systems on the same machine.'),
                ('Best Linux distro for beginners?', ['Arch Linux', 'Ubuntu or Pop!_OS', 'Gentoo', 'Linux From Scratch'], 1, 'Ubuntu and Pop!_OS are beginner-friendly with excellent community support.'),
                ('Relationship between Linux and macOS?', ['They are the same', 'Both are Unix-like', 'macOS copied Linux', 'No relationship'], 1, 'Both are Unix-like systems sharing similar command-line tools and philosophy.'),
                ('Before dual booting, you should?', ['Delete files', 'Backup data', 'Buy new laptop', 'Uninstall Windows'], 1, 'Always backup data before partitioning drives to prevent loss.'),
                ('Who created Linux?', ['Bill Gates', 'Linus Torvalds', 'Steve Jobs', 'Richard Stallman'], 1, 'Linus Torvalds created Linux in 1991 as a free Unix-like kernel.'),
            ]
        })

        levels_data.append({
            'level_number': 2,
            'title': 'Linux Tree Structure & Essential Commands',
            'description': 'Master the Linux directory structure and 10 essential commands',
            'category': 'Linux',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('Root directory in Linux?', ['/home', '/root', '/', '/user'], 2, 'The / is the root directory where everything starts.'),
                ('What does "ls" command do?', ['List files/dirs', 'Login system', 'Load software', 'Link server'], 0, 'ls lists files and directories in the current location.'),
                ('"ls -a" shows what?', ['All files', 'Hidden files starting with .', 'Archive files', 'Application files'], 1, '-a flag shows hidden files (starting with dot).'),
                ('Command to create empty file?', ['create', 'touch', 'new', 'file'], 1, 'touch command creates a new empty file.'),
                ('Up arrow key does?', ['Scrolls up', 'Shows previous commands', 'Closes terminal', 'Nothing'], 1, 'Up arrow cycles through previously executed commands.'),
                ('Command to remove files?', ['delete', 'remove', 'rm', 'del'], 2, 'rm (remove) deletes files. Be careful - no recycle bin!'),
                ('Tab key does?', ['Creates tab', 'Auto-completes commands', 'Indents text', 'Nothing'], 1, 'Tab provides auto-completion for commands and filenames.'),
                ('Command to display file contents?', ['show', 'display', 'cat', 'view'], 2, 'cat displays file contents. Example: cat file.txt'),
                ('Command to create directory?', ['newfolder', 'createdir', 'mkdir', 'makefolder'], 2, 'mkdir creates new folders.'),
                ('Command to move/rename files?', ['move', 'mv', 'rename', 'rn'], 1, 'mv moves and renames files.'),
            ]
        })

        levels_data.append({
            'level_number': 3,
            'title': 'Linux File Navigation & Paths',
            'description': 'Master absolute and relative paths, navigation, and advanced commands',
            'category': 'Linux',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('What is absolute path?', ['Path from current dir', 'Path from root /', 'Relative location', 'Shortcut path'], 1, 'Absolute path starts from root /. Example: /home/user/file.txt'),
                ('What is relative path?', ['Path from /', 'Path from current location', 'Path to relatives', 'Shortcut path'], 1, 'Relative path is from current directory. Example: ./projects/file.txt'),
                ('./ represents?', ['Parent directory', 'Current directory', 'Root directory', 'Home directory'], 1, './ refers to current directory.'),
                ('../ represents?', ['Current dir', 'Parent directory', 'Root dir', 'Previous dir'], 1, '../ goes up one level to parent.'),
                ('~ (tilde) represents?', ['Root directory', 'Current dir', 'Home directory', 'Temp dir'], 2, '~ is shortcut to your home directory.'),
                ('Copy directory recursively?', ['cp directory', 'cp -r directory', 'copy directory', 'cp --all directory'], 1, 'cp -r copies directories and all contents.'),
                ('mkdir -p projects/frontend/src does?', ['Makes src only', 'Makes all parent dirs', 'Prints directory', 'Makes private dir'], 1, 'mkdir -p creates parent directories if needed.'),
                ('What are flags in commands?', ['Country flags', 'Options modifying behavior', 'Error messages', 'File types'], 1, 'Flags (like -r, -a) modify how commands work.'),
            ]
        })

        levels_data.append({
            'level_number': 4,
            'title': 'User Management & System Processes',
            'description': 'Learn about users, permissions, and managing system processes',
            'category': 'Linux',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('What does sudo do?', ['Super do everything', 'Superuser do - runs as admin', 'System update', 'Secure download'], 1, 'sudo runs commands with superuser privileges.'),
                ('Command for running processes?', ['processes', 'ps or top', 'running', 'jobs'], 1, 'ps shows processes, top shows real-time.'),
                ('Kill/stop running process?', ['stop id', 'kill id', 'end id', 'terminate id'], 1, 'kill stops processes. kill -9 forcefully terminates.'),
                ('What does chmod do?', ['Changes permissions', 'Changes date', 'Changes owner', 'Changes dir'], 0, 'chmod modifies file permissions (read, write, execute).'),
                ('Command with & at end does?', ['Runs twice', 'Runs in background', 'Runs as root', 'Cancels it'], 1, '& runs command in background.'),
                ('CPU/memory usage command?', ['cpu', 'top or htop', 'memory', 'usage'], 1, 'top and htop show real-time system resource usage.'),
            ]
        })

        # ==================== NETWORKING & INTERNET (Levels 5-8) ====================

        levels_data.append({
            'level_number': 5,
            'title': 'IP Addresses, DNS & Server Platforms',
            'description': 'Understand how devices find each other on the internet',
            'category': 'Networking',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('What is IP address?', ['Internet Protocol - unique address', 'Internet Provider', 'Instant Protocol', 'Internal Password'], 0, 'IP is unique identifier for devices on network.'),
                ('What does DNS do?', ['Downloads files', 'Translates domain to IP', 'Encrypts data', 'Stores passwords'], 1, 'DNS converts names like google.com to IP addresses.'),
                ('Difference IPv4 vs IPv6?', ['No difference', 'IPv6 has more addresses', 'IPv4 faster', 'IPv6 older'], 1, 'IPv6 has more available addresses than IPv4.'),
                ('Cloud platform for developers?', ['Mainframe', 'Digital Ocean', 'Floppy hosting', 'CD-ROM server'], 1, 'Digital Ocean is developer-friendly and affordable.'),
                ('What is AWS?', ['Website', 'Amazon Web Services', 'Anti-virus', 'Programming language'], 1, 'AWS is largest cloud computing platform.'),
                ('What is localhost?', ['Remote server', 'Your computer (127.0.0.1)', 'Cloud server', 'Router'], 1, 'Localhost refers to your own machine.'),
            ]
        })

        levels_data.append({
            'level_number': 6,
            'title': 'HTTP & HTTPS Fundamentals',
            'description': 'Learn how web browsers and servers communicate',
            'category': 'Networking',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('HTTP stands for?', ['HyperText Transfer Protocol', 'High Tech Transfer', 'Hyper Transfer Text', 'Host Transfer'], 0, 'HTTP is protocol for transferring web data.'),
                ('HTTP vs HTTPS difference?', ['Speed', 'HTTPS is encrypted', 'Color', 'Cost'], 1, 'HTTPS encrypts data using TLS/SSL.'),
                ('URL contains?', ['Domain name', 'Protocol, domain, path, params', 'IP address', 'File name'], 1, 'URL: https://example.com/path?param=value'),
                ('HTTP port?', ['21', '80 for HTTP, 443 for HTTPS', '22', '3306'], 1, 'Port 80=HTTP, 443=HTTPS.'),
                ('Why use HTTPS?', ['Faster', 'Security/encryption', 'Better design', 'Lower cost'], 1, 'HTTPS protects user data from eavesdropping.'),
                ('Cookie is?', ['Snack', 'Data stored by browser', 'Error', 'Plugin'], 1, 'Cookies store browser data like sessions.'),
                ('404 error means?', ['Server error', 'Page not found', 'Success', 'Forbidden'], 1, '404 means requested resource not found.'),
            ]
        })

        levels_data.append({
            'level_number': 7,
            'title': 'TCP/IP, TLS & Network Security',
            'description': 'Understand how internet protocols and encryption work',
            'category': 'Networking',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('TCP/IP is?', ['One protocol', 'Suite of protocols', 'Error message', 'File type'], 1, 'TCP/IP is suite of networking protocols.'),
                ('What does TLS do?', ['Transfers data', 'Encrypts communication', 'Lists files', 'Transfers links'], 1, 'TLS encrypts communication between client-server.'),
                ('Man-in-the-middle attack?', ['Computer in middle', 'Attacker intercepts communication', 'Router problem', 'Software bug'], 1, 'MITM: attacker intercepts data between two parties.'),
                ('HTTPS prevents?', ['Slow loading', 'MITM attacks', 'Viruses', 'Malware'], 1, 'HTTPS encryption prevents man-in-the-middle attacks.'),
                ('Port number is?', ['Door on network', 'Server entrance', 'Virtual connection endpoint', 'All of above'], 2, 'Ports are endpoints for network connections.'),
                ('Common ports?', ['80, 443, 22, 3306', 'All same', '8080 only', 'Random numbers'], 0, '80=HTTP, 443=HTTPS, 22=SSH, 3306=MySQL.'),
                ('Firewall purpose?', ['Melts ice', 'Controls network traffic', 'Speeds connection', 'Stores data'], 1, 'Firewall controls incoming/outgoing traffic.'),
            ]
        })

        levels_data.append({
            'level_number': 8,
            'title': 'Browser DevTools & Local Storage',
            'description': 'Learn to use browser developer tools and understand client storage',
            'category': 'Networking',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('Open DevTools with?', ['F5', 'F12 or Ctrl+Shift+I', 'Alt+D', 'Right-click only'], 1, 'F12 or Ctrl+Shift+I opens browser DevTools.'),
                ('Console tab shows?', ['Colors', 'JavaScript errors/logs', 'Images', 'HTML source'], 1, 'Console displays JS errors and console.log output.'),
                ('Network tab shows?', ['Websites list', 'HTTP requests/responses', 'Photos', 'Code editor'], 1, 'Network tab shows all HTTP requests.'),
                ('Local storage is?', ['Remote server', 'Browser-side data storage', 'Cloud storage', 'Email storage'], 1, 'localStorage stores data on client side persistently.'),
                ('Session storage differs?', ['No difference', 'Expires when browser closes', 'Uses cloud', 'Slower'], 1, 'sessionStorage clears when browser closes.'),
                ('localStorage stores?', ['Forever', 'Until cleared by user/code', 'One session', 'One hour'], 1, 'localStorage persists until explicitly deleted.'),
            ]
        })

        # ==================== FRONTEND GENERAL (Levels 9-15) ====================

        levels_data.append({
            'level_number': 9,
            'title': 'HTML Fundamentals',
            'description': 'Learn the building blocks of web pages',
            'category': 'Frontend',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('HTML stands for?', ['Hyper Text Machine Language', 'HyperText Markup Language', 'High Tech', 'Host Transfer'], 1, 'HTML is markup language for web content.'),
                ('HTML tags like <p>?', ['Programming', 'Instructions for browser', 'Formatting files', 'JavaScript'], 1, 'Tags tell browser how to display content.'),
                ('<head> section contains?', ['Body content', 'Metadata, title, scripts', 'Images', 'Links only'], 1, '<head> has metadata like title and styles.'),
                ('<body> section?', ['Never used', 'Contains visible page content', 'For styling', 'For scripts only'], 1, '<body> contains all visible page content.'),
                ('<img> tag needs?', ['Only src', 'src and alt attributes', 'Just alt', 'Nothing'], 1, '<img src="url" alt="description">'),
                ('<a> tag is?', ['Alert', 'Anchor/link', 'Array', 'Attribute'], 1, '<a href="url">Link text</a> creates links.'),
                ('<form> allows?', ['Just display', 'User input collection', 'Images only', 'Styling'], 1, '<form> collects user input data.'),
            ]
        })

        levels_data.append({
            'level_number': 10,
            'title': 'CSS & Styling Basics',
            'description': 'Learn to style and layout web pages',
            'category': 'Frontend',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('CSS stands for?', ['Computer Style Sheet', 'Cascading Style Sheets', 'Color Style', 'Client Side'], 1, 'CSS styles HTML elements.'),
                ('CSS selector p means?', ['Program', 'All <p> tags', 'Paragraph only', 'Parent'], 1, 'p selector targets all <p> elements.'),
                ('.classname selector?', ['Period required', 'Selects elements with class', 'Selects files', 'Function call'], 1, '.classname selects class="classname".'),
                ('#idname selector?', ['Comment', 'Selects element with id', 'Selects all', 'Link'], 1, '#idname selects id="idname".'),
                ('Box model includes?', ['Margin, border, padding, content', 'Colors only', 'Fonts', 'Images'], 0, 'Box model: margin > border > padding > content.'),
                ('Flexbox does?', ['Deletes content', 'Arranges elements flexibly', 'Colors text', 'Adds borders'], 1, 'Flexbox makes responsive layouts.'),
                ('Grid layout for?', ['Deleting', '2D layout control', 'Text only', 'Colors'], 1, 'CSS Grid controls 2D layouts.'),
            ]
        })

        levels_data.append({
            'level_number': 11,
            'title': 'JavaScript Essentials',
            'description': 'Master JavaScript fundamentals for web interactivity',
            'category': 'Frontend',
            'difficulty': 'beginner',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('JavaScript is?', ['Server language', 'Client-side programming language', 'Style language', 'Database'], 1, 'JavaScript adds interactivity to web pages.'),
                ('let vs const?', ['No difference', 'let=reassignable, const=fixed', 'const faster', 'let for objects'], 1, 'const cannot be reassigned, let can.'),
                ('Array methods include?', ['paint', 'push, pop, map, filter', 'color', 'delete'], 1, 'push, pop, map, filter are array methods.'),
                ('Function syntax?', ['func name() {}', 'function name() {}', 'define name() {}', 'method name()'], 1, 'function keyword defines functions.'),
                ('Arrow function?', ['Points to target', 'const fn = (x) => x*2', 'Old syntax', 'Only for objects'], 1, 'Arrow functions: const fn = (x) => x*2'),
                ('Promise is?', ['Gift', 'Async operation eventually resolving', 'Variable', 'Function'], 1, 'Promise handles async operations.'),
                ('async/await?', ['Old syntax', 'Cleaner promise handling', 'Synchronous only', 'Loops'], 1, 'async/await simplifies promise code.'),
                ('DOM is?', ['Data Object Model', 'Document Object Model - HTML tree', 'Data Object Module', 'Double Operator'], 1, 'DOM represents HTML as object tree.'),
                ('DOM manipulation?', ['Delete HTML', 'Change HTML/CSS dynamically', 'Store data', 'Upload files'], 1, 'document.getElementById modifies DOM.'),
                ('Event listener?', ['Listens to music', 'Responds to user actions', 'Reads files', 'Connects internet'], 1, 'element.addEventListener("click", function)'),
            ]
        })

        levels_data.append({
            'level_number': 12,
            'title': 'Package Managers (npm, yarn, bun)',
            'description': 'Manage project dependencies efficiently',
            'category': 'Frontend',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('Package manager is?', ['Food service', 'Tool managing project dependencies', 'Shipping', 'Email client'], 1, 'Package managers handle libraries/dependencies.'),
                ('npm stands for?', ['Network Package Module', 'Node Package Manager', 'New Package Method', 'Network Protocol'], 1, 'npm is JavaScript package manager.'),
                ('package.json contains?', ['Passwords', 'Project metadata and dependencies', 'Images', 'HTML'], 1, 'package.json lists project dependencies.'),
                ('npm install does?', ['Removes packages', 'Downloads dependencies', 'Runs tests', 'Deploys app'], 1, 'npm install fetches dependencies from npm registry.'),
                ('yarn advantage?', ['None', 'Faster, offline mode, better UX', 'Slower', 'Only for backend'], 1, 'yarn improves speed and reliability.'),
                ('bun is?', ['Food', 'Fast modern JS runtime', 'Package', 'Language'], 1, 'bun is faster npm alternative.'),
            ]
        })

        levels_data.append({
            'level_number': 13,
            'title': 'CSS Frameworks & Design Systems',
            'description': 'Use frameworks to build faster with predefined components',
            'category': 'Frontend',
            'difficulty': 'intermediate',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('CSS framework is?', ['Drawing tool', 'Collection of CSS components', 'Programming language', 'Server'],1, 'Frameworks provide ready-made styles.'),
                ('Tailwind CSS?', ['Old framework', 'Utility-first CSS framework', 'Bootstrap', 'SASS'], 1, 'Tailwind uses utility classes.'),
                ('Bootstrap is?', ['Startup process', 'Component framework with predefined classes', 'CSS file', 'JavaScript library'], 1, 'Bootstrap provides responsive components.'),
                ('Utility classes mean?', ['Factories', 'Single-purpose CSS classes', 'Tools', 'Functions'], 1, 'Utilities like pt-4, bg-blue are single-purpose.'),
                ('Why use frameworks?', ['Make it complex', 'Speed up development, consistency', 'Slower', 'For backend only'], 1, 'Frameworks save time and ensure consistency.'),
            ]
        })

        levels_data.append({
            'level_number': 14,
            'title': 'Frontend Architecture & Concepts',
            'description': 'Understand library vs framework, rendering, and architecture patterns',
            'category': 'Frontend',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Library vs Framework?', ['Same thing', 'Library=tools, Framework=structure+tools', 'Framework=library', 'No difference'], 1, 'Libraries are reusable, frameworks are full structure.'),
                ('CSR means?', ['Client Side Rendering - browser renders HTML', 'Server Side', 'Cloud Server', 'Code Section'], 0, 'CSR: browser runs JS to generate HTML.'),
                ('SSR means?', ['Server Side Rendering - server generates HTML', 'Client Side', 'Secure Server', 'Static Site'], 0, 'SSR: server generates complete HTML.'),
                ('SPA is?', ['Spa resort', 'Single Page Application - JS-based navigation', 'Static Page', 'Service Provider'], 1, 'SPA loads once, JS handles navigation.'),
                ('MPA is?', ['Multiple Page Application - server for each page', 'Mobile', 'Marketplace', 'Master Page'], 0, 'MPA: each route loads from server.'),
                ('CSR advantage?', ['Faster server', 'Faster after load, offline capable', 'SEO better', 'Simpler'], 1, 'CSR faster interactions after initial load.'),
                ('SSR advantage?', ['Offline works', 'Better SEO, faster initial load', 'Cheaper', 'Easier'], 1, 'SSR better for SEO and first load.'),
            ]
        })

        levels_data.append({
            'level_number': 15,
            'title': 'Frontend Security & SEO',
            'description': 'Protect users and ensure search engine visibility',
            'category': 'Frontend',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('XSS attack is?', ['Extra SQL', 'Injecting malicious scripts into pages', 'Encryption', 'Browser feature'], 1, 'XSS: attacker injects JavaScript.'),
                ('CSRF attack?', ['Server attack', 'Forcing user to perform unwanted action', 'Encryption', 'SQL injection'], 1, 'CSRF tricks user into unwanted requests.'),
                ('JWT is?', ['Just Web Token', 'JSON Web Token - stateless auth', 'Java Web', 'JavaScript Tool'], 1, 'JWT stores auth info in token.'),
                ('HTTPS vs HTTP?', ['Same', 'HTTPS encrypts, HTTP does not', 'HTTP better', 'HTTPS slower'], 1, 'HTTPS encrypts data in transit.'),
                ('SEO is?', ['Search Engine Optimization - visibility in search', 'Server Endpoint', 'Security', 'Software'], 0, 'SEO improves search engine rankings.'),
                ('Meta tags help?', ['Structure page', 'Improve SEO and social sharing', 'Nothing', 'Design'], 1, '<meta> tags improve SEO.'),
                ('Linting is?', ['Lint removal', 'Finding code errors/style issues', 'Compression', 'Testing'], 1, 'Linters catch errors and enforce style.'),
            ]
        })

        # ==================== REACT SPECIFIC (Level 16) ====================

        levels_data.append({
            'level_number': 16,
            'title': 'React Deep Dive',
            'description': 'Master React components, hooks, and state management',
            'category': 'Frontend',
            'difficulty': 'intermediate',
            'xp_reward': 250,
            'passing_percentage': 40,
            'questions': [
                ('React is?', ['Server language', 'Library for building UIs with components', 'Framework only', 'Styling tool'], 1, 'React is UI library with reusable components.'),
                ('Component is?', ['Server function', 'Reusable UI piece returning JSX', 'CSS class', 'HTML file'], 1, 'Components are building blocks of React.'),
                ('JSX is?', ['Java syntax', 'JavaScript XML - JS+HTML mixing', 'JSON', 'JavaScript function'], 1, 'JSX lets you write HTML-like in JavaScript.'),
                ('Props are?', ['Properties - immutable data passed to components', 'Variables', 'Functions', 'CSS'], 0, 'Props pass data from parent to child.'),
                ('State is?', ['Status', 'Component data that can change', 'Props', 'Constants'], 1, 'State makes components interactive.'),
                ('useState hook?', ['Not used', 'Hook to add state to functional component', 'Class feature', 'Style', ], 1, 'useState(initialValue) creates state variable.'),
                ('useEffect hook?', ['No purpose', 'Runs side effects after render', 'Only for display', 'Loops'], 1, 'useEffect runs code after component renders.'),
                ('Conditional render?', ['Never render', 'Render based on conditions', 'No conditions', 'Static only'], 1, '{isLoggedIn && <Dashboard />}'),
                ('List rendering?', ['No lists', '.map() renders list of components', 'For loops only', 'Static'], 1, 'array.map(item => <Component key={item.id} />)'),
                ('Event handling?', ['No events', 'onClick, onChange respond to user', 'Server only', 'CSS'], 1, '<button onClick={handleClick}>Click</button>'),
            ]
        })

        # ==================== APIs & INTEGRATION (Levels 17-20) ====================

        levels_data.append({
            'level_number': 17,
            'title': 'API Fundamentals & HTTP Methods',
            'description': 'Learn how applications communicate via APIs',
            'category': 'APIs',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('API is?', ['Server only', 'Application Programming Interface - system communication', 'Website', 'Database'], 1, 'API allows apps to communicate.'),
                ('HTTP GET?', ['Sends data', 'Retrieves data from server', 'Deletes', 'Modifies'], 1, 'GET fetches data, cannot send body.'),
                ('HTTP POST?', ['Retrieves', 'Creates/sends data to server', 'Updates', 'Deletes'], 1, 'POST creates new resource.'),
                ('HTTP PUT?', ['Gets data', 'Replaces entire resource', 'Partial update', 'Deletes'], 1, 'PUT replaces full resource.'),
                ('HTTP PATCH?', ['Gets data', 'Partial update of resource', 'Full update', 'Deletes'], 1, 'PATCH modifies part of resource.'),
                ('HTTP DELETE?', ['Gets data', 'Removes resource', 'Updates', 'Creates'], 1, 'DELETE removes a resource.'),
                ('Status code 200?', ['Error', 'Success - OK', 'Redirect', 'Not found'], 1, '200 means request succeeded.'),
                ('Status code 404?', ['Success', 'Not found - resource missing', 'Redirect', 'Error 500'], 1, '404 means resource not found.'),
            ]
        })

        levels_data.append({
            'level_number': 18,
            'title': 'REST & Data Formats',
            'description': 'Understand RESTful API design and data formats',
            'category': 'APIs',
            'difficulty': 'intermediate',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('REST is?', ['Relaxation', 'Architectural style for APIs using HTTP', 'Network', 'Language'], 1, 'REST uses HTTP methods on resources.'),
                ('RESTful design?', ['Random URLs', 'Resource-based URLs with standard methods', 'Database design', 'Server setup'], 1, '/users (GET all), /users/1 (GET one).'),
                ('JSON is?', ['Java', 'JavaScript Object Notation - data format', 'Java Script', 'Just Object'], 1, 'JSON stores data as key-value pairs.'),
                ('JSON object example?', ['[1,2,3]', '{name: "John", age: 30}', 'name: John', '<name>John</name>'], 1, 'JSON uses {} for objects.'),
                ('JSON array?', ['{} only', '[item1, item2, item3]', 'Just strings', 'Numbers only'], 1, 'JSON uses [] for arrays.'),
                ('XML is?', ['Old format', 'eXtensible Markup Language', 'Experimental', 'Extension'], 1, 'XML uses tags like HTML.'),
                ('JSON vs XML?', ['Same', 'JSON smaller/faster, XML more human-readable', 'XML faster', 'No difference'], 1, 'JSON is preferred in modern APIs.'),
            ]
        })

        levels_data.append({
            'level_number': 19,
            'title': 'API Tools: Postman, Bruno, CURL',
            'description': 'Test and debug APIs using professional tools',
            'category': 'APIs',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('Postman is?', ['Mail service', 'API testing tool with GUI', 'Programming language', 'Browser plugin'], 1, 'Postman tests APIs with visual interface.'),
                ('Bruno is?', ['Name', 'Modern open-source API client', 'Language', 'Framework'], 1, 'Bruno is lightweight Postman alternative.'),
                ('CURL is?', ['Wavy', 'Command-line tool for HTTP requests', 'Programming language', 'Browser'], 1, 'curl makes HTTP requests from terminal.'),
                ('curl GET example?', ['curl POST', 'curl https://api.example.com', 'curl localhost', 'curl GET /data'], 1, 'curl https://api.example.com (GET by default).'),
                ('curl POST data?', ['curl -X POST', 'curl -d data', 'curl -X POST -d "data"', 'curl data'], 2, 'curl -X POST -d "key=value" -H "Content-Type: application/json"'),
                ('API headers in Postman?', ['Ignore them', 'Tab for Content-Type, Authorization', 'Not needed', 'URL only'], 1, 'Headers tab sets Content-Type and auth.'),
                ('Why test APIs?', ['No reason', 'Verify endpoints work correctly', 'Waste time', 'Only for backend'], 1, 'Testing ensures API functionality before coding.'),
            ]
        })

        levels_data.append({
            'level_number': 20,
            'title': 'Authentication: JWT, OAuth, API Keys',
            'description': 'Secure APIs and applications with authentication',
            'category': 'APIs',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Authentication?', ['Authorization', 'Verifying user identity', 'Encryption', 'Server'], 1, 'Authentication proves who you are.'),
                ('Authorization?', ['Verifying identity', 'Checking user permissions/access', 'Encryption', 'Same as auth'], 1, 'Authorization defines what you can do.'),
                ('JWT is?', ['Java', 'JSON Web Token for stateless auth', 'Java Web', 'Just Token'], 1, 'JWT stores user info in encoded token.'),
                ('JWT structure?', ['Single string', 'Header.Payload.Signature', 'Object', 'Array'], 1, 'JWT: eyJ0eXAi.eyJzdWI.SflK'),
                ('OAuth is?', ['Open database', 'Open authentication standard', 'Only for email', 'Encryption'], 1, 'OAuth lets users login via third-party (Google, GitHub).'),
                ('API key?', ['Random', 'Unique identifier for app', 'User password', 'Token'], 1, 'API keys authenticate application requests.'),
                ('Bearer token?', ['No use', 'JWT sent in Authorization header', 'Encryption', 'Username'], 1, 'Authorization: Bearer <token>'),
                ('Where store token?', ['Cookies only', 'localStorage or sessionStorage', 'Server only', 'Public'], 1, 'Store tokens in secure client storage.'),
            ]
        })

        # ==================== BACKEND GENERAL (Levels 21-25) ====================

        levels_data.append({
            'level_number': 21,
            'title': 'Backend Fundamentals & Languages',
            'description': 'Understand backend architecture and when to use different languages',
            'category': 'Backend',
            'difficulty': 'beginner',
            'xp_reward': 150,
            'passing_percentage': 40,
            'questions': [
                ('Backend is?', ['User interface', 'Server-side logic and data', 'Database only', 'Frontend'], 1, 'Backend handles data, logic, security.'),
                ('Python good for?', ['Desktop apps only', 'Web, data science, automation', 'Only mobile', 'Graphics'], 1, 'Python versatile for web and data.'),
                ('JavaScript backend?', ['No', 'Yes, with Node.js', 'Only frontend', 'Impossible'], 1, 'Node.js runs JavaScript on server.'),
                ('Django is?', ['Language', 'Python web framework', 'Database', 'Package'], 1, 'Django is Python web framework.'),
                ('Express is?', ['Shipping', 'Node.js web framework', 'Python', 'Database'], 1, 'Express is JavaScript/Node.js framework.'),
                ('REST API?', ['Relaxation', 'Backend API architecture', 'Frontend', 'Database'], 1, 'REST API backend serves frontend/mobile.'),
            ]
        })

        levels_data.append({
            'level_number': 22,
            'title': 'Database Types: SQL vs NoSQL',
            'description': 'Choose the right database for your application',
            'category': 'Backend',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Database stores?', ['Code', 'Persistent data', 'Images only', 'Sessions'], 1, 'Databases store and retrieve data.'),
                ('SQL is?', ['Structured Query Language - relational DB', 'Simple Query', 'Storage Query', 'Server Query'], 0, 'SQL uses tables with relationships.'),
                ('NoSQL is?', ['Not SQL', 'Non-relational database', 'SQL alternative only', 'New SQL'], 1, 'NoSQL stores data flexibly (JSON, documents).'),
                ('PostgreSQL is?', ['No SQL', 'Relational SQL database', 'JavaScript', 'Python'], 1, 'PostgreSQL is powerful open-source SQL DB.'),
                ('MongoDB is?', ['Database manager', 'NoSQL document database', 'SQL database', 'Cache'], 1, 'MongoDB stores JSON documents.'),
                ('Redis is?', ['Result', 'In-memory cache for fast access', 'Database only', 'Language'], 1, 'Redis caches data for speed.'),
                ('SQL advantage?', ['No structure', 'Structure, relationships, ACID safe', 'Flexible', 'No joins'], 1, 'SQL ensures data integrity.'),
                ('NoSQL advantage?', ['Strict', 'Flexible structure, scalable', 'No querying', 'Slower'], 1, 'NoSQL handles flexible data.'),
            ]
        })

        levels_data.append({
            'level_number': 23,
            'title': 'ORM & Database Design',
            'description': 'Map objects to databases and design efficient schemas',
            'category': 'Backend',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('ORM is?', ['Operational Resource', 'Object-Relational Mapping', 'Online Resource', 'Open Resource'], 1, 'ORM maps Python/JS objects to DB tables.'),
                ('Model in ORM?', ['Fashion', 'Represents database table/collection', 'View', 'Controller'], 1, 'Models define database structure.'),
                ('Migration is?', ['Moving data', 'Schema version control', 'Backup', 'Transfer'], 1, 'Migrations manage database changes.'),
                ('Relationship: one-to-many?', ['No relationship', 'One user has many posts', 'Many users one post', 'No connection'], 1, 'One user → many posts relationship.'),
                ('Foreign key?', ['Foreign data', 'Reference to another table', 'Primary key', 'Duplicate'], 1, 'Foreign keys link tables together.'),
                ('Index in database?', ['Catalog', 'Speed up queries on indexed column', 'Encryption', 'Backup'], 1, 'Indexes make queries faster.'),
                ('Normalization?', ['Standardization', 'Reduce data redundancy', 'Encryption', 'Backup'], 1, 'Normalization prevents duplicate data.'),
            ]
        })

        levels_data.append({
            'level_number': 24,
            'title': 'Authentication & Authorization',
            'description': 'Implement secure user authentication in backends',
            'category': 'Backend',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Password hashing?', ['Plain text storage', 'Converting password to irreversible hash', 'Encryption', 'Encoding'], 1, 'Hashing protects passwords from theft.'),
                ('bcrypt/argon2?', ['Programming language', 'Password hashing algorithms', 'Encryption', 'Encoding'], 1, 'Modern secure hashing algorithms.'),
                ('Session vs token?', ['Same', 'Session=server-side, token=client-side', 'Token=session', 'No difference'], 1, 'Sessions store user on server, tokens on client.'),
                ('Logout token?', ['Ignore', 'Invalidate token (blacklist)', 'Session end', 'Clear cookies'], 1, 'Logout requires invalidating auth tokens.'),
                ('Role-based access?', ['Useless', 'Different permissions for user roles', 'No roles', 'All same'], 1, 'Admin vs User roles control access.'),
                ('Permission check?', ['Optional', 'Verify user can perform action', 'Never check', 'Skip'], 1, 'Always verify permissions before action.'),
            ]
        })

        levels_data.append({
            'level_number': 25,
            'title': 'Payment Gateways & Webhooks',
            'description': 'Accept payments and handle webhook events',
            'category': 'Backend',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Payment gateway?', ['Bank only', 'Service processing online payments', 'Credit card', 'Currency'], 1, 'Stripe, PayPal process payments.'),
                ('Stripe is?', ['Paint color', 'Payment processing company', 'Database', 'Language'], 1, 'Stripe handles payments securely.'),
                ('PCI compliance?', ['Optional', 'Security standard for card data', 'Nice to have', 'Marketing'], 1, 'PCI DSS protects payment card info.'),
                ('Webhook is?', ['Web design', 'HTTP callback for real-time events', 'Website hook', 'Web link'], 1, 'Webhooks notify app of events.'),
                ('Stripe webhook?', ['URL', 'Stripe sends event notifications to your URL', 'API call', 'Database'], 1, 'Webhook endpoint receives payment events.'),
                ('Idempotency?', ['Importance', 'Operation produces same result when repeated', 'Dependency', 'Redundancy'], 1, 'Idempotent requests prevent double charges.'),
            ]
        })

        # ==================== DJANGO SPECIFIC (Level 26) ====================

        levels_data.append({
            'level_number': 26,
            'title': 'Django & Django REST Framework',
            'description': 'Master Django web framework and DRF for APIs',
            'category': 'Backend',
            'difficulty': 'intermediate',
            'xp_reward': 250,
            'passing_percentage': 40,
            'questions': [
                ('Django is?', ['Static site builder', 'Python web framework with batteries', 'Frontend', 'Database'], 1, 'Django provides full web development toolkit.'),
                ('MTV pattern?', ['Animated', 'Model-Template-View architecture', 'Database', 'CSS'], 1, 'Django uses MTV pattern.'),
                ('Model defines?', ['Interface', 'Database table structure', 'Views', 'Templates'], 1, 'Models represent database tables.'),
                ('View handles?', ['Display', 'Business logic and data processing', 'Styling', 'Markup'], 1, 'Views contain request logic.'),
                ('Template is?', ['Model', 'HTML with Django template language', 'Python file', 'Database'], 1, 'Templates render dynamic HTML.'),
                ('Middleware?', ['Storage', 'Hooks that process requests/responses', 'Database', 'API'], 1, 'Middleware processes request/response.'),
                ('Django ORM?', ['Operational', 'ORM for writing Python instead of SQL', 'Language', 'Database'], 1, 'ORM lets you use Python objects.'),
                ('DRF?', ['Django', 'Django REST Framework for APIs', 'Database', 'Frontend'], 1, 'DRF builds REST APIs easily.'),
                ('Serializer in DRF?', ['Graphics', 'Converts objects to JSON/vice versa', 'Database', 'Template'], 1, 'Serializers handle API data.'),
                ('Permission class?', ['No control', 'Controls who can access endpoints', 'Database', 'Template'], 1, 'Permissions restrict API access.'),
            ]
        })

        # ==================== DEVOPS (Levels 27-30) ====================

        levels_data.append({
            'level_number': 27,
            'title': 'Docker Fundamentals',
            'description': 'Containerize applications for consistent deployment',
            'category': 'DevOps',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Docker is?', ['Ship company', 'Containerization platform', 'Server', 'Database'], 1, 'Docker packages apps with dependencies.'),
                ('Container is?', ['Box', 'Isolated executable package', 'Virtual machine', 'Server'], 1, 'Containers are lightweight and portable.'),
                ('Image vs Container?', ['Same', 'Image=template, Container=running instance', 'No difference', 'Opposite'], 1, 'Image is blueprint, container is instance.'),
                ('Dockerfile?', ['Text doc', 'Script defining image build', 'Configuration', 'Environment'], 1, 'Dockerfile contains build instructions.'),
                ('docker-compose?', ['Music', 'Orchestrates multiple containers', 'Docker tool', 'Networking'], 1, 'docker-compose runs multi-container apps.'),
                ('Volume in Docker?', ['Sound', 'Persistent storage for containers', 'Networking', 'Memory'], 1, 'Volumes persist data across container restarts.'),
                ('Port mapping?', ['Letter', 'Maps container port to host port', 'Networking', 'Database'], 1, 'Port mapping connects container to host.'),
            ]
        })

        levels_data.append({
            'level_number': 28,
            'title': 'Server Hosting, SSH & Platforms',
            'description': 'Deploy applications to cloud servers safely',
            'category': 'DevOps',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Server hosting?', ['Physical storage', 'Renting server to run app', 'Email', 'Domain'], 1, 'Hosting provides remote server for app.'),
                ('Cloud vs VPS?', ['Same', 'Cloud=scalable, VPS=dedicated portion', 'No difference', 'Opposite'], 1, 'Cloud platforms scale automatically.'),
                ('SSH is?', ['Safety', 'Secure Shell - encrypted remote access', 'Secure Server', 'Shell Script'], 1, 'SSH connects to server securely.'),
                ('SSH key?', ['Door key', 'Cryptographic key pair for auth', 'Password', 'Certificate'], 1, 'SSH keys more secure than passwords.'),
                ('Public key vs private?', ['Same', 'Public=share, private=keep secret', 'No difference', 'Reversed'], 1, 'Private key must never be shared.'),
                ('Deployment?', ['Movement', 'Publishing app to production server', 'Testing', 'Development'], 1, 'Deployment makes app live.'),
                ('AWS vs Digital Ocean?', ['Same', 'AWS=large, DO=simple/dev-friendly', 'No difference', 'Opposite'], 1, 'Choose based on complexity needs.'),
            ]
        })

        levels_data.append({
            'level_number': 29,
            'title': 'CI/CD & Automation',
            'description': 'Automate testing and deployment pipelines',
            'category': 'DevOps',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('CI/CD is?', ['Index', 'Continuous Integration/Deployment', 'Continuous', 'Automation'], 0, 'CI/CD automates build, test, deploy.'),
                ('Continuous Integration?', ['Server hosting', 'Automated testing on code commit', 'Deployment', 'Development'], 1, 'CI runs tests automatically.'),
                ('Continuous Deployment?', ['Manual release', 'Automatic deployment to production', 'Testing', 'Integration'], 1, 'CD releases approved code automatically.'),
                ('GitHub Actions?', ['Repository', 'CI/CD tool built into GitHub', 'Deployment', 'Testing'], 1, 'GitHub Actions automates workflows.'),
                ('Pipeline stages?', ['Steps', 'Build → Test → Deploy sequence', 'Just deploy', 'Testing only'], 1, 'Pipelines run automated steps.'),
                ('Test coverage?', ['Percentage of code tested', 'Running tests', 'Quality', 'Performance'], 0, 'Coverage shows how much code is tested.'),
            ]
        })

        levels_data.append({
            'level_number': 30,
            'title': 'Nginx, Observability & Monitoring',
            'description': 'Monitor applications and optimize with web servers',
            'category': 'DevOps',
            'difficulty': 'intermediate',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Nginx is?', ['Search engine', 'Web server and reverse proxy', 'Database', 'Framework'], 1, 'Nginx serves web content efficiently.'),
                ('Reverse proxy?', ['Backwards', 'Server receiving requests for backend', 'Proxy client', 'Load balancer'], 1, 'Reverse proxy sits in front of backend.'),
                ('Load balancing?', ['Weights', 'Distributing traffic across servers', 'Testing', 'Monitoring'], 1, 'Load balancer spreads traffic.'),
                ('Logging?', ['Information', 'Recording app events/errors', 'Monitoring', 'Testing'], 1, 'Logs help debug issues.'),
                ('Monitoring?', ['Observing', 'Tracking app health/performance', 'Logging', 'Testing'], 1, 'Monitoring alerts you to problems.'),
                ('Metrics?', ['Measurements like response time, CPU', 'Numbers', 'Data', 'All above'], 0, 'Metrics quantify performance.'),
            ]
        })

        # ==================== PROFESSIONAL SKILLS (Levels 31-33) ====================

        levels_data.append({
            'level_number': 31,
            'title': 'Indie Hacker Mindset & DSA',
            'description': 'Problem-solving skills and data structure fundamentals',
            'category': 'Professional',
            'difficulty': 'intermediate',
            'xp_reward': 250,
            'passing_percentage': 40,
            'questions': [
                ('Problem solving first step?', ['Code', 'Understand problem completely', 'Google', 'Ask'],1, 'Understand before coding.'),
                ('DSA is?', ['Data Structures Algorithms - logic fundamentals', 'Database', 'Design', 'Development'], 0, 'DSA critical for efficient code.'),
                ('Array is?', ['Single item', 'Ordered list of elements', 'Dictionary', 'Set'], 1, 'Arrays store multiple values.'),
                ('Linked list?', ['Web link', 'Nodes connected by pointers', 'Array', 'Tree'], 1, 'Linked lists chain nodes together.'),
                ('Hash table?', ['Hashtags', 'Key-value store with fast lookup', 'Array', 'List'], 1, 'Hash tables provide O(1) lookup.'),
                ('Time complexity?', ['Duration', 'How algorithm performance scales', 'Space', 'Speed'], 1, 'O(n), O(log n), O(1) measure efficiency.'),
                ('Big O notation?', ['Large letter', 'Worst-case algorithm complexity', 'Best case', 'Average'], 1, 'Big O describes algorithm scaling.'),
                ('Debugging?', ['Removing bugs', 'Finding and fixing code errors', 'Testing', 'QA'], 1, 'Debugging essential for development.'),
            ]
        })

        levels_data.append({
            'level_number': 32,
            'title': 'Git, GitHub & Version Control',
            'description': 'Manage code and collaborate with teams',
            'category': 'Professional',
            'difficulty': 'beginner',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Git is?', ['Social media', 'Version control system', 'GitHub', 'Repository'], 1, 'Git tracks code changes.'),
                ('Repository?', ['Storage facility', 'Project with version history', 'Database', 'Server'], 1, 'Repo contains all project files/history.'),
                ('Commit?', ['Promise', 'Snapshot of changes with message', 'Push', 'Branch'], 1, 'Commits save code changes.'),
                ('Branch?', ['Tree part', 'Independent development line', 'Main code', 'Version'], 1, 'Branches allow parallel development.'),
                ('Merge?', ['Join', 'Combine two branches', 'Commit', 'Push'], 1, 'Merge integrates branch changes.'),
                ('GitHub is?', ['Git', 'Platform for hosting git repositories', 'Version control', 'Server'], 1, 'GitHub stores code online.'),
                ('Pull request?', ['Retrieve', 'Request to merge branch changes', 'Commit', 'Branch'], 1, 'Pull requests review code before merge.'),
                ('Conflict?', ['Argument', 'Git cannot auto-merge changes', 'Error', 'Issue'], 1, 'Conflicts need manual resolution.'),
            ]
        })

        levels_data.append({
            'level_number': 33,
            'title': 'Open Source & Community',
            'description': 'Contribute to open source and grow in tech community',
            'category': 'Professional',
            'difficulty': 'beginner',
            'xp_reward': 200,
            'passing_percentage': 40,
            'questions': [
                ('Open source?', ['Publicly available', 'Code freely available and modifiable', 'Free software', 'Community'], 1, 'Open source promotes collaboration.'),
                ('GSOC is?', ['Global Summer', 'Google Summer of Code - paid internship', 'Open source', 'Community'], 1, 'GSOC pays students to contribute to open source.'),
                ('MLH is?', ['Machine Learning', 'Major League Hacking - hackathon organizer', 'Open source', 'Community'], 1, 'MLH organizes student coding competitions.'),
                ('Hackathon?', ['Illegal', 'Intense coding competition/event', 'Open source', 'Conference'], 1, 'Hackathons accelerate learning and networking.'),
                ('Contributing to repo?', ['Just for members', 'Anyone can submit improvements', 'Paid only', 'Developers'], 1, 'Open source welcomes all contributors.'),
                ('Pull request review?', ['Ignore', 'Maintainer examines code quality', 'Automatic', 'Not needed'], 1, 'Code review ensures quality.'),
            ]
        })

        # Create all levels and questions
        for level_data in levels_data:
            questions = level_data.pop('questions')
            level = Level.objects.create(**level_data)
            for question_text, options, correct_answer, explanation in questions:
                Question.objects.create(
                    level=level,
                    question=question_text,
                    options=options,
                    correct_answer=correct_answer,
                    explanation=explanation
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with 33 comprehensive levels!'))
        self.stdout.write(f'Total levels: 33')
        self.stdout.write(f'Total questions: {Question.objects.count()}')
