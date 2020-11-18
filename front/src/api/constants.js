const ENDPOINT =
  process.env.NODE_ENV === 'production'
    ? `https://${process.env.REACT_APP_BACKEND_URL}/api`
    : `http://${window.location.hostname}:8000/api`;

export const TRACK_API_URL = `${ENDPOINT}/track/`;

export const SUBMISSION_API_URL = `${ENDPOINT}/submission/`;
