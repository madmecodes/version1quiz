import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { GoogleLogin } from '@react-oauth/google';
import { useAuth } from '../context';

export default function LoginModal({ isOpen, onClose, onSuccess }) {
  const navigate = useNavigate();
  const { loginWithGoogle } = useAuth();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  if (!isOpen) return null;

  const handleGoogleSuccess = async (credentialResponse) => {
    setLoading(true);
    setError('');
    try {
      const response = await loginWithGoogle(credentialResponse);

      // Close the login modal
      onClose();

      // Redirect based on username requirement
      if (response.username_required) {
        // New user needs to complete registration
        navigate('/register');
      } else {
        // Existing user, proceed normally
        if (onSuccess) onSuccess();
      }
    } catch (err) {
      console.error('Login failed:', err);
      setError('Login failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleError = () => {
    setError('Google login failed. Please try again.');
  };

  return (
    <>
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-70" style={{ minHeight: '100vh' }} onClick={onClose}>
        <div
          className="w-full max-w-md p-8 mx-4 rounded-lg"
          onClick={(e) => e.stopPropagation()}
          style={{
            background: '#ffffff',
            border: '2px solid rgba(255, 215, 0, 0.3)',
            boxShadow: '0 0 30px rgba(255, 215, 0, 0.3), 0 2px 8px rgba(0, 0, 0, 0.1)',
          }}
        >
          <div className="space-y-6">
            <div className="space-y-2 border-b border-yellow-400 border-opacity-30 pb-4">
              <h2 className="text-3xl font-bold text-neutral-900" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif", color: '#f59e0b', textShadow: '0 0 10px rgba(255, 215, 0, 0.6)' }}>
                LOGIN REQUIRED
              </h2>
              <p className="text-neutral-600 text-sm">
                Sign in to start this quiz
              </p>
            </div>

            {/* Error Message */}
            {error && (
              <div className="p-3 rounded-lg" style={{ backgroundColor: 'rgba(255, 0, 110, 0.1)', border: '1px solid rgba(255, 0, 110, 0.3)' }}>
                <p className="text-sm" style={{ color: '#ff006e' }}>{error}</p>
              </div>
            )}

            {/* Google Login Button */}
            <div className="flex justify-center">
              <GoogleLogin
                onSuccess={handleGoogleSuccess}
                onError={handleGoogleError}
                size="large"
                text="signin_with"
                shape="rectangular"
                theme="filled_black"
                width="100%"
              />
            </div>

            {/* Terms */}
            <p className="text-xs text-neutral-600 text-center">
              By signing in, you agree to Terms &amp; Privacy Policy
            </p>
          </div>
        </div>
      </div>
    </>
  );
}
