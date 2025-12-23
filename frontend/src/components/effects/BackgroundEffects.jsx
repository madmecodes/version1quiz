import React, { useEffect, useState } from 'react';

export const BackgroundEffects = () => {
  const [particles, setParticles] = useState([]);

  useEffect(() => {
    // Generate random particles
    const generatedParticles = Array.from({ length: 50 }).map((_, i) => ({
      id: i,
      left: Math.random() * 100,
      top: Math.random() * 100,
      delay: Math.random() * 5,
      duration: 6 + Math.random() * 4,
    }));
    setParticles(generatedParticles);
  }, []);

  return (
    <>
      {/* Cyberpunk Background */}
      <div className="cyberpunk-bg" />

      {/* Grid Overlay */}
      <div className="grid-overlay" />

      {/* Scan Lines */}
      <div className="scanlines" />

      {/* Animated Gradient Blobs */}
      <div
        className="blob blob-purple"
        style={{
          top: '10%',
          right: '10%',
        }}
      />
      <div
        className="blob blob-cyan"
        style={{
          top: '50%',
          left: '5%',
        }}
      />
      <div
        className="blob blob-pink"
        style={{
          bottom: '5%',
          right: '20%',
        }}
      />

      {/* Floating Particles */}
      <div className="particle">
        {particles.map((particle) => (
          <div
            key={particle.id}
            className="particle-dot"
            style={{
              left: `${particle.left}%`,
              top: `${particle.top}%`,
              animationDelay: `${particle.delay}s`,
              animationDuration: `${particle.duration}s`,
            }}
          />
        ))}
      </div>
    </>
  );
};

export default BackgroundEffects;
