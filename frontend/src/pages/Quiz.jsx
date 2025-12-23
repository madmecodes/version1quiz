import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../context';
import { QuestionCard } from '../components/quiz';
import { Button } from '../components';
import { quizAPI } from '../services/api';
import { IoChevronBack } from 'react-icons/io5';
import LoginModal from './Login';

export default function Quiz() {
  const { levelId } = useParams();
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();

  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [answeredQuestions, setAnsweredQuestions] = useState(new Set());
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [level, setLevel] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [showLoginModal, setShowLoginModal] = useState(false);

  useEffect(() => {
    // Check authentication first
    if (!isAuthenticated) {
      setShowLoginModal(true);
      return;
    }

    const fetchQuizData = async () => {
      try {
        setLoading(true);
        const [levelData, questionsData] = await Promise.all([
          quizAPI.getLevelDetail(levelId),
          quizAPI.getLevelQuestions(levelId),
        ]);
        setLevel(levelData);
        setQuestions(questionsData);
      } catch (error) {
        console.error('Error fetching quiz data:', error);
        navigate('/dashboard');
      } finally {
        setLoading(false);
      }
    };

    fetchQuizData();
  }, [levelId, isAuthenticated, navigate]);

  const handleSelectOption = (optionIndex) => {
    if (!answeredQuestions.has(currentQuestionIndex)) {
      setSelectedAnswers({
        ...selectedAnswers,
        [currentQuestionIndex]: optionIndex,
      });
    }
  };

  const handleSubmitAnswer = async () => {
    setAnsweredQuestions(new Set([...answeredQuestions, currentQuestionIndex]));

    if (currentQuestionIndex < questions.length - 1) {
      setTimeout(() => {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
      }, 1000);
    }
  };

  const handlePreviousQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(currentQuestionIndex - 1);
    }
  };

  const handleFinishQuiz = async () => {
    setSubmitting(true);
    try {
      // Prepare answers array - just the selected option indices
      const answers = questions.map((question, index) => selectedAnswers[index] ?? -1);

      // Submit quiz to backend
      const response = await quizAPI.submitQuiz(levelId, answers);

      // Navigate to results
      navigate(`/results/${levelId}`, {
        state: {
          result: response,
          level,
        },
      });
    } catch (error) {
      console.error('Quiz submission failed:', error);
      alert('Failed to submit quiz. Please try again.');
    } finally {
      setSubmitting(false);
    }
  };

  const handleLoginSuccess = () => {
    setShowLoginModal(false);
    // The useEffect will automatically re-run when isAuthenticated changes
  };

  const progress = questions.length > 0 ? ((currentQuestionIndex + 1) / questions.length) * 100 : 0;
  const allQuestionsAnswered = answeredQuestions.size === questions.length;

  // Show login modal if not authenticated
  if (showLoginModal) {
    return (
      <LoginModal
        isOpen={showLoginModal}
        onClose={() => navigate('/dashboard')}
        onSuccess={handleLoginSuccess}
      />
    );
  }

  // Show loading spinner
  if (loading || !level || questions.length === 0) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="w-12 h-12 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin" />
      </div>
    );
  }

  const currentQuestion = questions[currentQuestionIndex];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <button
          onClick={() => navigate('/dashboard')}
          className="flex items-center gap-2 font-medium transition-all"
          style={{ color: '#f59e0b', textShadow: '0 0 10px rgba(255, 215, 0, 0.6)' }}
        >
          <IoChevronBack className="w-5 h-5" />
          Back to Dashboard
        </button>
      </div>

      {/* Main Quiz Area */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Question Card */}
        <div className="lg:col-span-2">
          <QuestionCard
            questionNumber={currentQuestionIndex + 1}
            totalQuestions={questions.length}
            question={currentQuestion.question}
            options={currentQuestion.options}
            selectedOption={selectedAnswers[currentQuestionIndex] ?? null}
            onSelectOption={handleSelectOption}
            isAnswered={answeredQuestions.has(currentQuestionIndex)}
            onSubmit={handleSubmitAnswer}
            onPrevious={handlePreviousQuestion}
            loading={submitting}
          />
        </div>

        {/* Sidebar - Progress */}
        <div className="lg:col-span-1">
          <div style={{
            background: '#ffffff',
            border: '2px solid rgba(255, 215, 0, 0.3)',
            borderRadius: '0.75rem',
            padding: '1.5rem',
            boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
            maxHeight: 'calc(100vh - 120px)',
            overflowY: 'auto'
          }} className="sticky top-20 space-y-4">
            {/* Topic Title */}
            <div className="space-y-2">
              <h2 className="font-bold text-neutral-900" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>{level.title}</h2>
              <p className="text-xs text-neutral-600">{level.description}</p>
            </div>

            {/* Progress Bar */}
            <div className="space-y-2">
              <h3 className="font-bold text-neutral-900 text-sm" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>Progress</h3>
              <div className="w-full bg-neutral-200 rounded-full h-2 overflow-hidden" style={{ border: '1px solid rgba(255, 215, 0, 0.3)' }}>
                <div
                  className="h-full transition-all duration-300"
                  style={{
                    background: 'linear-gradient(to right, #ffd700, #ffc107)',
                    boxShadow: '0 0 10px rgba(255, 215, 0, 0.6)',
                    width: `${progress}%`
                  }}
                />
              </div>
              <p className="text-xs text-neutral-600">
                {currentQuestionIndex + 1} of {questions.length} answered
              </p>
            </div>

            {/* Finish Button */}
            {allQuestionsAnswered && (
              <Button
                variant="success"
                size="lg"
                onClick={handleFinishQuiz}
                loading={submitting}
                className="w-full"
              >
                Finish Quiz
              </Button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
