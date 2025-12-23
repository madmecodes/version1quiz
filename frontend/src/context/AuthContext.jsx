import React, { createContext, useContext, useState, useEffect } from 'react';
import { authAPI } from '../services/api';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const initAuth = async () => {
      const token = localStorage.getItem('authToken');
      const storedUser = localStorage.getItem('user');

      if (token && storedUser) {
        try {
          const userData = JSON.parse(storedUser);
          setUser(userData);
          setIsAuthenticated(true);

          // Try to refresh profile, but don't fail if backend is down
          try {
            const profile = await authAPI.getProfile();
            setUser(profile);
            localStorage.setItem('user', JSON.stringify(profile));
          } catch (profileError) {
            console.warn('Could not refresh profile from backend, using cached data:', profileError.message);
            // Keep using cached user data instead of logging out
          }
        } catch (error) {
          console.error('Failed to parse stored user:', error);
          localStorage.removeItem('authToken');
          localStorage.removeItem('user');
          setUser(null);
          setIsAuthenticated(false);
        }
      }
      setIsLoading(false);
    };

    initAuth();
  }, []);

  const loginWithGoogle = async (credentialResponse) => {
    try {
      setIsLoading(true);

      console.log('='.repeat(50));
      console.log('GOOGLE OAUTH DEBUG - Frontend');
      console.log('credentialResponse:', credentialResponse);
      console.log('credential (first 50 chars):', credentialResponse.credential?.substring(0, 50) + '...');
      console.log('credential length:', credentialResponse.credential?.length);

      const response = await authAPI.googleLogin(credentialResponse.credential);

      console.log('Backend response received:', response);
      console.log('='.repeat(50));

      localStorage.setItem('authToken', response.token);
      localStorage.setItem('user', JSON.stringify(response.user));

      setUser(response.user);
      setIsAuthenticated(true);

      return response;
    } catch (error) {
      console.error('='.repeat(50));
      console.error('Login failed ERROR:');
      console.error('Error message:', error.message);
      console.error('Error response:', error.response?.data);
      console.error('Error status:', error.response?.status);
      console.error('Full error:', error);
      console.error('='.repeat(50));
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const updateUser = (updatedUser) => {
    setUser(updatedUser);
    localStorage.setItem('user', JSON.stringify(updatedUser));
  };

  const logout = async () => {
    try {
      await authAPI.logout();
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      setUser(null);
      setIsAuthenticated(false);
      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
    }
  };

  const value = {
    user,
    isAuthenticated,
    isLoading,
    loginWithGoogle,
    updateUser,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export default AuthContext;
