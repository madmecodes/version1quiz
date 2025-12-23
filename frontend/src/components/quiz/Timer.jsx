import React, { useState, useEffect } from 'react';
import { IoTimer } from 'react-icons/io5';

export const Timer = ({
  initialSeconds = 300,
  onTimeUp,
  isActive = true,
  ...props
}) => {
  const [timeLeft, setTimeLeft] = useState(initialSeconds);

  useEffect(() => {
    if (!isActive || timeLeft <= 0) {
      if (timeLeft <= 0) onTimeUp?.();
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          onTimeUp?.();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [isActive, timeLeft, onTimeUp]);

  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;
  const isWarning = timeLeft < 60;
  const isDanger = timeLeft < 30;

  const getTimerStyle = () => {
    if (isDanger) {
      return {
        background: 'rgba(255, 0, 110, 0.15)',
        color: '#ff006e',
        border: '2px solid rgba(255, 0, 110, 0.4)',
        boxShadow: '0 0 10px rgba(255, 0, 110, 0.6)',
      };
    } else if (isWarning) {
      return {
        background: 'rgba(255, 193, 7, 0.15)',
        color: '#ffc107',
        border: '2px solid rgba(255, 193, 7, 0.4)',
        boxShadow: '0 0 10px rgba(255, 193, 7, 0.4)',
      };
    } else {
      return {
        background: 'rgba(0, 240, 255, 0.1)',
        color: '#00f0ff',
        border: '2px solid rgba(0, 240, 255, 0.3)',
        boxShadow: '0 0 10px rgba(0, 240, 255, 0.4)',
      };
    }
  };

  return (
    <div
      className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold text-lg transition-all ${isDanger ? 'animate-pulse' : ''}`}
      style={getTimerStyle()}
      {...props}
    >
      <IoTimer className="w-5 h-5" />
      <span>
        {minutes.toString().padStart(2, '0')}:{seconds.toString().padStart(2, '0')}
      </span>
    </div>
  );
};

export default Timer;
