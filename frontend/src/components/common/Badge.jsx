import React from 'react';

export const Badge = ({
  children,
  variant = 'primary',
  size = 'md',
  className = '',
  icon: Icon = null,
  ...props
}) => {
  const baseStyles = 'inline-flex items-center justify-center gap-1.5 font-semibold rounded-full';

  const variants = {
    primary: 'bg-primary-100 text-primary-700',
    secondary: 'bg-neutral-200 text-neutral-700',
    success: 'bg-success-100 text-success-700',
    danger: 'bg-danger-100 text-danger-700',
    warning: 'bg-yellow-100 text-yellow-700',
  };

  const sizes = {
    sm: 'px-2 py-1 text-xs',
    md: 'px-3 py-1.5 text-sm',
    lg: 'px-4 py-2 text-base',
  };

  const variantStyles = variants[variant] || variants.primary;
  const sizeStyles = sizes[size] || sizes.md;

  return (
    <span className={`${baseStyles} ${variantStyles} ${sizeStyles} ${className}`} {...props}>
      {Icon && <Icon className="w-4 h-4" />}
      {children}
    </span>
  );
};

export default Badge;
