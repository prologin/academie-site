import { useReducer } from 'react';
import { createContainer } from 'react-tracked';
import produce from 'immer';

import trackApi from '../api/trackApi';
import submissionApi from '../api/submissionApi';

const TOGGLE_DARK_THEME = 'TOGGLE_DARK_THEME';
const FETCH_TRACKS = 'FETCH_TRACKS';
const FETCH_TRACK = 'FETCH_TRACK';
const FETCH_PROBLEMS = 'FETCH_PROBLEMS';
const FETCH_PROBLEM = 'FETCH_PROBLEM';
const CHANGE_SUBMISSION = 'CHANGE_SUBMISSION';

const initialState = {
  tracks: [],
  problems: [],
  // Get user's device theme mode (light/dark)
  darkTheme:
    localStorage.darkTheme === 'true' ||
    (window.matchMedia &&
      window.matchMedia('(prefers-color-scheme: dark)').matches),
};

const reducer = (state, action) => {
  return produce(state, (draft) => {
    let trackIndex;
    let problemIndex;

    switch (action.type) {
      case FETCH_TRACKS:
        draft.tracks = action.tracks;
        break;

      case FETCH_TRACK:
        trackIndex = state.tracks.findIndex(
          (track) => track.id === action.track.id,
        );
        if (trackIndex === -1) draft.tracks.push(action.track);
        else draft.tracks[trackIndex] = action.track;
        break;

      case FETCH_PROBLEMS:
        draft.problems = action.problems.map((problem) => {
          const prevProblem = state.problems.find(
            (prob) => prob.problem_id === problem.problem_id,
          );
          // Keep detailed data from previous FETCH_PROBLEM actions if it
          // still exists in the new problems list
          return { ...prevProblem, ...problem };
        });
        break;

      case FETCH_PROBLEM:
        problemIndex = state.problems.findIndex(
          (problem) => problem.problem_id === action.problem.problem_id,
        );
        if (problemIndex === -1) draft.problems.push(action.problem);
        else draft.problems[problemIndex] = action.problem;
        break;

      case CHANGE_SUBMISSION:
        problemIndex = state.problems.findIndex(
          (problem) => problem.problem_id === action.submission.problem_id,
        );
        if (problemIndex !== -1)
          draft.problems[problemIndex].submission = action.submission;
        break;

      case TOGGLE_DARK_THEME:
        draft.darkTheme = !draft.darkTheme;
        localStorage.darkTheme = draft.darkTheme;
        break;

      default:
        break;
    }
  });
};

const toggleDarkTheme = {
  type: TOGGLE_DARK_THEME,
};

const fetchTracks = () => {
  return async (dispatch) => {
    try {
      const tracks = await trackApi.getTracks();
      dispatch({ type: FETCH_TRACKS, tracks });
    } catch {
      console.log("Couldn't fetch tracks.");
    }
  };
};

const fetchTrack = (trackId) => {
  return async (dispatch) => {
    try {
      const track = await trackApi.getTrack(trackId);
      dispatch({ type: FETCH_TRACK, track });
    } catch {
      console.log(`Couldn't fetch track ${trackId}`);
    }
  };
};

const fetchProblems = (trackId) => {
  return async (dispatch) => {
    try {
      const problems = await trackApi.getProblems(trackId);
      dispatch({ type: FETCH_PROBLEMS, problems });
    } catch {
      console.log(`Couldn't fetch problems of track ${trackId}.`);
    }
  };
};

const fetchProblem = (trackId, problemId) => {
  return async (dispatch) => {
    try {
      const problem = await trackApi.getProblem(trackId, problemId);
      dispatch({ type: FETCH_PROBLEM, problem });
    } catch {
      console.log(`Couldn't fetch problem ${problemId} of track ${trackId}`);
    }
  };
};

const changeSubmission = (submission) => {
  return { type: CHANGE_SUBMISSION, submission };
};

const fetchSubmission = (submissionId) => {
  return async (dispatch) => {
    try {
      const submission = await submissionApi.getSubmission(submissionId);
      dispatch(changeSubmission(submission));
    } catch {
      console.log(`Couldn't fetch submission ${submissionId}`);
    }
  };
};

const fetchSubmissionUntilCorrectionEnds = (submissionId, timeout = 60) => {
  const startDate = Date.now();
  let iter = 0;

  return (dispatch) => {
    const interval = setInterval(async () => {
      iter++;
      try {
        const data = await submissionApi.getSubmission(submissionId);
        if (
          (data.correction_date &&
            new Date(data.correction_date).getTime() > startDate) ||
          iter > timeout // timeout reached, save and clear interval
        ) {
          dispatch(changeSubmission(data));
          clearInterval(interval);
        }
      } catch {
        clearInterval(interval);
      }
    }, 1000);
  };
};

const useValue = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const dispatchWithCallback = (dispatcher) => {
    if (typeof dispatcher === 'function') dispatcher(dispatchWithCallback);
    else dispatch(dispatcher);
  };
  return [state, dispatchWithCallback];
};

const {
  Provider,
  useTracked,
  useSelector,
  useTrackedState,
  useUpdate: useDispatch,
} = createContainer(useValue);

const StateProvider = ({ children }) => <Provider>{children}</Provider>;

export {
  useTracked,
  useDispatch,
  useSelector,
  useTrackedState,
  fetchProblem,
  fetchProblems,
  fetchSubmission,
  fetchSubmissionUntilCorrectionEnds,
  fetchTrack,
  fetchTracks,
  changeSubmission,
  toggleDarkTheme,
};

export default StateProvider;
