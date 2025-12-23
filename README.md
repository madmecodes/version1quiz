# Version1 Quiz

Master indie hacking through a 23-level interactive quiz curriculum.

A full-stack learning platform where aspiring indie hackers learn to build, deploy, and market their products. From Linux essentials to launching on Product Hunt, our curriculum covers the complete indie hacking journey.

## What's Inside

- 23 Levels of curated content: Technical Foundations (19), Indie Hacking (3), DSA Fundamentals (1)
- 500+ Questions covering: Linux, Networking, Frontend, Backend, DevOps, Deployment, and Marketing
- Interactive Quiz System with instant feedback, explanations, and XP rewards
- User Progress Tracking with leaderboard and achievement system
- Monorepo Architecture for easy contribution

## Prerequisites

Backend:
- Docker Desktop (includes Docker and Docker Compose)

Frontend:
- Node.js 18 or higher
- npm (comes with Node.js)

## Local Development Setup

The platform uses Docker for the backend and npm for the frontend. Both run independently on your machine.

### Backend Setup

Open a terminal and navigate to the backend directory:

```bash
cd backend
docker-compose up
```

This starts:
- Django API server on http://localhost:8000
- PostgreSQL database on localhost:5432

In another terminal, run migrations and populate example data:

```bash
cd backend
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py seed_example_data
```

To create an admin user for managing data:

```bash
docker-compose exec web python manage.py createsuperuser
```

Then access the admin panel at http://localhost:8000/admin

### Frontend Setup

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
npm install
npm run dev
```

This starts the React development server on http://localhost:5173

Access the application at http://localhost:5173

## Populating Data

You have two options:

### Option 1: Use Example Data (Recommended for Testing)

The example seed data script creates 5 sample levels with 25 questions to help you understand the platform structure:

```bash
cd backend
docker-compose exec web python manage.py seed_example_data
```

This creates:
- Linux Basics (5 questions)
- Git & GitHub (5 questions)
- JavaScript Fundamentals (5 questions)
- React Basics (5 questions)
- Django Basics (5 questions)

### Option 2: Add Data Manually via Admin Panel

1. Start the backend: `cd backend && docker-compose up`
2. Create a superuser: `docker-compose exec web python manage.py createsuperuser`
3. Go to http://localhost:8000/admin
4. Login with your superuser credentials
5. Create Levels and Questions manually

## Environment Configuration

### Backend

The backend uses environment variables defined in `backend/docker-compose.yml`. For custom configuration, you can create a `.env` file in the backend directory using `backend/.env.example` as reference.

Key variables:
- DEBUG: Set to False in production
- SECRET_KEY: Keep this secret
- DATABASE_URL: Configured to use Docker PostgreSQL
- ALLOWED_HOSTS: Add your domain
- CORS_ALLOWED_ORIGINS: Add your frontend URL

### Frontend

The frontend communicates with the backend API. By default, it connects to http://localhost:8000/api

You can optionally create a `.env` file in the frontend directory using `frontend/.env.example` as reference.

## Project Structure

```
version1quiz/
├── backend/
│   ├── quiz/                    # Quiz levels and questions
│   ├── users/                   # User authentication
│   ├── leaderboard/             # Ranking system
│   ├── v1quiz_backend/          # Django settings
│   ├── docker-compose.yml       # Docker configuration
│   ├── Dockerfile               # Backend container definition
│   ├── requirements.txt          # Python dependencies
│   └── manage.py                # Django management script
│
├── frontend/
│   ├── src/
│   │   ├── pages/               # Page components
│   │   ├── components/          # Reusable components
│   │   ├── services/            # API integration
│   │   ├── context/             # State management
│   │   └── main.jsx             # Entry point
│   ├── package.json             # Node dependencies
│   └── vite.config.js           # Vite configuration
│
└── README.md                    # This file
```

## Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository on GitHub

2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/version1quiz.git
   cd version1quiz
   ```

3. Create a branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Make your changes:
   - Backend changes go in the `backend/` folder
   - Frontend changes go in the `frontend/` folder
   - Follow existing code patterns and conventions

5. Test locally:
   - Start both backend and frontend as described above
   - Test your changes thoroughly

6. Commit and push:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request on GitHub with a clear description of your changes

### Contribution Ideas

- Add more levels or questions to the curriculum
- Improve the UI/UX design
- Fix bugs or improve performance
- Add tests
- Improve documentation

## Monorepo Structure

This project uses a monorepo (both backend and frontend in one repository) to make contribution easier:
- Clone once, get everything
- Make changes across backend and frontend in a single commit
- Single issue tracker for all problems
- Simplified onboarding for new contributors

While ideally backend and frontend could be separate repositories, keeping them together reduces friction for contributors and makes atomic commits easier.

## Stopping the Application

Backend (Docker):
```bash
cd backend
docker-compose down
```

Frontend:
Press Ctrl+C in the terminal running npm run dev

## Troubleshooting

Backend won't start:
- Ensure Docker Desktop is running
- Check if ports 5432 and 8000 are not in use
- Run `docker-compose logs` for error details

Frontend won't start:
- Ensure Node.js 18+ is installed: `node --version`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`
- Check if port 5173 is in use

Database issues:
- Restart Docker: `docker-compose down && docker-compose up`

## License

MIT License - feel free to use this project for learning and commercial purposes.

## Support

Found a bug? Have a question? Want to contribute?
- Open an issue on GitHub
- Check existing issues for solutions
- Create a discussion for questions

---

Happy Learning!
