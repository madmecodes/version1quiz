import React from 'react';
import { Badge } from '../common';
import { IoTrophy, IoStar } from 'react-icons/io5';

export const RankingRow = ({
  rank,
  user,
  xp,
  level,
  isCurrentUser = false,
  ...props
}) => {
  const getMedalColor = (rank) => {
    switch (rank) {
      case 1:
        return '#ffd700';
      case 2:
        return '#c0c0c0';
      case 3:
        return '#cd7f32';
      default:
        return '#ff9800';
    }
  };

  const getRankBadgeVariant = (rank) => {
    switch (rank) {
      case 1:
        return 'warning';
      case 2:
        return 'secondary';
      case 3:
        return 'danger';
      default:
        return 'primary';
    }
  };

  return (
    <div
      className="flex items-center gap-4 p-4 rounded-lg border-2 transition-all"
      style={isCurrentUser ? {
        background: 'rgba(255, 215, 0, 0.15)',
        border: '2px solid rgba(255, 215, 0, 0.4)',
        boxShadow: '0 2px 12px rgba(255, 215, 0, 0.3)',
      } : {
        background: '#ffffff',
        border: '2px solid rgba(255, 215, 0, 0.2)',
        boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
      }}
      {...props}
    >
      {/* Rank Badge */}
      <div className="flex-shrink-0 w-12 h-12 flex items-center justify-center">
        {rank <= 3 ? (
          <IoTrophy className="w-6 h-6" style={{ color: getMedalColor(rank) }} />
        ) : (
          <span className="text-lg font-bold text-yellow-700"># {rank}</span>
        )}
      </div>

      {/* User Info */}
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2">
          {user.avatar && (
            <img
              src={user.avatar}
              alt={user.name}
              className="w-8 h-8 rounded-full flex-shrink-0"
            />
          )}
          <div className="min-w-0 flex-1">
            <p className="font-semibold text-neutral-900 truncate">
              {user.name}
              {isCurrentUser && <span className="ml-2 text-xs text-yellow-700">(You)</span>}
            </p>
            <p className="text-xs text-neutral-600 truncate">{user.email}</p>
          </div>
        </div>
      </div>

      {/* Level Badge */}
      <div className="flex-shrink-0">
        <Badge
          variant={getRankBadgeVariant(rank)}
          icon={IoStar}
        >
          Level {level}
        </Badge>
      </div>

      {/* XP */}
      <div className="flex-shrink-0 text-right">
        <p className="text-lg font-bold text-yellow-700">{xp.toLocaleString()}</p>
        <p className="text-xs text-neutral-600">XP</p>
      </div>
    </div>
  );
};

export default RankingRow;
