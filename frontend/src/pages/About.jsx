import React from 'react';
import { IoLogoYoutube, IoBook, IoBulb, IoCheckmarkCircle, IoRefresh } from 'react-icons/io5';
import profileMadmeCodes from '../assets/profileMadmeCodes.png';

export default function About() {
  return (
    <div className="space-y-8 max-w-6xl mx-auto">
      {/* What is Version1 - 2 Column Layout */}
      <div
        className="rounded-lg p-6"
        style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}
      >
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Left Column - Video */}
          <div className="w-full">
            <div className="relative w-full" style={{ paddingBottom: '56.25%' }}>
              <iframe
                className="absolute top-0 left-0 w-full h-full rounded-lg"
                src="https://www.youtube.com/embed/rXqtj-nGupQ"
                title="Version1 Introduction"
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            </div>
          </div>

          {/* Right Column - Text */}
          <div className="flex flex-col justify-center">
            <h1 className="text-3xl font-bold text-neutral-900 mb-4" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif", textShadow: '0 0 20px rgba(255, 215, 0, 0.3)' }}>
              What is Version1?
            </h1>
            <p className="text-base text-neutral-700 leading-relaxed mb-4">
              Version1 is a complete guide for anyone entering tech — whether you're a future tech founder, a manager, or a student.
              From Linux, networking, and internet to full-stack apps, SaaS, and AI, this series takes you from beginner to advanced,
              giving you the foundation to build and launch your own ideas.
            </p>
            <a
              href="https://www.youtube.com/playlist?list=PLmPMBIejpQTv3dhRi8izwWL7lG0r0gZz_"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 px-4 py-2 rounded-lg font-semibold text-white transition-all w-fit"
              style={{
                background: 'linear-gradient(to right, #ffd700, #ffc107)',
                boxShadow: '0 0 10px rgba(255, 215, 0, 0.4)',
              }}
            >
              <IoLogoYoutube className="w-5 h-5" />
              Watch Complete Playlist
            </a>
          </div>
        </div>
      </div>

      {/* How to Use This Site - 2 Column Grid */}
      <div
        className="rounded-lg p-6"
        style={{
          background: '#ffffff',
          border: '2px solid rgba(255, 215, 0, 0.3)',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}
      >
        <h2 className="text-2xl font-bold text-neutral-900 mb-6" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>
          How to Use This Site
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Left Column */}
          <div className="space-y-6">
            {/* Quiz Levels */}
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <IoBook className="w-5 h-5 text-yellow-600" />
                <h3 className="text-lg font-semibold text-neutral-900">Quiz Levels</h3>
              </div>
              <p className="text-neutral-700 leading-relaxed">
                Each quiz level is designed to test your knowledge on specific topics. Start from Level 1 and progress through
                each level by achieving the passing score. Levels are unlocked sequentially, so complete each one to advance.
              </p>
            </div>

            {/* Learning Strategy */}
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <IoBulb className="w-5 h-5 text-yellow-600" />
                <h3 className="text-lg font-semibold text-neutral-900">Learning Strategy</h3>
              </div>
              <p className="text-neutral-700 leading-relaxed">
                Don't know the answer to a question? That's perfectly fine! Use it as an opportunity to research and learn.
                Search the internet, watch the related YouTube videos, and come back to retry the quiz. This active learning
                approach will help you retain knowledge better.
              </p>
            </div>
          </div>

          {/* Right Column */}
          <div className="space-y-6">
            {/* Track Your Progress */}
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <IoCheckmarkCircle className="w-5 h-5 text-yellow-600" />
                <h3 className="text-lg font-semibold text-neutral-900">Track Your Progress</h3>
              </div>
              <p className="text-neutral-700 leading-relaxed">
                Monitor your progress through the dashboard, check your rank on the leaderboard, and earn XP for each completed
                level. Your profile shows all your achievements and completed quizzes.
              </p>
            </div>

            {/* Retry & Improve */}
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <IoRefresh className="w-5 h-5 text-yellow-600" />
                <h3 className="text-lg font-semibold text-neutral-900">Retry & Improve</h3>
              </div>
              <p className="text-neutral-700 leading-relaxed">
                You can retry any quiz to improve your score. Each attempt helps you learn and master the content. Aim for
                100% accuracy on each level!
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Creator Shoutout */}
      <div
        className="rounded-lg p-6"
        style={{
          background: 'rgba(255, 215, 0, 0.15)',
          border: '2px solid rgba(255, 215, 0, 0.4)',
          boxShadow: '0 2px 8px rgba(0, 0, 0, 0.05)',
        }}
      >
        <h2 className="text-2xl font-bold text-neutral-900 mb-4" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>
          Created by Madmecodes
        </h2>
        <div className="flex flex-col md:flex-row items-center md:items-start gap-6">
          <img
            src={profileMadmeCodes}
            alt="Madmecodes"
            className="w-32 h-32 rounded-full border-4"
            style={{ borderColor: '#ffd700', boxShadow: '0 0 20px rgba(255, 215, 0, 0.4)' }}
          />
          <div className="flex-1 space-y-4">
            <p className="text-neutral-700 leading-relaxed">
              This platform and the entire Version1 series was created by <strong>Madmecodes</strong>, a tech content creator
              passionate about helping people enter the tech world.
            </p>

            <div className="space-y-2">
              <h3 className="text-lg font-semibold text-neutral-900">Channel Content:</h3>
              <ul className="space-y-1 text-neutral-700">
                <li>• Tech insights & opinions</li>
                <li>• Podcasts with builders</li>
                <li>• Podcasts with startup founders</li>
                <li>• Personal tech journey stories</li>
              </ul>
            </div>

            <a
              href="https://www.youtube.com/@Madmecodes"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 px-4 py-2 rounded-lg font-semibold text-white transition-all"
              style={{
                background: 'linear-gradient(to right, #ffd700, #ffc107)',
                boxShadow: '0 0 10px rgba(255, 215, 0, 0.4)',
              }}
            >
              <IoLogoYoutube className="w-5 h-5" />
              Visit Madmecodes Channel
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
