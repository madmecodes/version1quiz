import React, { useState, useEffect } from 'react';
import { useLocation, useParams, useNavigate } from 'react-router-dom';
import { Button, Card, Badge } from '../components';
import { IoCheckmark, IoClose, IoArrowForward, IoHome, IoChevronDown } from 'react-icons/io5';
import { quizAPI } from '../services/api';

export default function Results() {
  const { levelId } = useParams();
  const location = useLocation();
  const navigate = useNavigate();
  const [showAnimation, setShowAnimation] = useState(false);
  const [submissionDetails, setSubmissionDetails] = useState(null);
  const [loadingDetails, setLoadingDetails] = useState(true);
  const [expandedQuestions, setExpandedQuestions] = useState(new Set());

  const result = location.state?.result || null;
  const level = location.state?.level || null;

  useEffect(() => {
    const timer = setTimeout(() => setShowAnimation(true), 200);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    const fetchSubmissionDetails = async () => {
      try {
        const details = await quizAPI.getSubmissionDetail(levelId);
        setSubmissionDetails(details);
      } catch (error) {
        console.error('Error fetching submission details:', error);
      } finally {
        setLoadingDetails(false);
      }
    };

    if (levelId) {
      fetchSubmissionDetails();
    }
  }, [levelId]);

  if (!result || !level) {
    return (
      <div className="flex items-center justify-center h-64">
        <div style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          borderRadius: '0.75rem',
          padding: '2rem',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <p className="text-center text-neutral-700 mb-4">No results found</p>
          <Button
            variant="primary"
            onClick={() => navigate('/dashboard')}
            className="w-full"
          >
            Back to Dashboard
          </Button>
        </div>
      </div>
    );
  }

  const { passed, percentage, xp_earned, submission } = result;
  const score = submission?.score;
  const total_questions = submission?.total_questions;

  return (
    <div className="space-y-4 max-w-3xl mx-auto">
      {/* Result Card */}
      <div
        className={`transform transition-all duration-1000 ${
          showAnimation ? 'scale-100 opacity-100' : 'scale-95 opacity-0'
        }`}
      >
        <div
          className="text-center space-y-4"
          style={{
            background: passed
              ? 'rgba(0, 255, 136, 0.1)'
              : 'rgba(255, 0, 110, 0.1)',
            border: `2px solid ${passed ? 'rgba(0, 255, 136, 0.3)' : 'rgba(255, 0, 110, 0.3)'}`,
            borderRadius: '0.75rem',
            padding: '1.5rem',
            boxShadow: `0 2px 8px rgba(0, 0, 0, 0.05)`,
          }}
        >
          {/* Result Indicator */}
          <div className="flex items-center justify-center gap-3">
            <div
              className="w-16 h-16 rounded-full flex items-center justify-center"
              style={{
                background: passed
                  ? 'rgba(0, 255, 136, 0.2)'
                  : 'rgba(255, 0, 110, 0.2)',
              }}
            >
              {passed ? (
                <IoCheckmark style={{ color: '#00ff88' }} className="w-8 h-8" />
              ) : (
                <IoClose style={{ color: '#ff006e' }} className="w-8 h-8" />
              )}
            </div>
            <div className="text-left">
              <h1 className="text-2xl font-bold" style={{
                color: passed ? '#00ff88' : '#ff006e',
                fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif",
                textShadow: `0 0 15px rgba(${passed ? '0, 255, 136' : '255, 0, 110'}, 0.6)`
              }}>
                {passed ? 'Level Complete' : 'Try Again'}
              </h1>
              <p className="text-sm" style={{ color: passed ? '#00ff88' : '#ff006e' }}>
                {passed
                  ? "You've unlocked the next level."
                  : 'Score higher to pass. Keep practicing!'}
              </p>
            </div>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-3 gap-3 py-3" style={{ borderTop: `1px solid ${passed ? 'rgba(0, 255, 136, 0.2)' : 'rgba(255, 0, 110, 0.2)'}`, borderBottom: `1px solid ${passed ? 'rgba(0, 255, 136, 0.2)' : 'rgba(255, 0, 110, 0.2)'}` }}>
            <div>
              <p className="text-xs font-medium text-neutral-600">Score</p>
              <p className="text-2xl font-bold text-neutral-900">
                {score}/{total_questions}
              </p>
            </div>
            <div>
              <p className="text-xs font-medium text-neutral-600">Accuracy</p>
              <p className="text-2xl font-bold text-neutral-900">
                {percentage}%
              </p>
            </div>
            <div>
              <p className="text-xs font-medium text-yellow-700">XP Earned</p>
              <p className="text-2xl font-bold text-yellow-700">+{xp_earned}</p>
            </div>
          </div>

          {/* Details */}
          <div className="text-left space-y-2">
            <h3 className="font-bold text-neutral-900 text-sm" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>Quiz Details</h3>
            <div className="space-y-1 text-xs">
              <div className="flex justify-between">
                <span className="text-neutral-600">Level</span>
                <span className="font-semibold text-neutral-900">{level.title}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-neutral-600">Passing Requirement</span>
                <span className="font-semibold text-neutral-900">{level.passing_percentage}%</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-neutral-600">Difficulty</span>
                <Badge variant="primary" size="sm">
                  {level.difficulty}
                </Badge>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Wrong Questions Section - Collapsible */}
      {!loadingDetails && submissionDetails && submissionDetails.questions && (
        (() => {
          const wrongQuestions = submissionDetails.questions.filter((q, idx) =>
            submissionDetails.submission.answers[idx] !== q.correct_answer
          );

          return wrongQuestions.length > 0 ? (
            <div className={`transform transition-all duration-1000 ${
              showAnimation ? 'translate-y-0 opacity-100' : 'translate-y-4 opacity-0'
            }`}>
              <div style={{
                background: '#ffffff',
                border: '2px solid rgba(255, 0, 110, 0.3)',
                borderRadius: '0.75rem',
                overflow: 'hidden',
              }}>
                {/* Header */}
                <div
                  onClick={() => setExpandedQuestions(prev => prev.size === 0 ? new Set([...wrongQuestions.map(q => q.id)]) : new Set())}
                  className="p-4 cursor-pointer hover:bg-gray-50 transition-colors flex items-center justify-between"
                  style={{ borderBottom: expandedQuestions.size > 0 ? '1px solid rgba(255, 0, 110, 0.2)' : 'none' }}
                >
                  <div className="flex items-center gap-3">
                    <IoClose style={{ color: '#ff006e' }} className="w-5 h-5" />
                    <h3 className="font-bold text-neutral-900" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>
                      Questions You Got Wrong ({wrongQuestions.length})
                    </h3>
                  </div>
                  <IoChevronDown
                    className="w-5 h-5 transition-transform"
                    style={{
                      color: '#ff006e',
                      transform: expandedQuestions.size > 0 ? 'rotate(180deg)' : 'rotate(0deg)'
                    }}
                  />
                </div>

                {/* Collapsible Content */}
                {expandedQuestions.size > 0 && (
                  <div className="space-y-1 p-4 pt-0">
                    {wrongQuestions.map((question) => {
                      const isExpanded = expandedQuestions.has(question.id);
                      const userAnswerIdx = submissionDetails.submission.answers[submissionDetails.questions.indexOf(question)];
                      return (
                        <div
                          key={question.id}
                          style={{
                            background: 'rgba(255, 0, 110, 0.05)',
                            border: '1px solid rgba(255, 0, 110, 0.2)',
                            borderRadius: '0.5rem',
                            overflow: 'hidden',
                          }}
                        >
                          {/* Question Header */}
                          <div
                            onClick={() => setExpandedQuestions(prev => {
                              const newSet = new Set(prev);
                              if (newSet.has(question.id)) {
                                newSet.delete(question.id);
                              } else {
                                newSet.add(question.id);
                              }
                              return newSet;
                            })}
                            className="p-3 cursor-pointer hover:bg-gray-100 transition-colors flex items-start justify-between"
                          >
                            <p className="font-semibold text-neutral-900 text-sm flex-1">{question.question}</p>
                            <IoChevronDown
                              className="w-4 h-4 flex-shrink-0 mt-1 ml-2 transition-transform"
                              style={{
                                color: '#ff006e',
                                transform: isExpanded ? 'rotate(180deg)' : 'rotate(0deg)'
                              }}
                            />
                          </div>

                          {/* Question Details */}
                          {isExpanded && (
                            <div className="px-3 pb-3 pt-2 space-y-2 border-t border-rgba(255, 0, 110, 0.2)">
                              {question.options.map((option, optIdx) => (
                                <div
                                  key={optIdx}
                                  className="p-2 rounded text-sm"
                                  style={{
                                    background:
                                      optIdx === question.correct_answer
                                        ? 'rgba(0, 255, 136, 0.15)'
                                        : optIdx === userAnswerIdx
                                        ? 'rgba(255, 0, 110, 0.15)'
                                        : '#f5f5f5',
                                    border:
                                      optIdx === question.correct_answer
                                        ? '1px solid rgba(0, 255, 136, 0.5)'
                                        : optIdx === userAnswerIdx
                                        ? '1px solid rgba(255, 0, 110, 0.5)'
                                        : '1px solid #e5e5e5',
                                  }}
                                >
                                  <div className="flex items-center gap-2">
                                    {optIdx === question.correct_answer && (
                                      <IoCheckmark style={{ color: '#00ff88' }} className="w-4 h-4" />
                                    )}
                                    {optIdx === userAnswerIdx && optIdx !== question.correct_answer && (
                                      <IoClose style={{ color: '#ff006e' }} className="w-4 h-4" />
                                    )}
                                    <span className={optIdx === question.correct_answer ? 'font-semibold text-success-700' : optIdx === userAnswerIdx ? 'text-red-600' : 'text-neutral-600'}>
                                      {option}
                                    </span>
                                  </div>
                                </div>
                              ))}
                              {question.explanation && (
                                <div className="mt-2 p-2 bg-blue-50 rounded border-l-2 border-blue-400">
                                  <p className="text-xs text-blue-700"><strong>Explanation:</strong> {question.explanation}</p>
                                </div>
                              )}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            </div>
          ) : null;
        })()
      )}

      {/* Action Buttons */}
      <div className={`grid grid-cols-2 gap-3 transform transition-all duration-1000 ${
        showAnimation ? 'translate-y-0 opacity-100' : 'translate-y-4 opacity-0'
      }`}>
        <Button
          variant="secondary"
          size="md"
          icon={IoHome}
          onClick={() => navigate('/dashboard')}
          className="w-full"
        >
          Dashboard
        </Button>
        {passed ? (
          <Button
            variant="primary"
            size="md"
            icon={IoArrowForward}
            onClick={() => navigate(`/quiz/${parseInt(levelId) + 1}`)}
            className="w-full"
          >
            Next Level
          </Button>
        ) : (
          <Button
            variant="primary"
            size="md"
            icon={IoArrowForward}
            onClick={() => navigate(`/quiz/${levelId}`)}
            className="w-full"
          >
            Retry Level
          </Button>
        )}
      </div>

      {/* Celebration/Tips Message */}
      {passed ? (
        <div style={{
          background: 'rgba(0, 255, 136, 0.1)',
          border: '2px solid rgba(0, 255, 136, 0.3)',
          borderRadius: '0.75rem',
          padding: '1rem',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }} className="text-center">
          <p className="text-lg font-bold text-success-700 mb-1" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>Great job!</p>
          <p className="text-sm text-success-600">
            You've earned <span className="font-bold text-success-700">{xp_earned} XP</span> and are on your way to becoming an indie hacking expert!
          </p>
        </div>
      ) : (
        <div style={{
          background: 'rgba(255, 193, 7, 0.1)',
          border: '2px solid rgba(255, 193, 7, 0.3)',
          borderRadius: '0.75rem',
          padding: '1rem',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}>
          <h3 className="font-bold text-yellow-700 text-sm mb-2" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>
            Tips to Improve
          </h3>
          <ul className="space-y-1 text-xs text-yellow-700">
            <li>• Review the concepts covered in this level</li>
            <li>• Read each question carefully before answering</li>
            <li>• Consider each option thoroughly</li>
          </ul>
        </div>
      )}
    </div>
  );
}
