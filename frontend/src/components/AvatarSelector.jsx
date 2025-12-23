import React, { useState, useEffect } from 'react';
import { IoCloudUpload, IoCheckmarkCircle } from 'react-icons/io5';
import { authAPI } from '../services/api';

export default function AvatarSelector({ selectedAvatar, onAvatarChange }) {
  const [uploadedImage, setUploadedImage] = useState(null);
  const [predefinedAvatars, setPredefinedAvatars] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAvatars = async () => {
      try {
        const data = await authAPI.getAvailableAvatars();
        setPredefinedAvatars(data.avatars);
      } catch (error) {
        console.error('Failed to fetch avatars:', error);
        setPredefinedAvatars([]);
      } finally {
        setLoading(false);
      }
    };

    fetchAvatars();
  }, []);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (file.size > 5 * 1024 * 1024) {
        alert('File size must be less than 5MB');
        return;
      }

      if (!file.type.startsWith('image/')) {
        alert('Please upload an image file');
        return;
      }

      const reader = new FileReader();
      reader.onloadend = () => {
        setUploadedImage(reader.result);
        onAvatarChange({ type: 'upload', data: reader.result });
      };
      reader.readAsDataURL(file);
    }
  };

  const handlePredefinedSelect = (avatar) => {
    setUploadedImage(null);
    onAvatarChange({ type: 'predefined', data: avatar.id, src: avatar.url });
  };

  const isSelected = (avatarId) => {
    return selectedAvatar?.type === 'predefined' && selectedAvatar?.data === avatarId;
  };

  const isUploadSelected = () => {
    return selectedAvatar?.type === 'upload';
  };

  return (
    <div className="space-y-4">
      <div>
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Choose Your Avatar</h3>

        {/* Predefined Avatars Grid */}
        {loading ? (
          <div className="flex justify-center items-center py-8">
            <div className="text-sm text-neutral-600">Loading avatars...</div>
          </div>
        ) : (
          <div className="grid grid-cols-5 gap-3 mb-4">
            {predefinedAvatars.map((avatar) => (
              <button
                key={avatar.id}
                type="button"
                onClick={() => handlePredefinedSelect(avatar)}
                className="relative group cursor-pointer transition-all"
                style={{
                  opacity: isSelected(avatar.id) ? 1 : 0.7,
                }}
              >
                <img
                  src={avatar.url}
                  alt={avatar.name}
                  className="w-full h-full rounded-full border-2 transition-all group-hover:scale-110"
                  style={{
                    borderColor: isSelected(avatar.id) ? '#ffd700' : 'rgba(255, 215, 0, 0.3)',
                    boxShadow: isSelected(avatar.id) ? '0 0 15px rgba(255, 215, 0, 0.6)' : 'none',
                  }}
                />
                {isSelected(avatar.id) && (
                  <div className="absolute -top-1 -right-1 bg-yellow-500 rounded-full p-1">
                    <IoCheckmarkCircle className="w-4 h-4 text-white" />
                  </div>
                )}
              </button>
            ))}
          </div>
        )}

        {/* Upload Custom Avatar */}
        <div className="mt-4">
          <label
            htmlFor="avatar-upload"
            className="flex items-center justify-center gap-2 px-4 py-3 rounded-lg cursor-pointer transition-all border-2 border-dashed"
            style={{
              background: isUploadSelected() ? 'rgba(255, 215, 0, 0.1)' : 'rgba(255, 215, 0, 0.05)',
              borderColor: isUploadSelected() ? '#ffd700' : 'rgba(255, 215, 0, 0.3)',
            }}
          >
            <IoCloudUpload className="w-5 h-5 text-yellow-600" />
            <span className="text-sm font-medium text-neutral-700">
              {uploadedImage ? 'Change Custom Avatar' : 'Upload Custom Avatar'}
            </span>
          </label>
          <input
            id="avatar-upload"
            type="file"
            accept="image/*"
            onChange={handleFileUpload}
            className="hidden"
          />
          <p className="mt-2 text-xs text-neutral-600 text-center">
            Max 5MB. JPG, PNG, GIF supported.
          </p>
        </div>

        {/* Preview Uploaded Image */}
        {uploadedImage && (
          <div className="mt-4 flex justify-center">
            <div className="relative">
              <img
                src={uploadedImage}
                alt="Uploaded avatar"
                className="w-24 h-24 rounded-full border-4"
                style={{
                  borderColor: '#ffd700',
                  boxShadow: '0 0 20px rgba(255, 215, 0, 0.4)',
                }}
              />
              <div className="absolute -top-1 -right-1 bg-yellow-500 rounded-full p-1">
                <IoCheckmarkCircle className="w-5 h-5 text-white" />
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
