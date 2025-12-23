import React, { useState, useEffect } from 'react';
import { useAuth } from '../context';
import { IoBarChart, IoCheckmark, IoFlash, IoMail, IoPerson, IoCamera } from 'react-icons/io5';
import { quizAPI, leaderboardAPI, authAPI } from '../services/api';
import { formatNumber } from '../utils/helpers';
import AvatarSelector from '../components/AvatarSelector';

export default function Profile() {
  const { user, isAuthenticated, updateUser } = useAuth();
  const [progress, setProgress] = useState(null);
  const [userRank, setUserRank] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showAvatarModal, setShowAvatarModal] = useState(false);
  const [selectedAvatar, setSelectedAvatar] = useState(null);
  const [savingAvatar, setSavingAvatar] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      if (!isAuthenticated) {
        setLoading(false);
        return;
      }

      try {
        setLoading(true);
        setError(null);

        const [progressData, rankData] = await Promise.all([
          quizAPI.getProgress().catch(() => null),
          leaderboardAPI.getUserRank().catch(() => null),
        ]);

        setProgress(progressData);
        setUserRank(rankData);
      } catch (error) {
        setError('Failed to load profile data. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [isAuthenticated]);

  const handleSaveAvatar = async () => {
    if (!selectedAvatar) return;

    setSavingAvatar(true);
    try {
      const response = await authAPI.updateProfile({
        avatar: selectedAvatar.data,
        avatar_type: selectedAvatar.type,
      });
      updateUser(response);
      setShowAvatarModal(false);
      setSelectedAvatar(null);
    } catch (err) {
      alert('Failed to update avatar. Please try again.');
    } finally {
      setSavingAvatar(false);
    }
  };

  if (!isAuthenticated) {
    return (
      <div className="flex items-center justify-center h-64">
        <div style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '2rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <p className="text-neutral-700">Please log in to view your profile</p>
        </div>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="w-12 h-12 border-4 border-t-primary-600 rounded-full animate-spin" style={{
          borderColor: 'rgba(255, 215, 0, 0.2)',
          borderTopColor: '#ffd700'
        }} />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-64">
        <div style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 0, 110, 0.3)',
          borderRadius: '0.75rem',
          padding: '2rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <p className="text-neutral-700">{error}</p>
          <p className="text-sm text-neutral-500 mt-2">Check console for details</p>
        </div>
      </div>
    );
  }

  const stats = {
    totalXP: progress?.total_xp || 0,
    currentLevel: progress?.current_level?.level_number || 1,
    completedLevels: progress?.completed_levels?.length || 0,
    rank: userRank?.rank || 'N/A',
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold text-neutral-900 mb-1" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif", textShadow: '0 0 20px rgba(255, 215, 0, 0.3)' }}>Profile</h1>
        <p className="text-base text-neutral-600">Your learning journey and achievements</p>
      </div>

      {/* User Info Card */}
      <div style={{
        background: '#ffffff',
        border: '2px solid rgba(255, 215, 0, 0.3)',
        borderRadius: '0.75rem',
        padding: '1.5rem',
        boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
      }}>
        <div className="flex flex-col md:flex-row items-center md:items-start gap-4">
          <div className="relative">
            {user?.avatar && (
              <img
                src={user.avatar}
                alt={user.name || 'User'}
                className="w-20 h-20 rounded-full border-2"
                style={{ borderColor: '#ffd700', boxShadow: '0 0 15px rgba(255, 215, 0, 0.3)' }}
              />
            )}
            <button
              onClick={() => setShowAvatarModal(true)}
              className="absolute bottom-0 right-0 p-2 rounded-full transition-all"
              style={{
                background: 'linear-gradient(to right, #ffd700, #ffc107)',
                boxShadow: '0 0 10px rgba(255, 215, 0, 0.4)',
              }}
            >
              <IoCamera className="w-4 h-4 text-white" />
            </button>
          </div>
          <div className="flex-1 text-center md:text-left">
            <h2 className="text-2xl font-bold text-neutral-900 mb-1">{user?.name || user?.username || 'User'}</h2>
            {user?.username && (
              <p className="text-sm font-medium text-yellow-700 mb-2">@{user.username}</p>
            )}
            <div className="flex flex-col md:flex-row gap-3 items-center md:items-start text-sm">
              <div className="flex items-center gap-2">
                <IoMail className="w-4 h-4 text-neutral-500" />
                <span className="text-neutral-600">{user?.email}</span>
              </div>
              <div className="flex items-center gap-2">
                <IoPerson className="w-4 h-4 text-neutral-500" />
                <span className="text-neutral-600">Member since {new Date().toLocaleDateString()}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Main Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div style={{
          background: 'rgba(255, 215, 0, 0.1)',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '1rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <IoFlash className="w-8 h-8 mx-auto mb-2 text-yellow-600" style={{ filter: 'drop-shadow(0 0 3px rgba(255, 215, 0, 0.6))' }} />
          <p className="text-2xl font-bold text-neutral-900">{formatNumber(stats.totalXP)}</p>
          <p className="text-xs text-neutral-600 mt-1">Total XP</p>
        </div>

        <div style={{
          background: 'rgba(255, 193, 7, 0.1)',
          border: '2px solid rgba(255, 193, 7, 0.3)',
          borderRadius: '0.75rem',
          padding: '1rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <IoCheckmark className="w-8 h-8 mx-auto mb-2 text-yellow-700" style={{ filter: 'drop-shadow(0 0 3px rgba(255, 193, 7, 0.6))' }} />
          <p className="text-2xl font-bold text-neutral-900">{stats.completedLevels}</p>
          <p className="text-xs text-neutral-600 mt-1">Levels Complete</p>
        </div>

        <div style={{
          background: 'rgba(255, 152, 0, 0.1)',
          border: '2px solid rgba(255, 152, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '1rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <IoBarChart className="w-8 h-8 mx-auto mb-2" style={{ color: '#ff9800', filter: 'drop-shadow(0 0 3px rgba(255, 152, 0, 0.6))' }} />
          <p className="text-2xl font-bold text-neutral-900">#{stats.rank}</p>
          <p className="text-xs text-neutral-600 mt-1">Global Rank</p>
        </div>
      </div>

      {/* Completed Levels */}
      {progress?.completed_levels && progress.completed_levels.length > 0 && (
        <div style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '1.5rem',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <h3 className="font-bold text-neutral-900 mb-4 text-lg">Completed Levels</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {progress.completed_levels.map((level) => (
              <div
                key={level.id}
                className="flex items-center gap-3 p-3 rounded-lg"
                style={{
                  background: 'rgba(0, 255, 136, 0.1)',
                  border: '1px solid rgba(0, 255, 136, 0.2)',
                }}
              >
                <IoCheckmark className="w-5 h-5 text-success-600 flex-shrink-0" />
                <div className="flex-1 min-w-0">
                  <p className="font-medium text-neutral-900 text-sm truncate">{level.title}</p>
                  <p className="text-xs text-neutral-600">+{level.xp_reward} XP</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Empty State */}
      {!progress?.completed_levels || progress.completed_levels.length === 0 && (
        <div style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '3rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <p className="text-lg text-neutral-700 mb-2">No levels completed yet</p>
          <p className="text-sm text-neutral-600">Start your journey by completing your first quiz!</p>
        </div>
      )}

      {/* Avatar Edit Modal */}
      {showAvatarModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-70 p-4" onClick={() => setShowAvatarModal(false)}>
          <div
            className="w-full max-w-2xl p-6 rounded-lg"
            onClick={(e) => e.stopPropagation()}
            style={{
              background: '#ffffff',
              border: '2px solid rgba(255, 215, 0, 0.3)',
              boxShadow: '0 0 30px rgba(255, 215, 0, 0.3)',
              maxHeight: '90vh',
              overflowY: 'auto',
            }}
          >
            <h2 className="text-2xl font-bold text-neutral-900 mb-4" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>
              Change Avatar
            </h2>

            <AvatarSelector
              selectedAvatar={selectedAvatar}
              onAvatarChange={setSelectedAvatar}
            />

            <div className="flex gap-3 mt-6">
              <button
                onClick={handleSaveAvatar}
                disabled={!selectedAvatar || savingAvatar}
                className="flex-1 py-3 rounded-lg font-semibold text-white transition-all"
                style={{
                  background: !selectedAvatar || savingAvatar ? 'rgba(100, 100, 100, 0.5)' : 'linear-gradient(to right, #ffd700, #ffc107)',
                  boxShadow: !selectedAvatar || savingAvatar ? 'none' : '0 0 20px rgba(255, 215, 0, 0.6)',
                  cursor: !selectedAvatar || savingAvatar ? 'not-allowed' : 'pointer',
                  opacity: !selectedAvatar || savingAvatar ? 0.5 : 1,
                }}
              >
                {savingAvatar ? 'Saving...' : 'Save Avatar'}
              </button>
              <button
                onClick={() => {
                  setShowAvatarModal(false);
                  setSelectedAvatar(null);
                }}
                className="flex-1 py-3 rounded-lg font-semibold transition-all"
                style={{
                  background: 'rgba(255, 215, 0, 0.1)',
                  color: '#737373',
                  border: '2px solid rgba(255, 215, 0, 0.3)',
                }}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
