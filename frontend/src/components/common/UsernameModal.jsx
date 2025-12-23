import React, { useState } from 'react';
import { authAPI } from '../../services/api';

export default function UsernameModal({ isOpen, onClose, onSuccess }) {
  const [username, setUsername] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!username || username.length < 3) {
      setError('Username must be at least 3 characters');
      return;
    }

    setLoading(true);

    try {
      await authAPI.checkUsername(username);
      const response = await authAPI.setUsername(username);
      onSuccess(response.user);
      onClose();
    } catch (err) {
      setError(err.response?.data?.error || err.response?.data?.username?.[0] || 'Username is already taken');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-70">
      <div
        className="w-full max-w-md p-6 mx-4 rounded-lg"
        style={{
          background: 'rgba(6, 8, 24, 0.95)',
          border: '2px solid rgba(0, 240, 255, 0.3)',
          boxShadow: '0 0 20px rgba(0, 240, 255, 0.2), inset 0 0 20px rgba(0, 240, 255, 0.1)',
        }}
      >
        <h2 className="text-2xl font-bold mb-2 text-neutral-100" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif", color: '#00f0ff', textShadow: '0 0 10px rgba(0, 240, 255, 0.6)' }}>
          Choose Your Username
        </h2>
        <p className="text-sm text-neutral-400 mb-6">
          Pick a unique username for your profile
        </p>

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="username" className="block text-sm font-medium text-neutral-300 mb-2">
              Username
            </label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-2 rounded-lg text-neutral-100 focus:outline-none"
              style={{
                background: 'rgba(0, 0, 0, 0.5)',
                border: '1px solid rgba(0, 240, 255, 0.3)',
              }}
              placeholder="Enter username"
              required
              minLength={3}
              maxLength={150}
              disabled={loading}
            />
            {error && (
              <p className="mt-2 text-sm" style={{ color: '#ff006e' }}>
                {error}
              </p>
            )}
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 rounded-lg font-semibold text-neutral-900 transition-all"
            style={{
              background: loading ? 'rgba(100, 100, 100, 0.5)' : 'linear-gradient(to right, #00f0ff, #0084ff)',
              boxShadow: loading ? 'none' : '0 0 15px rgba(0, 240, 255, 0.6)',
              cursor: loading ? 'not-allowed' : 'pointer',
            }}
          >
            {loading ? 'Setting Username...' : 'Continue'}
          </button>
        </form>
      </div>
    </div>
  );
}
