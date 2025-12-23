import React from 'react';

export const Card = ({
  children,
  className = '',
  shadow = 'md',
  hover = false,
  onClick,
  variant = 'default',
  ...props
}) => {
  const shadowStyles = {
    none: 'shadow-none',
    sm: 'shadow-sm',
    md: 'shadow-md',
    lg: 'shadow-lg',
    xl: 'shadow-xl',
  };

  const variantStyles = {
    default: 'bg-white border border-neutral-200',
    primary: 'bg-gradient-to-br from-primary-50 to-primary-100 border border-primary-200',
    success: 'bg-gradient-to-br from-success-50 to-success-100 border border-success-200',
    danger: 'bg-gradient-to-br from-danger-50 to-danger-100 border border-danger-200',
    dark: 'bg-neutral-800 border border-neutral-700',
  };

  const baseStyles = 'rounded-xl p-6 transition-all duration-200';
  const hoverStyles = hover ? 'hover:shadow-xl hover:-translate-y-1 cursor-pointer' : '';
  const clickableStyles = onClick ? 'cursor-pointer' : '';

  return (
    <div
      className={`${baseStyles} ${shadowStyles[shadow] || shadowStyles.md} ${variantStyles[variant] || variantStyles.default} ${hoverStyles} ${clickableStyles} ${className}`}
      onClick={onClick}
      {...props}
    >
      {children}
    </div>
  );
};

export default Card;
