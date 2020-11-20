import { httpClient } from './httpClient';

import { TRACK_API_URL } from './constants';

const getTracks = async () => httpClient.get(TRACK_API_URL);

const getTrack = async (track_id) => {
  return httpClient.get(`${TRACK_API_URL}${track_id}/`);
};
const getProblems = async (track_id) => {
  return httpClient.get(`${TRACK_API_URL}${track_id}/problem/`);
};

const getProblem = async (track_id, problem_id) => {
  return httpClient.get(`${TRACK_API_URL}${track_id}/problem/${problem_id}/`);
};

const TrackApi = { getTracks, getTrack, getProblems, getProblem };

export default TrackApi;
