const ENDPOINT =
  process.env.NODE_ENV === 'production'
    ? `https://${process.env.REACT_APP_BACKEND_URL}/api`
    : `http://${window.location.hostname}:8080`;

export const TRACK_API_URL = `${ENDPOINT}/track/`;
export const ACTIVITIES_API_URL = `${ENDPOINT}/activities/`;

export const SUBMISSION_API_URL = `${ENDPOINT}/submission/`;

export const USER_API_URL = `${ENDPOINT}/user/`;

export const LOGIN_URL = '/api-auth/login';
export const LOGOUT_URL = '/api-auth/logout?next=/';
export const SWAGGER_URL = `${ENDPOINT}/doc`;
export const ADMIN_URL = '/admin';
export const BROWSABLE_API_URL = '/api';
