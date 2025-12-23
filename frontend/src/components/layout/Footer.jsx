import React from 'react';
import { IoLogoTwitter, IoLogoLinkedin, IoLogoYoutube, IoLogoGithub } from 'react-icons/io5';
import v1logo from '../../assets/v1logo.png';
import profileMadmeCodes from '../../assets/profileMadmeCodes.png';

export const Footer = ({ ...props }) => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="mt-16" style={{
      background: '#f5f5f5',
      borderTop: '2px solid rgba(255, 215, 0, 0.3)',
      boxShadow: '0 -2px 8px rgba(0, 0, 0, 0.05)',
    }} {...props}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          {/* Brand */}
          <div>
            <div className="flex items-center gap-2 mb-4">
              <img
                src={v1logo}
                alt="Version1"
                className="w-16 h-16"
              />
              <span className="font-bold text-neutral-900" style={{ fontFamily: "'Rajdhani', 'Exo 2', system-ui, sans-serif" }}>Version1 Quiz</span>
            </div>
            <p className="text-sm text-neutral-600">
              Level-based indie hacking education platform
            </p>
          </div>

          {/* Links */}
          <div>
            <h3 className="font-semibold text-neutral-900 mb-4">Platform</h3>
            <ul className="space-y-2 text-sm">
              <li>
                <a href="#dashboard" className="transition-colors hover:text-yellow-700" style={{ color: '#737373' }}>
                  Dashboard
                </a>
              </li>
              <li>
                <a href="#leaderboard" className="transition-colors hover:text-yellow-700" style={{ color: '#737373' }}>
                  Leaderboard
                </a>
              </li>
              <li>
                <a href="#profile" className="transition-colors hover:text-yellow-700" style={{ color: '#737373' }}>
                  Profile
                </a>
              </li>
            </ul>
          </div>

          {/* Resources */}
          <div>
            <h3 className="font-semibold text-neutral-900 mb-4">Resources</h3>
            <ul className="space-y-2 text-sm">
              <li>
                <a
                  href="https://www.youtube.com/playlist?list=PLmPMBIejpQTv3dhRi8izwWL7lG0r0gZz_"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="transition-colors hover:text-yellow-700"
                  style={{ color: '#737373' }}
                >
                  YouTube Playlist
                </a>
              </li>
              <li>
                <a
                  href="https://github.com/madmecodes/version1quiz"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="transition-colors hover:text-yellow-700"
                  style={{ color: '#737373' }}
                >
                  GitHub Repository
                </a>
              </li>
            </ul>
          </div>

          {/* Developer */}
          <div>
            <h3 className="font-semibold text-neutral-900 mb-4">Developer</h3>
            <div className="space-y-3">
              <div className="flex items-center gap-2">
                <img
                  src={profileMadmeCodes}
                  alt="Madme"
                  className="w-10 h-10 rounded-full border-2"
                  style={{ borderColor: '#ffd700' }}
                />
                <span className="text-sm font-semibold text-neutral-900">Madme</span>
              </div>
              <div className="flex gap-2">
                <a
                  href="https://x.com/madmecodes"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-2 rounded-lg transition-all"
                  style={{
                    background: 'rgba(255, 215, 0, 0.1)',
                    color: '#f59e0b',
                    border: '1px solid rgba(255, 215, 0, 0.3)',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 215, 0, 0.2)';
                    e.currentTarget.style.boxShadow = '0 0 10px rgba(255, 215, 0, 0.4)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 215, 0, 0.1)';
                    e.currentTarget.style.boxShadow = 'none';
                  }}
                  aria-label="Twitter"
                >
                  <IoLogoTwitter className="w-5 h-5" />
                </a>
                <a
                  href="https://www.linkedin.com/in/ayush-gupta-dev/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-2 rounded-lg transition-all"
                  style={{
                    background: 'rgba(255, 215, 0, 0.1)',
                    color: '#f59e0b',
                    border: '1px solid rgba(255, 215, 0, 0.3)',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 215, 0, 0.2)';
                    e.currentTarget.style.boxShadow = '0 0 10px rgba(255, 215, 0, 0.4)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 215, 0, 0.1)';
                    e.currentTarget.style.boxShadow = 'none';
                  }}
                  aria-label="LinkedIn"
                >
                  <IoLogoLinkedin className="w-5 h-5" />
                </a>
                <a
                  href="https://www.youtube.com/@Madmecodes"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-2 rounded-lg transition-all"
                  style={{
                    background: 'rgba(255, 215, 0, 0.1)',
                    color: '#f59e0b',
                    border: '1px solid rgba(255, 215, 0, 0.3)',
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 215, 0, 0.2)';
                    e.currentTarget.style.boxShadow = '0 0 10px rgba(255, 215, 0, 0.4)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'rgba(255, 215, 0, 0.1)';
                    e.currentTarget.style.boxShadow = 'none';
                  }}
                  aria-label="YouTube"
                >
                  <IoLogoYoutube className="w-5 h-5" />
                </a>
              </div>
            </div>
          </div>
        </div>

        {/* Contribution Section */}
        <div
          className="rounded-lg p-4 mb-8"
          style={{
            background: 'rgba(255, 215, 0, 0.08)',
            border: '1px solid rgba(255, 215, 0, 0.3)',
          }}
        >
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div className="flex-1">
              <h3 className="font-semibold text-neutral-900 mb-1 flex items-center gap-2">
                <IoLogoGithub className="w-5 h-5" />
                Open Source & Community
              </h3>
              <p className="text-sm text-neutral-700">
                Found a bug? Have an idea? Contributions are welcome! Visit our GitHub repository to report issues, suggest features, or contribute code.
              </p>
            </div>
            <a
              href="https://github.com/madmecodes/version1quiz"
              target="_blank"
              rel="noopener noreferrer"
              className="px-4 py-2 rounded-lg font-semibold text-white transition-all whitespace-nowrap"
              style={{
                background: 'linear-gradient(to right, #ffd700, #ffc107)',
                boxShadow: '0 0 10px rgba(255, 215, 0, 0.4)',
              }}
            >
              View on GitHub
            </a>
          </div>
        </div>

        {/* Divider */}
        <div style={{ borderTop: '1px solid rgba(255, 215, 0, 0.2)' }} className="pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <p className="text-sm text-neutral-600">
              © {currentYear} Version1 Quiz. All rights reserved.
            </p>
            <div className="flex gap-6 mt-4 md:mt-0 text-sm">
              <a href="#privacy" className="transition-colors hover:text-yellow-700" style={{ color: '#737373' }}>
                Privacy Policy
              </a>
              <a href="#terms" className="transition-colors hover:text-yellow-700" style={{ color: '#737373' }}>
                Terms of Service
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
