import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
      window.location.href = '/';
    }
    return Promise.reject(error);
  }
);

export const authAPI = {
  googleLogin: async (accessToken) => {
    const response = await api.post('/users/auth/google/', { access_token: accessToken });
    return response.data;
  },

  getAvailableAvatars: async () => {
    const response = await api.get('/users/available-avatars/');
    return response.data;
  },

  checkUsername: async (username) => {
    const response = await api.post('/users/check-username/', { username });
    return response.data;
  },

  setUsername: async (username, avatar) => {
    const formData = new FormData();
    formData.append('username', username);

    if (avatar) {
      if (avatar.type === 'predefined') {
        formData.append('avatar_id', avatar.data);
      } else if (avatar.type === 'upload') {
        // Convert base64 to blob for upload
        const response = await fetch(avatar.data);
        const blob = await response.blob();
        formData.append('avatar', blob, 'avatar.png');
      }
    }

    const response = await api.post('/users/set-username/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  getProfile: async () => {
    const response = await api.get('/users/profile/');
    return response.data;
  },

  updateProfile: async (data) => {
    const formData = new FormData();

    if (data.avatar && data.avatar_type) {
      if (data.avatar_type === 'predefined') {
        formData.append('avatar_id', data.avatar);
      } else if (data.avatar_type === 'upload') {
        // Convert base64 to blob for upload
        const response = await fetch(data.avatar);
        const blob = await response.blob();
        formData.append('avatar', blob, 'avatar.png');
      }
    }

    // Add other fields if present
    if (data.username) formData.append('username', data.username);
    if (data.first_name) formData.append('first_name', data.first_name);
    if (data.last_name) formData.append('last_name', data.last_name);

    const response = await api.put('/users/profile/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  logout: () => {
    localStorage.removeItem('authToken');
    localStorage.removeItem('user');
    return Promise.resolve();
  },
};

export const quizAPI = {
  getLevels: async () => {
    const response = await api.get('/quiz/levels/');
    return response.data;
  },

  getLevelDetail: async (levelId) => {
    const response = await api.get(`/quiz/levels/${levelId}/`);
    return response.data;
  },

  getLevelQuestions: async (levelId) => {
    const response = await api.get(`/quiz/levels/${levelId}/questions/`);
    return response.data;
  },

  submitQuiz: async (levelId, answers) => {
    const response = await api.post('/quiz/submit/', {
      level_id: levelId,
      answers: answers,
    });
    return response.data;
  },

  getProgress: async () => {
    const response = await api.get('/quiz/progress/');
    return response.data;
  },

  getSubmissionDetail: async (levelId) => {
    const response = await api.get(`/quiz/submission/${levelId}/`);
    return response.data;
  },
};

export const leaderboardAPI = {
  getLeaderboard: async (params = {}) => {
    const response = await api.get('/leaderboard/', { params });
    return response.data;
  },

  getUserRank: async () => {
    const response = await api.get('/leaderboard/user-rank/');
    return response.data;
  },

  updateLeaderboard: async () => {
    const response = await api.post('/leaderboard/update/');
    return response.data;
  },

  getTopLeaderboard: async (limit = 10) => {
    const response = await api.get('/leaderboard/top/', { params: { limit } });
    return response.data;
  },
};

export default api;
