import React, { useState, useEffect } from 'react';
import { useAuth } from '../context';
import { Button, Badge } from '../components';
import { RankingRow } from '../components/leaderboard';
import { IoSwapVertical } from 'react-icons/io5';
import { leaderboardAPI } from '../services/api';

export default function Leaderboard() {
  const { user, isAuthenticated } = useAuth();
  const [leaderboard, setLeaderboard] = useState([]);
  const [userRank, setUserRank] = useState(null);
  const [loading, setLoading] = useState(true);
  const [sortBy, setSortBy] = useState('xp'); // 'xp' or 'level'
  const [filterRange, setFilterRange] = useState('top10'); // 'top10', 'all'

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        setLoading(true);
        const leaderboardData = await leaderboardAPI.getLeaderboard();
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : (leaderboardData.results || []));

        if (isAuthenticated) {
          const rankData = await leaderboardAPI.getUserRank().catch(() => null);
          setUserRank(rankData);
        }
      } catch (error) {
        // Silently handle errors
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, [isAuthenticated]);

  const getFilteredLeaderboard = () => {
    let filtered = [...leaderboard];

    // Apply range filter
    if (filterRange === 'top10') {
      filtered = filtered.slice(0, 10);
    }

    // Apply sorting
    if (sortBy === 'level') {
      filtered.sort((a, b) => b.current_level_number - a.current_level_number || b.total_xp - a.total_xp);
    }

    return filtered;
  };

  const filteredLeaderboard = getFilteredLeaderboard();

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin" />
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-bold text-neutral-900 mb-1" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif", textShadow: '0 0 20px rgba(255, 215, 0, 0.3)' }}>Leaderboard</h1>
        <p className="text-sm text-neutral-600">
          Compete with other indie hackers and see how you rank
        </p>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        {/* Your Rank */}
        {isAuthenticated && (
          <div style={{
            background: 'rgba(255, 215, 0, 0.15)',
            border: '2px solid rgba(255, 215, 0, 0.4)',
            borderRadius: '0.75rem',
            padding: '0.75rem',
            boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
          }}>
            <div className="space-y-1">
              <p className="text-xs text-yellow-700 font-medium">Your Rank</p>
              <p className="text-2xl font-bold text-neutral-900">
                #{userRank?.rank || 'N/A'}
              </p>
              <p className="text-xs text-neutral-600">
                {userRank ? `${userRank.total_xp} XP · Level ${userRank.current_level}` : 'Start learning to get ranked'}
              </p>
            </div>
          </div>
        )}

        {/* Total Users */}
        <div style={{
          background: 'rgba(255, 193, 7, 0.15)',
          border: '2px solid rgba(255, 193, 7, 0.4)',
          borderRadius: '0.75rem',
          padding: '0.75rem',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <div className="space-y-1">
            <p className="text-xs text-yellow-700 font-medium">Total Users</p>
            <p className="text-2xl font-bold text-neutral-900">{leaderboard.length}</p>
            <p className="text-xs text-neutral-600">Actively learning</p>
          </div>
        </div>

        {/* Top Score */}
        <div style={{
          background: 'rgba(0, 255, 136, 0.15)',
          border: '2px solid rgba(0, 255, 136, 0.4)',
          borderRadius: '0.75rem',
          padding: '0.75rem',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <div className="space-y-1">
            <p className="text-xs text-success-700 font-medium">Top Score</p>
            <p className="text-2xl font-bold text-success-600">{leaderboard[0]?.total_xp || 0} XP</p>
            <p className="text-xs text-neutral-600">{leaderboard[0]?.username || 'madme'}</p>
          </div>
        </div>
      </div>

      {/* Controls */}
      <div className="flex flex-col md:flex-row gap-3 items-center">
        <div className="flex gap-2 flex-wrap">
          <Badge
            variant={sortBy === 'xp' ? 'primary' : 'secondary'}
            className="cursor-pointer hover:opacity-80"
            onClick={() => setSortBy('xp')}
            icon={IoSwapVertical}
          >
            Sort by XP
          </Badge>
          <Badge
            variant={sortBy === 'level' ? 'primary' : 'secondary'}
            className="cursor-pointer hover:opacity-80"
            onClick={() => setSortBy('level')}
            icon={IoSwapVertical}
          >
            Sort by Level
          </Badge>
        </div>

        <div className="flex gap-2">
          <button
            onClick={() => setFilterRange('top10')}
            className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
            style={{
              background: filterRange === 'top10' ? 'linear-gradient(to right, #ffd700, #ffc107)' : '#e5e5e5',
              color: filterRange === 'top10' ? '#ffffff' : '#737373',
              boxShadow: filterRange === 'top10' ? '0 0 10px rgba(255, 215, 0, 0.4)' : 'none',
            }}
          >
            Top 10
          </button>
          <button
            onClick={() => setFilterRange('all')}
            className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
            style={{
              background: filterRange === 'all' ? 'linear-gradient(to right, #ffd700, #ffc107)' : '#e5e5e5',
              color: filterRange === 'all' ? '#ffffff' : '#737373',
              boxShadow: filterRange === 'all' ? '0 0 10px rgba(255, 215, 0, 0.4)' : 'none',
            }}
          >
            All
          </button>
        </div>
      </div>

      {/* Leaderboard List - Scrollable Container */}
      <div
        className="space-y-2 overflow-y-auto"
        style={{
          maxHeight: '500px',
          paddingRight: '0.5rem',
        }}
      >
        {filteredLeaderboard.map((entry, index) => (
          <RankingRow
            key={entry.user_id || index}
            rank={entry.rank}
            user={{
              id: entry.user_id,
              name: entry.username,
              email: entry.user_email,
              avatar: entry.user_avatar,
            }}
            xp={entry.total_xp}
            level={entry.current_level_number}
            isCurrentUser={isAuthenticated && entry.user_email === user?.email}
          />
        ))}
      </div>

      {/* Current User Position */}
      {isAuthenticated && userRank && !filteredLeaderboard.some((u) => u.user_email === user?.email) && (
        <div style={{
          background: 'rgba(255, 215, 0, 0.1)',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '0.75rem',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <p className="text-center text-yellow-700 font-medium text-sm">
            ↓ You are ranked #{userRank.rank} with {userRank.total_xp} XP ↓
          </p>
        </div>
      )}

      {/* Empty State */}
      {filteredLeaderboard.length === 0 && (
        <div style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '2rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <p className="text-base text-neutral-700">No users found</p>
        </div>
      )}
    </div>
  );
}
