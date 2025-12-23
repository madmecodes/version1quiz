# Version1 Quiz - Indie Hacker Learning Platform

**Master indie hacking through a 23-level interactive quiz curriculum.**

A full-stack learning platform where aspiring indie hackers learn to build, deploy, and market their products. From Linux essentials to launching on Product Hunt, our curriculum covers the complete indie hacking journey.

## 🎯 What's Inside

- **23 Levels** of curated content: Technical Foundations (19), Indie Hacking (3), DSA Fundamentals (1)
- **500+ Questions** covering: Linux, Networking, Frontend, Backend, DevOps, Deployment, and Marketing
- **Interactive Quiz System** with instant feedback, explanations, and XP rewards
- **User Progress Tracking** with leaderboard and achievement system
- **Monorepo Architecture** for easy contribution and deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.9+ (Backend)
- Node.js 18+ (Frontend)
- PostgreSQL 12+ (Database)
- Docker & Docker Compose (Optional, recommended)

### Setup (Docker - Easiest)

```bash
# Clone the repository
git clone https://github.com/madmecodes/version1quiz.git
cd version1quiz

# Start the stack
docker-compose up

# In another terminal, migrate database and populate data
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py indie_hacking_v1

# Access the app
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# Admin Panel: http://localhost:8000/admin
```

### Setup (Local Development)

#### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file and configure
cp .env.example .env
# Edit .env with your settings (DATABASE_URL, SECRET_KEY, etc.)

# Run migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser

# Populate curriculum data
python manage.py indie_hacking_v1

# Start server
python manage.py runserver
```

#### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.example .env
# Edit .env with VITE_API_URL (e.g., http://localhost:8000)

# Start development server
npm run dev
```

## 📊 Populating Data

### Option 1: Automatic Curriculum (Recommended)
```bash
docker-compose exec web python manage.py indie_hacking_v1
```
Populates all 23 levels with 500+ questions instantly.

### Option 2: Add Specific Level
```bash
docker-compose exec web python manage.py indie_hacking_v1_part6  # Level 23 only
```

### Option 3: Admin Panel
1. Go to `http://localhost:8000/admin`
2. Login with superuser credentials
3. Create Levels → Add Questions manually
4. Manage Users and Progress

## 🔧 Environment Configuration

### Backend (.env.example)
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/v1quiz_db
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
GOOGLE_OAUTH_CLIENT_ID=your-google-oauth-id
```

### Frontend (.env.example)
```env
VITE_API_URL=http://localhost:8000/api
```

## 🤝 Contributing

We love contributions! Here's how to get started:

1. **Fork & Clone**
   ```bash
   git clone https://github.com/yourusername/version1quiz.git
   cd version1quiz
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Backend changes: `backend/` folder
   - Frontend changes: `frontend/` folder
   - Follow existing code patterns

4. **Test Locally**
   - Ensure all tests pass
   - Test both backend and frontend

5. **Push & Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Create a Pull Request with description of changes

### Contribution Ideas
- Add more levels/questions
- Improve UI/UX
- Fix bugs
- Optimize performance
- Add tests
- Improve documentation

## 📚 Project Structure

```
version1quiz/
├── backend/              # Django REST API
│   ├── quiz/            # Quiz questions and levels
│   ├── users/           # Authentication and profiles
│   ├── leaderboard/     # Rankings and progress
│   └── manage.py
├── frontend/            # React + Vite
│   ├── src/
│   │   ├── pages/      # Quiz, Results, Dashboard
│   │   ├── components/ # Reusable UI components
│   │   ├── services/   # API integration
│   │   └── context/    # State management
│   └── package.json
├── docker-compose.yml   # Full stack setup
└── README.md
```

## 🏗️ Monorepo Structure (Why?)

Both backend and frontend are in the same repository for **ease of contribution**:
- Clone once, get everything
- Atomic commits across frontend & backend
- Shared CI/CD pipeline
- Single issue tracker
- Easier collaboration

Deployment is still separate:
- **Backend**: Railway or Render
- **Frontend**: Vercel
- Both pull from same GitHub repo using root directory settings

## 🚀 Deployment

### Backend (Railway)
```
Root Directory: backend/
Framework: Django
Database: PostgreSQL (auto-created)
```

### Frontend (Vercel)
```
Root Directory: frontend/
Framework: Vite
Build Command: npm run build
```

See [Deployment Guide](DEPLOYMENT.md) for detailed instructions.

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Built with:
- Django & Django REST Framework
- React & Vite
- PostgreSQL
- TailwindCSS

## 📞 Support

- Found a bug? Open an [Issue](https://github.com/madmecodes/version1quiz/issues)
- Have a question? Start a [Discussion](https://github.com/madmecodes/version1quiz/discussions)
- Want to contribute? See [Contributing](#-contributing)

---

**Happy Learning & Building! 🚀**
