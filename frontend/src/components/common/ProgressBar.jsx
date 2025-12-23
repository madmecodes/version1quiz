import React from 'react';

export const ProgressBar = ({
  current = 0,
  total = 100,
  variant = 'primary',
  size = 'md',
  showLabel = true,
  animated = true,
  className = '',
  label = '',
  ...props
}) => {
  const percentage = Math.min((current / total) * 100, 100);

  const variantStyles = {
    primary: 'bg-gradient-to-r from-primary-400 to-primary-600',
    success: 'bg-gradient-to-r from-success-400 to-success-600',
    danger: 'bg-gradient-to-r from-danger-400 to-danger-600',
    warning: 'bg-gradient-to-r from-yellow-400 to-yellow-600',
  };

  const sizeStyles = {
    sm: 'h-2',
    md: 'h-3',
    lg: 'h-4',
  };

  const bgColor = variantStyles[variant] || variantStyles.primary;
  const sizeClass = sizeStyles[size] || sizeStyles.md;

  return (
    <div className={`w-full ${className}`} {...props}>
      {(showLabel || label) && (
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium text-neutral-700">
            {label || `${current} / ${total}`}
          </span>
          {showLabel && (
            <span className="text-xs font-semibold text-primary-600">
              {Math.round(percentage)}%
            </span>
          )}
        </div>
      )}
      <div className={`w-full bg-neutral-200 rounded-full overflow-hidden ${sizeClass}`}>
        <div
          className={`${bgColor} ${sizeClass} rounded-full transition-all duration-500 ease-out ${animated ? 'shadow-glow' : ''}`}
          style={{
            width: `${percentage}%`,
          }}
        />
      </div>
    </div>
  );
};

export default ProgressBar;
