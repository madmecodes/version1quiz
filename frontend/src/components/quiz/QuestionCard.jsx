import React from 'react';
import { Card, Button } from '../common';
import { IoArrowBack } from 'react-icons/io5';

export const QuestionCard = ({
  questionNumber,
  totalQuestions,
  question,
  options,
  selectedOption,
  onSelectOption,
  isAnswered,
  onSubmit,
  onPrevious,
  loading = false,
  ...props
}) => {
  return (
    <div style={{
      background: '#ffffff',
      border: '2px solid rgba(255, 215, 0, 0.3)',
      borderRadius: '0.75rem',
      padding: '1.5rem',
      boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
    }} className="space-y-6" {...props}>
      {/* Question Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex-1">
          <p className="text-sm font-medium text-yellow-700 mb-1" style={{ textShadow: '0 0 8px rgba(255, 215, 0, 0.5)' }}>
            Question {questionNumber} of {totalQuestions}
          </p>
          <h2 className="text-2xl font-bold text-neutral-900" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>{question}</h2>
        </div>
        <div className="ml-4 px-4 py-2 bg-gradient-to-br from-yellow-400 via-yellow-500 to-yellow-600 text-white rounded-lg font-semibold" style={{ boxShadow: '0 0 8px rgba(255, 215, 0, 0.5)' }}>
          {questionNumber}/{totalQuestions}
        </div>
      </div>

      {/* Progress Indicator */}
      <div className="w-full bg-neutral-200 rounded-full h-1 overflow-hidden" style={{ border: '1px solid rgba(255, 215, 0, 0.3)' }}>
        <div
          className="h-full transition-all duration-300"
          style={{
            background: 'linear-gradient(to right, #ffd700, #ffc107)',
            boxShadow: '0 0 10px rgba(255, 215, 0, 0.6)',
            width: `${(questionNumber / totalQuestions) * 100}%`
          }}
        />
      </div>

      {/* Options */}
      <div className="space-y-3 py-4">
        {options.map((option, index) => (
          <label
            key={index}
            className="flex items-center p-4 rounded-lg border-2 cursor-pointer transition-all"
            style={
              selectedOption === index
                ? {
                    borderColor: '#ffd700',
                    background: 'rgba(255, 215, 0, 0.15)',
                    boxShadow: '0 0 10px rgba(255, 215, 0, 0.6)',
                  }
                : {
                    borderColor: 'rgba(255, 215, 0, 0.2)',
                    background: 'rgba(255, 215, 0, 0.05)',
                  }
            }
          >
            <input
              type="radio"
              name="option"
              value={index}
              checked={selectedOption === index}
              onChange={() => !isAnswered && onSelectOption(index)}
              disabled={isAnswered}
              className="w-4 h-4 cursor-pointer"
              style={{ accentColor: '#ffd700' }}
            />
            <span className="ml-3 text-base font-medium text-neutral-800">
              {option}
            </span>
          </label>
        ))}
      </div>

      {/* Action Buttons */}
      <div className="flex justify-between gap-3 pt-4" style={{ borderTop: '1px solid rgba(255, 215, 0, 0.3)' }}>
        {/* Previous Button */}
        {questionNumber > 1 && (
          <Button
            variant="secondary"
            onClick={onPrevious}
            icon={IoArrowBack}
          >
            Previous
          </Button>
        )}
        <div className="flex-1" />
        {/* Submit/Next Button */}
        <Button
          variant={selectedOption !== null ? 'primary' : 'secondary'}
          onClick={onSubmit}
          disabled={selectedOption === null || isAnswered || loading}
          loading={loading}
        >
          {isAnswered ? 'Next Question' : 'Submit Answer'}
        </Button>
      </div>
    </div>
  );
};

export default QuestionCard;
