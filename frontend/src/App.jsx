import React, { Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, ProgressProvider, useAuth } from './context';
import { Header, Footer } from './components';
import './App.css';

// Lazy load pages
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const Quiz = React.lazy(() => import('./pages/Quiz'));
const Results = React.lazy(() => import('./pages/Results'));
const Leaderboard = React.lazy(() => import('./pages/Leaderboard'));
const Profile = React.lazy(() => import('./pages/Profile'));
const About = React.lazy(() => import('./pages/About'));
const Register = React.lazy(() => import('./pages/Register'));
const NotFound = React.lazy(() => import('./pages/NotFound'));

// Loading fallback
function LoadingFallback() {
  return (
    <div className="flex items-center justify-center h-screen">
      <div className="text-center">
        <div className="w-12 h-12 border-4 rounded-full animate-spin mx-auto mb-4"
             style={{
               borderColor: 'rgba(255, 215, 0, 0.2)',
               borderTopColor: '#ffd700'
             }}
        />
        <p className="text-yellow-600">Loading...</p>
      </div>
    </div>
  );
}

// Main App Layout
function AppLayout({ children }) {
  const { user, logout } = useAuth();

  return (
    <div className="flex flex-col min-h-screen relative overflow-hidden" style={{ background: '#ffffff' }}>
      {/* Background effects positioned behind content */}
      <div className="fixed inset-0 z-0 pointer-events-none">
        <div className="grid-overlay" />
      </div>

      {/* Content layer */}
      <div className="flex flex-col min-h-screen relative z-10">
        <Header user={user} onLogout={logout} />
        <main className="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-8 pt-24">
          {children}
        </main>
        <Footer />
      </div>
    </div>
  );
}

// App Router Content
function AppRoutes() {
  return (
    <Suspense fallback={<LoadingFallback />}>
      <Routes>
        {/* All routes accessible to everyone - Dashboard is the default */}
        <Route
          path="/dashboard"
          element={
            <AppLayout>
              <Dashboard />
            </AppLayout>
          }
        />
        <Route
          path="/quiz/:levelId"
          element={
            <AppLayout>
              <Quiz />
            </AppLayout>
          }
        />
        <Route
          path="/results/:levelId"
          element={
            <AppLayout>
              <Results />
            </AppLayout>
          }
        />
        <Route
          path="/leaderboard"
          element={
            <AppLayout>
              <Leaderboard />
            </AppLayout>
          }
        />
        <Route
          path="/profile"
          element={
            <AppLayout>
              <Profile />
            </AppLayout>
          }
        />
        <Route
          path="/about"
          element={
            <AppLayout>
              <About />
            </AppLayout>
          }
        />
        <Route
          path="/register"
          element={<Register />}
        />

        {/* Default & 404 Routes */}
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Suspense>
  );
}

export default function App() {
  return (
    <Router>
      <AuthProvider>
        <ProgressProvider>
          <AppRoutes />
        </ProgressProvider>
      </AuthProvider>
    </Router>
  );
}
