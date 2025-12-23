import React, { createContext, useContext, useState, useEffect } from 'react';

const ProgressContext = createContext();

export const ProgressProvider = ({ children }) => {
  const [userProgress, setUserProgress] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Mock: Initialize from localStorage
  useEffect(() => {
    const storedProgress = localStorage.getItem('userProgress');
    if (storedProgress) {
      try {
        const progress = JSON.parse(storedProgress);
        setUserProgress(progress);
      } catch (error) {
        console.error('Failed to parse stored progress:', error);
        localStorage.removeItem('userProgress');
        // Initialize default progress
        setUserProgress({
          totalXP: 0,
          currentLevel: 1,
          levelProgress: {},
          completedLevels: [],
          attemptHistory: [],
        });
      }
    } else {
      // Initialize default progress
      setUserProgress({
        totalXP: 0,
        currentLevel: 1,
        levelProgress: {},
        completedLevels: [],
        attemptHistory: [],
      });
    }
    setIsLoading(false);
  }, []);

  const updateProgress = (levelId, score, xp, passed) => {
    setUserProgress((prev) => {
      const updated = { ...prev };
      updated.totalXP += xp;

      if (!updated.levelProgress[levelId]) {
        updated.levelProgress[levelId] = {
          attempts: 0,
          highestScore: 0,
          xpEarned: 0,
          passed: false,
        };
      }

      const levelData = updated.levelProgress[levelId];
      levelData.attempts += 1;
      levelData.highestScore = Math.max(levelData.highestScore, score);
      levelData.xpEarned += xp;

      if (passed && !levelData.passed) {
        levelData.passed = true;
        if (!updated.completedLevels.includes(levelId)) {
          updated.completedLevels.push(levelId);
        }
        updated.currentLevel = Math.max(updated.currentLevel, parseInt(levelId) + 1);
      }

      updated.attemptHistory.push({
        levelId,
        score,
        xp,
        passed,
        timestamp: new Date().toISOString(),
      });

      localStorage.setItem('userProgress', JSON.stringify(updated));
      return updated;
    });
  };

  const resetProgress = () => {
    const defaultProgress = {
      totalXP: 0,
      currentLevel: 1,
      levelProgress: {},
      completedLevels: [],
      attemptHistory: [],
    };
    setUserProgress(defaultProgress);
    localStorage.setItem('userProgress', JSON.stringify(defaultProgress));
  };

  const getLevelProgress = (levelId) => {
    return userProgress?.levelProgress?.[levelId] || null;
  };

  const isLevelUnlocked = (levelId) => {
    return parseInt(levelId) <= userProgress?.currentLevel;
  };

  const value = {
    userProgress,
    isLoading,
    updateProgress,
    resetProgress,
    getLevelProgress,
    isLevelUnlocked,
  };

  return (
    <ProgressContext.Provider value={value}>{children}</ProgressContext.Provider>
  );
};

export const useProgress = () => {
  const context = useContext(ProgressContext);
  if (!context) {
    throw new Error('useProgress must be used within a ProgressProvider');
  }
  return context;
};

export default ProgressContext;
