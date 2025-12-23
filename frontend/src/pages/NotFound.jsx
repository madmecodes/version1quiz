import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from '../components';
import { IoArrowBack } from 'react-icons/io5';

export default function NotFound() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-neutral-100 flex items-center justify-center px-4">
      <div className="text-center max-w-md">
        <div className="text-9xl font-bold text-primary-200 mb-4">404</div>
        <h1 className="text-4xl font-bold text-neutral-900 mb-2">Page Not Found</h1>
        <p className="text-lg text-neutral-600 mb-8">
          Sorry, the page you're looking for doesn't exist or has been moved.
        </p>
        <Link to="/dashboard">
          <Button variant="primary" size="lg" icon={IoArrowBack}>
            Back to Dashboard
          </Button>
        </Link>
      </div>
    </div>
  );
}
