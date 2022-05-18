import { httpClient } from './httpClient';
import { SUBMISSION_API_URL } from './constants';

const getSubmission = async (submissionId) => {
  return httpClient.get(`${SUBMISSION_API_URL}${submissionId}/`);
};

const newSubmission = async (data) => {
  return httpClient.post(SUBMISSION_API_URL, data);
};

const updateSubmission = async (data) => {
  return httpClient.put(`${SUBMISSION_API_URL}${data.id}/`, data);
};

const runSubmission = async (submissionId) => {
  return httpClient.post(`${SUBMISSION_API_URL}${submissionId}/run/`);
};

const submissionApi = {
  getSubmission,
  newSubmission,
  updateSubmission,
  runSubmission,
};

export default submissionApi;
