import React from 'react';

export const Button = ({
  children,
  variant = 'primary',
  size = 'md',
  className = '',
  disabled = false,
  loading = false,
  icon: Icon = null,
  iconPosition = 'left',
  onClick,
  type = 'button',
  ...props
}) => {
  const baseStyles = 'font-semibold rounded-lg transition-all duration-200 inline-flex items-center justify-center gap-2 focus-visible:outline-2 focus-visible:outline-offset-2';

  const variants = {
    primary: 'bg-primary-600 text-white hover:bg-primary-700 disabled:bg-primary-400 focus-visible:outline-primary-600',
    secondary: 'bg-neutral-200 text-neutral-900 hover:bg-neutral-300 disabled:bg-neutral-100 focus-visible:outline-neutral-600',
    success: 'bg-success-600 text-white hover:bg-success-700 disabled:bg-success-400 focus-visible:outline-success-600',
    danger: 'bg-danger-600 text-white hover:bg-danger-700 disabled:bg-danger-400 focus-visible:outline-danger-600',
    outline: 'border-2 border-primary-600 text-primary-600 hover:bg-primary-50 disabled:border-primary-300 disabled:text-primary-300 focus-visible:outline-primary-600',
    ghost: 'text-primary-600 hover:bg-primary-50 disabled:text-primary-300 focus-visible:outline-primary-600',
  };

  const sizes = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
    xl: 'px-8 py-4 text-xl',
  };

  const variantStyles = variants[variant] || variants.primary;
  const sizeStyles = sizes[size] || sizes.md;

  return (
    <button
      type={type}
      disabled={disabled || loading}
      onClick={onClick}
      className={`${baseStyles} ${variantStyles} ${sizeStyles} ${disabled || loading ? 'cursor-not-allowed opacity-60' : 'cursor-pointer'} ${className}`}
      {...props}
    >
      {loading && (
        <div className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />
      )}
      {Icon && iconPosition === 'left' && <Icon className="w-5 h-5" />}
      <span>{children}</span>
      {Icon && iconPosition === 'right' && <Icon className="w-5 h-5" />}
    </button>
  );
};

export default Button;
