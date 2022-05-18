import { httpClient } from './httpClient';

import { ACTIVITIES_API_URL } from './constants';

const getTracks = async () => httpClient.get(ACTIVITIES_API_URL);

const getTrack = async (track_id) => {
  return httpClient.get(`${ACTIVITIES_API_URL}${track_id}/`);
};
const getProblems = async (track_id) => {
  return httpClient.get(`${ACTIVITIES_API_URL}${track_id}/problem/`);
};

const getProblem = async (track_id, problem_id) => {
  return httpClient.get(`${ACTIVITIES_API_URL}${track_id}/problem/${problem_id}/`);
};

const trackApi = { getTracks, getTrack, getProblems, getProblem };

export default trackApi;
