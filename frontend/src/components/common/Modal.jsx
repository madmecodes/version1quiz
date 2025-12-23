import React from 'react';
import { IoClose } from 'react-icons/io5';

export const Modal = ({
  isOpen = false,
  onClose,
  title,
  children,
  footer,
  size = 'md',
  className = '',
  closeOnBackdropClick = true,
  ...props
}) => {
  if (!isOpen) return null;

  const sizeStyles = {
    sm: 'max-w-sm',
    md: 'max-w-md',
    lg: 'max-w-lg',
    xl: 'max-w-xl',
    '2xl': 'max-w-2xl',
  };

  const handleBackdropClick = (e) => {
    if (closeOnBackdropClick && e.target === e.currentTarget) {
      onClose?.();
    }
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm"
      onClick={handleBackdropClick}
      {...props}
    >
      <div
        className={`bg-white rounded-xl shadow-2xl max-h-[90vh] overflow-y-auto w-full mx-4 ${sizeStyles[size] || sizeStyles.md} animate-slideIn`}
      >
        {/* Header */}
        {title && (
          <div className="flex items-center justify-between p-6 border-b border-neutral-200">
            <h2 className="text-xl font-bold text-neutral-900">{title}</h2>
            <button
              onClick={onClose}
              className="p-1 text-neutral-600 hover:text-neutral-900 hover:bg-neutral-100 rounded-lg transition-colors"
              aria-label="Close modal"
            >
              <IoClose className="w-6 h-6" />
            </button>
          </div>
        )}

        {/* Body */}
        <div className={`p-6 ${className}`}>
          {children}
        </div>

        {/* Footer */}
        {footer && (
          <div className="p-6 border-t border-neutral-200 flex gap-3 justify-end">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
};

export default Modal;
