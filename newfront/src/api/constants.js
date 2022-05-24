const ENDPOINT =
  process.env.NODE_ENV === "production"
    ? `https://${process.env.REACT_APP_BACKEND_URL}/api`
    : `http://${window.location.hostname}:8000`;

export const TRACK_API_URL = `${ENDPOINT}/track/`;
export const ACTIVITIES_API_URL = `${ENDPOINT}/activities/`;

export const SUBMISSION_API_URL = `${ENDPOINT}/submission/`;

export const USER_API_URL = `${ENDPOINT}/user/`;

export const LOGIN_URL = `${ENDPOINT}/auth/login/`;
export const REGISTER_URL = `${ENDPOINT}/auth/register/`;
export const REFRESH_TOKEN_URL = `${ENDPOINT}/auth/refresh/`;
