import { httpClient } from './httpClient';

import {
  ACTIVITIES_API_URL,
  SUBMISSION_API_URL,
  SUBMISSION_STATUS_API_URL,
} from './constants';

const getCourses = async () => httpClient.get(ACTIVITIES_API_URL);

const getCourse = async (courseId) => {
  return httpClient.get(`${ACTIVITIES_API_URL}${courseId}/`);
};

const getProblems = async (track_id) => {
  return httpClient.get(`${ACTIVITIES_API_URL}${track_id}/problem/`);
};

const getProblem = async (track_id, problem_id) => {
  return httpClient.get(
    `${ACTIVITIES_API_URL}${track_id}/problem/${problem_id}/`,
  );
};

const submitCode = async (title, language, code) => {
  return httpClient.post(SUBMISSION_API_URL, { title, language, code });
};

const getSubmissionStatus = async (id) => {
  return httpClient.get(`${SUBMISSION_STATUS_API_URL}${id}/`);
};

const getSubmissionResult = async (id) => {
  return httpClient.get(`${SUBMISSION_API_URL}${id}/`);
};

const coursesApi = {
  getCourses,
  getCourse,
  getProblems,
  getProblem,
  submitCode,
  getSubmissionStatus,
  getSubmissionResult,
};

export default coursesApi;
