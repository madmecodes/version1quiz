import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context';
import { Button, Badge, ProgressBar } from '../components';
import { IoPlay, IoCheckmark, IoFlash, IoLockClosed } from 'react-icons/io5';
import { quizAPI, leaderboardAPI } from '../services/api';
import { getDifficultyColor } from '../utils/helpers';
import LoginModal from './Login';

export default function Dashboard() {
  const navigate = useNavigate();
  const { user, isAuthenticated, isLoading: authLoading } = useAuth();
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [levels, setLevels] = useState([]);
  const [progress, setProgress] = useState(null);
  const [userRank, setUserRank] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showLoginModal, setShowLoginModal] = useState(false);
  const [pendingLevelId, setPendingLevelId] = useState(null);

  useEffect(() => {
    if (authLoading) return;

    const fetchData = async () => {
      try {
        setLoading(true);
        const levelsData = await quizAPI.getLevels();
        setLevels(Array.isArray(levelsData) ? levelsData : (levelsData.results || []));

        if (isAuthenticated) {
          const [progressData, rankData] = await Promise.all([
            quizAPI.getProgress().catch(err => { console.error('Error fetching progress:', err); return null; }),
            leaderboardAPI.getUserRank().catch(err => { console.error('Error fetching rank:', err); return null; })
          ]);
          setProgress(progressData);
          setUserRank(rankData);
        }
      } catch (error) {
        console.error('Error fetching levels:', error);
        setError('Backend not running. Start it with: cd backend && docker-compose up -d');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [isAuthenticated, authLoading]);

  if (loading || authLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-64">
        <div style={{
          background: 'rgba(255, 0, 110, 0.1)',
          border: '2px solid rgba(255, 0, 110, 0.3)',
          borderRadius: '0.75rem',
          padding: '2rem',
          boxShadow: 'inset 0 0 10px rgba(255, 0, 110, 0.1)',
        }}>
          <p className="text-center text-neutral-300 mb-4">{error}</p>
          <p className="text-center text-sm text-neutral-400">Run: cd backend && docker-compose up -d</p>
        </div>
      </div>
    );
  }

  const categories = ['All', ...new Set(levels.map((l) => l.category))];
  const filteredLevels = selectedCategory === 'All'
    ? levels
    : levels.filter((l) => l.category === selectedCategory);

  const handleStartQuiz = (levelId) => {
    if (!isAuthenticated) {
      setPendingLevelId(levelId);
      setShowLoginModal(true);
    } else {
      navigate(`/quiz/${levelId}`);
    }
  };

  const handleLoginSuccess = () => {
    if (pendingLevelId) {
      navigate(`/quiz/${pendingLevelId}`);
      setPendingLevelId(null);
    }
  };

  const getLevelCard = (level) => {
    const levelProgress = progress?.level_progress?.[level.level_number];
    const currentLevelNumber = progress?.current_level?.level_number || 1;
    const isLocked = level.level_number > currentLevelNumber;
    const isCompleted = levelProgress?.passed;
    const isAttempted = levelProgress && !isCompleted;

    return (
      <div
        key={level.id}
        onClick={() => !isLocked && handleStartQuiz(level.id)}
        className={`cursor-pointer relative overflow-hidden rounded-lg p-4 transition-all ${isLocked ? '' : 'hover:shadow-lg'}`}
        style={{
          background: isCompleted
            ? 'rgba(255, 215, 0, 0.35)'
            : '#ffffff',
          border: `2px solid ${isCompleted ? 'rgba(255, 193, 7, 0.6)' : 'rgba(255, 215, 0, 0.3)'}`,
          boxShadow: isCompleted ? '0 2px 12px rgba(255, 215, 0, 0.2)' : '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}
      >
        {/* Lock overlay */}
        {isLocked && (
          <div className="absolute inset-0 bg-white bg-opacity-60 flex items-center justify-center z-10 rounded-lg">
            <IoLockClosed className="w-12 h-12" style={{ color: '#a3a3a3', opacity: 0.7 }} />
          </div>
        )}

        {/* Level number badge */}
        <div className="absolute top-3 right-3 w-8 h-8 bg-gradient-to-br from-yellow-400 via-yellow-500 to-yellow-600 rounded-lg flex items-center justify-center text-white font-bold text-sm" style={{ boxShadow: '0 0 6px rgba(255, 215, 0, 0.5)' }}>
          {level.level_number}
        </div>

        {/* Content */}
        <div className="space-y-3">
          {/* Header */}
          <div>
            <h3 className="text-base font-bold text-neutral-900 mb-1" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>{level.title}</h3>
            <p className="text-xs text-neutral-600">{level.description}</p>
          </div>

          {/* Badges */}
          <div className="flex gap-2 flex-wrap">
            <Badge variant={getDifficultyColor(level.difficulty)} size="sm">
              {level.difficulty}
            </Badge>
            <Badge variant="secondary" size="sm">
              {level.category}
            </Badge>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 gap-2 py-2 text-xs" style={{ borderTop: '1px solid rgba(255, 215, 0, 0.3)', borderBottom: '1px solid rgba(255, 215, 0, 0.3)' }}>
            <div className="flex items-center gap-1">
              <IoFlash className="w-4 h-4 text-yellow-600" style={{ filter: 'drop-shadow(0 0 2px rgba(255, 215, 0, 0.5))' }} />
              <span className="font-semibold text-neutral-700">
                +{level.xp_reward} XP
              </span>
            </div>
            <div className="text-right">
              <span className="font-semibold text-neutral-700">
                {level.passing_percentage}% pass
              </span>
            </div>
          </div>

          {/* Progress */}
          {levelProgress && (
            <div className="space-y-1">
              <div className="flex justify-between items-center text-xs">
                <span className="text-neutral-600">Score</span>
                <span className="font-semibold text-yellow-700">
                  {levelProgress.highest_score}/{levelProgress.total_questions || 10}
                </span>
              </div>
              <ProgressBar
                current={levelProgress.highest_score}
                total={levelProgress.total_questions || 10}
                variant={isCompleted ? 'warning' : 'primary'}
                size="sm"
                showLabel={false}
              />
            </div>
          )}

          {/* Action Button */}
          <div>
            {isCompleted ? (
              <Button
                variant="secondary"
                size="sm"
                icon={IoCheckmark}
                className="w-full text-xs"
                disabled
              >
                Completed
              </Button>
            ) : isLocked ? (
              <Button
                variant="secondary"
                size="sm"
                className="w-full text-xs"
                disabled
              >
                Locked
              </Button>
            ) : (
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  handleStartQuiz(level.id);
                }}
                className="w-full text-xs px-3 py-1.5 rounded-lg font-semibold text-white transition-all flex items-center justify-center gap-2"
                style={{
                  background: isAttempted ? '#e5e5e5' : 'linear-gradient(to right, #ffd700, #ffc107)',
                  color: isAttempted ? '#737373' : '#ffffff',
                  boxShadow: isAttempted ? 'none' : '0 0 10px rgba(255, 215, 0, 0.4)',
                }}
              >
                <IoPlay className="w-4 h-4" />
                {isAttempted ? 'Retry' : 'Start'}
              </button>
            )}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="space-y-4">
      {/* Category Filter */}
      <div className="flex gap-1 overflow-x-auto pb-2">
        {categories.map((category) => (
          <button
            key={category}
            onClick={() => setSelectedCategory(category)}
            className="px-3 py-1 rounded-lg text-sm font-medium whitespace-nowrap transition-all"
            style={
              selectedCategory === category
                ? {
                    background: 'linear-gradient(to right, #ffd700, #ffc107)',
                    color: '#000000',
                    boxShadow: '0 0 10px rgba(255, 215, 0, 0.6)',
                  }
                : {
                    background: 'rgba(255, 215, 0, 0.1)',
                    color: '#737373',
                    border: '1px solid rgba(255, 215, 0, 0.3)',
                  }
            }
          >
            {category}
          </button>
        ))}
      </div>

      {/* Levels Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredLevels.map((level) => getLevelCard(level))}
      </div>

      {/* Empty State */}
      {filteredLevels.length === 0 && (
        <div style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '3rem',
          textAlign: 'center',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <p className="text-lg text-neutral-700">No levels found in this category</p>
        </div>
      )}

      {/* Login Modal */}
      <LoginModal
        isOpen={showLoginModal}
        onClose={() => setShowLoginModal(false)}
        onSuccess={handleLoginSuccess}
      />
    </div>
  );
}
