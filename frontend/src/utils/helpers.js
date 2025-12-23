/**
 * Format number with thousand separators
 */
export const formatNumber = (num) => {
  return new Intl.NumberFormat().format(num);
};

/**
 * Calculate percentage
 */
export const calculatePercentage = (current, total) => {
  if (total === 0) return 0;
  return Math.round((current / total) * 100);
};

/**
 * Get level badge color based on difficulty
 */
export const getDifficultyColor = (difficulty) => {
  const colors = {
    Beginner: 'warning',
    Intermediate: 'primary',
    Advanced: 'danger',
  };
  return colors[difficulty] || 'primary';
};

/**
 * Get level status
 */
export const getLevelStatus = (levelId, userProgress) => {
  if (!userProgress) return 'locked';

  const levelProgress = userProgress?.levelProgress?.[levelId];
  if (!levelProgress) return 'available';
  if (levelProgress.passed) return 'completed';
  return 'attempted';
};

/**
 * Calculate XP progress for current level
 */
export const calculateXPProgress = (currentXP, nextLevelXP) => {
  const progress = Math.min((currentXP / nextLevelXP) * 100, 100);
  return Math.round(progress);
};

/**
 * Format date
 */
export const formatDate = (date) => {
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  }).format(new Date(date));
};

/**
 * Format time remaining
 */
export const formatTimeRemaining = (seconds) => {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  if (hours > 0) {
    return `${hours}h ${minutes}m`;
  }
  if (minutes > 0) {
    return `${minutes}m ${secs}s`;
  }
  return `${secs}s`;
};

/**
 * Get next level requirement
 */
export const getNextLevelXP = (currentLevel) => {
  // Simple XP progression: each level requires 500 * level XP
  return 500 * (currentLevel + 1);
};

/**
 * Shuffle array (Fisher-Yates)
 */
export const shuffleArray = (array) => {
  const shuffled = [...array];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
};

/**
 * Get medal emoji based on rank
 */
export const getMedalEmoji = (rank) => {
  switch (rank) {
    case 1:
      return '🥇';
    case 2:
      return '🥈';
    case 3:
      return '🥉';
    default:
      return '';
  }
};

/**
 * Calculate streak
 */
export const calculateStreak = (attempts) => {
  if (!attempts || attempts.length === 0) return 0;

  const recentAttempts = attempts.slice(-10);
  let streak = 0;

  for (let i = recentAttempts.length - 1; i >= 0; i--) {
    if (recentAttempts[i].passed) {
      streak += 1;
    } else {
      break;
    }
  }

  return streak;
};
