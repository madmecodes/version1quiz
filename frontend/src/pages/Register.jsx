import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context';
import { authAPI } from '../services/api';
import AvatarSelector from '../components/AvatarSelector';

export default function Register() {
  const navigate = useNavigate();
  const { user, isAuthenticated, updateUser } = useAuth();
  const [username, setUsername] = useState('');
  const [selectedAvatar, setSelectedAvatar] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Redirect if not authenticated
    if (!isAuthenticated) {
      navigate('/dashboard');
      return;
    }

    // Redirect if already has username
    if (user?.username) {
      navigate('/dashboard');
    }
  }, [isAuthenticated, user, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!username || username.length < 3) {
      setError('Username must be at least 3 characters');
      return;
    }

    if (!/^[a-zA-Z0-9_]+$/.test(username)) {
      setError('Username can only contain letters, numbers, and underscores');
      return;
    }

    if (!selectedAvatar) {
      setError('Please select an avatar');
      return;
    }

    setLoading(true);

    try {
      await authAPI.checkUsername(username);
      const response = await authAPI.setUsername(username, selectedAvatar);
      updateUser(response.user);
      navigate('/dashboard');
    } catch (err) {
      setError(
        err.response?.data?.error ||
        err.response?.data?.username?.[0] ||
        'Username is already taken. Please choose another.'
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      {/* Registration Form */}
      <div className="w-full max-w-md">
        <div
          className="p-8 rounded-lg"
          style={{
            background: '#ffffff',
            border: '2px solid rgba(255, 215, 0, 0.3)',
            boxShadow: '0 0 30px rgba(255, 215, 0, 0.3), 0 2px 8px rgba(0, 0, 0, 0.1)',
          }}
        >
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold mb-2" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif", color: '#f59e0b', textShadow: '0 0 20px rgba(255, 215, 0, 0.6)' }}>
              Complete Registration
            </h1>
            <p className="text-sm text-neutral-600">
              Choose a unique username to get started
            </p>
          </div>

          {/* User Info */}
          {user && (
            <div className="flex items-center gap-3 mb-6 p-3 rounded-lg" style={{ background: 'rgba(255, 215, 0, 0.05)', border: '1px solid rgba(255, 215, 0, 0.2)' }}>
              {user.avatar && (
                <img
                  src={user.avatar}
                  alt={user.name}
                  className="w-12 h-12 rounded-full border-2"
                  style={{ borderColor: '#ffd700' }}
                />
              )}
              <div className="flex-1">
                <p className="font-semibold text-neutral-900 text-sm">{user.name}</p>
                <p className="text-xs text-neutral-600">{user.email}</p>
              </div>
            </div>
          )}

          {/* Form */}
          <form onSubmit={handleSubmit}>
            <div className="mb-6">
              <label htmlFor="username" className="block text-sm font-medium text-neutral-700 mb-2">
                Username *
              </label>
              <input
                type="text"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value.toLowerCase().trim())}
                className="w-full px-4 py-3 rounded-lg text-neutral-900 focus:outline-none focus:ring-2 transition-all"
                style={{
                  background: '#ffffff',
                  border: '1px solid rgba(255, 215, 0, 0.3)',
                  boxShadow: error ? '0 0 10px rgba(255, 0, 110, 0.3)' : 'none',
                }}
                placeholder="Enter your username"
                required
                minLength={3}
                maxLength={30}
                pattern="[a-zA-Z0-9_]+"
                disabled={loading}
                autoFocus
              />
              <p className="mt-2 text-xs text-neutral-600">
                3-30 characters. Letters, numbers, and underscores only.
              </p>
            </div>

            {/* Avatar Selection */}
            <div className="mb-6">
              <AvatarSelector
                selectedAvatar={selectedAvatar}
                onAvatarChange={setSelectedAvatar}
              />
            </div>

            {error && (
              <p className="mb-4 text-sm" style={{ color: '#ff006e' }}>
                {error}
              </p>
            )}

            <button
              type="submit"
              disabled={loading || !username || !selectedAvatar}
              className="w-full py-3 rounded-lg font-semibold text-white transition-all"
              style={{
                background: loading || !username || !selectedAvatar ? 'rgba(100, 100, 100, 0.5)' : 'linear-gradient(to right, #ffd700, #ffc107)',
                boxShadow: loading || !username || !selectedAvatar ? 'none' : '0 0 20px rgba(255, 215, 0, 0.6)',
                cursor: loading || !username || !selectedAvatar ? 'not-allowed' : 'pointer',
                opacity: loading || !username || !selectedAvatar ? 0.5 : 1,
              }}
            >
              {loading ? 'Creating Account...' : 'Continue to Dashboard'}
            </button>
          </form>

          {/* Note */}
          <p className="mt-6 text-xs text-neutral-600 text-center">
            This username will be displayed on the leaderboard
          </p>
        </div>
      </div>
    </div>
  );
}
