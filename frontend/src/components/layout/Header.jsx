import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { IoHome, IoLogOut, IoMenu, IoClose } from 'react-icons/io5';
import { Button } from '../common';
import LoginModal from '../../pages/Login';
import v1logo from '../../assets/v1logo.png';

export const Header = ({ user, onLogout, ...props }) => {
  const navigate = useNavigate();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [showLoginModal, setShowLoginModal] = useState(false);

  const handleLogout = () => {
    onLogout?.();
    navigate('/');
    setMobileMenuOpen(false);
  };

  const isActive = (path) => {
    return window.location.pathname === path;
  };

  const getLinkStyle = (path) => {
    const baseStyle = {
      fontWeight: '500',
      transition: 'all 0.3s ease',
      paddingBottom: '2px',
    };

    if (isActive(path)) {
      return {
        ...baseStyle,
        color: '#f59e0b',
        textShadow: '0 0 10px rgba(255, 215, 0, 0.8)',
        borderBottom: '2px solid #ffd700',
      };
    }

    return {
      ...baseStyle,
      color: '#737373',
      opacity: 0.8,
      borderBottom: '2px solid transparent',
    };
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 backdrop-blur-sm" style={{
      background: 'rgba(255, 255, 255, 0.95)',
      borderBottom: '2px solid rgba(255, 215, 0, 0.3)',
      boxShadow: '0 2px 10px rgba(0, 0, 0, 0.05)',
    }} {...props}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link
            to="/"
            className="flex items-center gap-3 no-underline hover:no-underline"
          >
            <img
              src={v1logo}
              alt="Version1"
              className="h-16"
            />
            <span className="font-bold text-lg text-neutral-900 hidden sm:inline" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>
              Version1 Quiz
            </span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-8">
            {user ? (
              <>
                <Link to="/dashboard" style={getLinkStyle('/dashboard')}>
                  Dashboard
                </Link>
                <Link to="/leaderboard" style={getLinkStyle('/leaderboard')}>
                  Leaderboard
                </Link>
                <Link to="/profile" style={getLinkStyle('/profile')}>
                  Profile
                </Link>
                <Link to="/about" style={getLinkStyle('/about')}>
                  About
                </Link>
              </>
            ) : (
              <>
                <Link to="/dashboard" style={getLinkStyle('/dashboard')}>
                  Levels
                </Link>
                <Link to="/leaderboard" style={getLinkStyle('/leaderboard')}>
                  Leaderboard
                </Link>
                <Link to="/about" style={getLinkStyle('/about')}>
                  About
                </Link>
              </>
            )}
          </nav>

          {/* User Info & Actions */}
          <div className="hidden md:flex items-center gap-4">
            {user ? (
              <>
                <div className="flex items-center gap-2">
                  {user.avatar && (
                    <img
                      src={user.avatar}
                      alt={user.name}
                      className="w-8 h-8 rounded-full border-2"
                      style={{ borderColor: '#ffd700' }}
                    />
                  )}
                  <div className="text-sm">
                    <p className="font-semibold text-neutral-900">{user.username || user.name}</p>
                    <p className="text-xs text-neutral-600">@{user.username || 'user'}</p>
                  </div>
                </div>
                <Button
                  variant="ghost"
                  size="sm"
                  icon={IoLogOut}
                  onClick={handleLogout}
                  style={{ color: '#ff006e' }}
                >
                  Logout
                </Button>
              </>
            ) : (
              <button
                onClick={() => setShowLoginModal(true)}
                className="px-4 py-2 text-sm font-semibold rounded-lg transition-all text-white"
                style={{
                  background: 'linear-gradient(to right, #ffd700, #ffc107)',
                  boxShadow: '0 0 10px rgba(255, 215, 0, 0.4)',
                }}
              >
                Login
              </button>
            )}
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2 rounded-lg transition-all"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            style={{ color: '#f59e0b' }}
          >
            {mobileMenuOpen ? (
              <IoClose className="w-6 h-6" />
            ) : (
              <IoMenu className="w-6 h-6" />
            )}
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden pb-4 space-y-2" style={{ borderTop: '1px solid rgba(255, 215, 0, 0.3)' }}>
            {user ? (
              <>
                <Link
                  to="/dashboard"
                  className="block px-4 py-2 rounded-lg transition-all border-b-2"
                  onClick={() => setMobileMenuOpen(false)}
                  style={isActive('/dashboard') ? { color: '#f59e0b', borderColor: '#ffd700', backgroundColor: 'rgba(255, 215, 0, 0.1)' } : { color: '#737373', borderColor: 'transparent' }}
                >
                  Dashboard
                </Link>
                <Link
                  to="/leaderboard"
                  className="block px-4 py-2 rounded-lg transition-all border-b-2"
                  onClick={() => setMobileMenuOpen(false)}
                  style={isActive('/leaderboard') ? { color: '#f59e0b', borderColor: '#ffd700', backgroundColor: 'rgba(255, 215, 0, 0.1)' } : { color: '#737373', borderColor: 'transparent' }}
                >
                  Leaderboard
                </Link>
                <Link
                  to="/profile"
                  className="block px-4 py-2 rounded-lg transition-all border-b-2"
                  onClick={() => setMobileMenuOpen(false)}
                  style={isActive('/profile') ? { color: '#f59e0b', borderColor: '#ffd700', backgroundColor: 'rgba(255, 215, 0, 0.1)' } : { color: '#737373', borderColor: 'transparent' }}
                >
                  Profile
                </Link>
                <Link
                  to="/about"
                  className="block px-4 py-2 rounded-lg transition-all border-b-2"
                  onClick={() => setMobileMenuOpen(false)}
                  style={isActive('/about') ? { color: '#f59e0b', borderColor: '#ffd700', backgroundColor: 'rgba(255, 215, 0, 0.1)' } : { color: '#737373', borderColor: 'transparent' }}
                >
                  About
                </Link>
                <button
                  className="w-full text-left px-4 py-2 rounded-lg transition-all"
                  onClick={handleLogout}
                  style={{ color: '#ff006e' }}
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <Link
                  to="/dashboard"
                  className="block px-4 py-2 rounded-lg transition-all border-b-2"
                  onClick={() => setMobileMenuOpen(false)}
                  style={isActive('/dashboard') ? { color: '#f59e0b', borderColor: '#ffd700', backgroundColor: 'rgba(255, 215, 0, 0.1)' } : { color: '#737373', borderColor: 'transparent' }}
                >
                  Levels
                </Link>
                <Link
                  to="/leaderboard"
                  className="block px-4 py-2 rounded-lg transition-all border-b-2"
                  onClick={() => setMobileMenuOpen(false)}
                  style={isActive('/leaderboard') ? { color: '#f59e0b', borderColor: '#ffd700', backgroundColor: 'rgba(255, 215, 0, 0.1)' } : { color: '#737373', borderColor: 'transparent' }}
                >
                  Leaderboard
                </Link>
                <Link
                  to="/about"
                  className="block px-4 py-2 rounded-lg transition-all border-b-2"
                  onClick={() => setMobileMenuOpen(false)}
                  style={isActive('/about') ? { color: '#f59e0b', borderColor: '#ffd700', backgroundColor: 'rgba(255, 215, 0, 0.1)' } : { color: '#737373', borderColor: 'transparent' }}
                >
                  About
                </Link>
                <button
                  className="w-full text-left px-4 py-2 rounded-lg transition-all"
                  onClick={() => {
                    setShowLoginModal(true);
                    setMobileMenuOpen(false);
                  }}
                  style={{ color: '#737373' }}
                >
                  Login
                </button>
              </>
            )}
          </div>
        )}
      </div>

      {/* Login Modal for Guests */}
      <LoginModal
        isOpen={showLoginModal}
        onClose={() => setShowLoginModal(false)}
        onSuccess={() => {
          setShowLoginModal(false);
          setMobileMenuOpen(false);
        }}
      />
    </header>
  );
};

export default Header;
