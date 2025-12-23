import React, { useState } from 'react';
import { useAuth } from '../context';
import { Button } from './common';
import { IoArrowForward } from 'react-icons/io5';

export const LoginModal = ({ isOpen = false, onClose }) => {
  const { login } = useAuth();
  const [loading, setLoading] = useState(false);
  const [email, setEmail] = useState('');

  if (!isOpen) return null;

  const handleGoogleLogin = async () => {
    setLoading(true);
    try {
      setTimeout(() => {
        login({
          name: 'User',
          email: email || 'user@example.com',
          picture: null,
        });
        setLoading(false);
        onClose?.();
      }, 1000);
    } catch (error) {
      console.error('Login failed:', error);
      setLoading(false);
    }
  };

  const handleDemoLogin = () => {
    login({
      name: 'Demo User',
      email: 'demo@example.com',
      picture: null,
    });
    onClose?.();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center" style={{ backgroundColor: 'rgba(0, 0, 0, 0.7)' }}>
      {/* Modal backdrop with glass blur */}
      <div className="absolute inset-0" style={{ backdropFilter: 'blur(4px)' }} onClick={onClose} />

      {/* Modal Card */}
      <div className="relative w-full max-w-md mx-4 p-8 rounded-xl animate-slideIn" style={{
        background: 'rgba(6, 8, 24, 0.95)',
        border: '2px solid rgba(0, 240, 255, 0.3)',
        boxShadow: 'inset 0 0 10px rgba(0, 240, 255, 0.2), 0 0 20px rgba(0, 240, 255, 0.3)',
      }}>
        {/* Header */}
        <div className="space-y-2 border-b pb-4" style={{ borderColor: 'rgba(0, 240, 255, 0.3)' }}>
          <h2 className="font-bold tracking-widest" style={{
            fontSize: '1.5rem',
            color: '#00f0ff',
            fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif",
            textShadow: '0 0 10px rgba(0, 240, 255, 0.8), 0 0 20px rgba(0, 240, 255, 0.4)',
          }}>
            ACCESS REQUIRED
          </h2>
          <p className="text-sm tracking-widest" style={{ color: '#a0b0c0' }}>
            AUTHENTICATE TO CONTINUE
          </p>
        </div>

        {/* Email Input */}
        <div className="space-y-3 mt-6">
          <label className="block text-xs font-bold tracking-widest" style={{
            color: '#00f0ff',
            fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif",
          }}>
            EMAIL ADDRESS
          </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="user@example.com"
            className="w-full px-4 py-3 border-2 rounded-lg focus:outline-none transition-all text-neutral-100 placeholder-neutral-600"
            style={{
              borderColor: 'rgba(0, 240, 255, 0.3)',
              backgroundColor: '#0f1419',
            }}
            onFocus={(e) => {
              e.target.style.borderColor = '#00f0ff';
              e.target.style.borderOpacity = '1';
              e.target.style.boxShadow = '0 0 10px rgba(0, 240, 255, 0.5)';
            }}
            onBlur={(e) => {
              e.target.style.borderColor = 'rgba(0, 240, 255, 0.3)';
              e.target.style.boxShadow = 'none';
            }}
          />
        </div>

        {/* Google Login Button */}
        <div className="mt-6">
          <Button
            variant="primary"
            size="lg"
            onClick={handleGoogleLogin}
            loading={loading}
            className="w-full font-bold tracking-wide"
            style={{
              background: 'linear-gradient(to right, #00f0ff, #0084ff)',
              color: '#0a0e27',
              boxShadow: '0 0 10px rgba(0, 240, 255, 0.5)',
            }}
          >
            {loading ? 'CONNECTING...' : 'SIGN IN WITH GOOGLE'}
          </Button>
        </div>

        {/* Divider */}
        <div className="relative py-4">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t" style={{ borderColor: 'rgba(0, 240, 255, 0.2)' }} />
          </div>
          <div className="relative flex justify-center">
            <span className="px-4 text-xs tracking-widest" style={{
              color: '#00f0ff',
              backgroundColor: 'rgba(6, 8, 24, 0.95)',
              fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif",
            }}>
              OR
            </span>
          </div>
        </div>

        {/* Demo Login Button */}
        <div className="mt-6">
          <Button
            variant="secondary"
            size="lg"
            icon={IoArrowForward}
            onClick={handleDemoLogin}
            className="w-full border-2 font-bold tracking-wide"
            style={{
              borderColor: '#b429f9',
              color: '#b429f9',
              backgroundColor: 'transparent',
              boxShadow: '0 0 10px rgba(180, 41, 249, 0.5), 0 0 20px rgba(180, 41, 249, 0.3)',
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.backgroundColor = 'rgba(180, 41, 249, 0.1)';
              e.currentTarget.style.boxShadow = '0 0 20px rgba(180, 41, 249, 0.8), 0 0 40px rgba(180, 41, 249, 0.4)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.backgroundColor = 'transparent';
              e.currentTarget.style.boxShadow = '0 0 10px rgba(180, 41, 249, 0.5), 0 0 20px rgba(180, 41, 249, 0.3)';
            }}
          >
            TRY DEMO MODE
          </Button>
        </div>

        {/* Terms */}
        <p className="text-xs text-center font-mono tracking-wide mt-6" style={{ color: '#5a6375' }}>
          By signing in, you agree to Terms &amp; Privacy Policy
        </p>
      </div>
    </div>
  );
};

export default LoginModal;
