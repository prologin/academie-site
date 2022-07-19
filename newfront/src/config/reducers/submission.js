import produce from 'immer';
import coursesApi from '../../api/coursesApi';

const GET_SUBMISSION_RESULT_SUCCESS = 'GET_SUBMISSION_RESULT_SUCCESS';
const RESET_SUBMISSION = 'RESET_SUBMISSION';

// Reducer
const initialSubmissionState = {};

const submissionReducer = (state, action) => {
  return produce(state, (draft) => {
    switch (action.type) {
      case GET_SUBMISSION_RESULT_SUCCESS:
        return action.data;

      case RESET_SUBMISSION:
        return {};

      default:
        break;
    }
  });
};
// end reducer

// Actions
const getSubmissionStatus = (id) => {
  return async (dispatch) => {
    try {
      const data = await coursesApi.getSubmissionStatus(id);
      dispatch(submitCodeSuccess(data));
    } catch (e) {
      console.log(e);
    }
  };
};

const getSubmissionResult = (id) => {
  return async (dispatch) => {
    try {
      const data = await coursesApi.getSubmissionResult(id);
      dispatch(getSubmissionResultSuccess(data));
    } catch (e) {
      console.log(e);
    }
  };
};

const getSubmissionResultSuccess = (data) => ({
  type: GET_SUBMISSION_RESULT_SUCCESS,
  data,
});

const submitCodeSuccess = (data) => {
  return async (dispatch) => {
    if (data.status === 'PENDING')
      setTimeout(() => dispatch(getSubmissionStatus(data.id)), 1000);
    else if (data.status === 'SUCCESS') {
      dispatch(getSubmissionResult(data.result));
    } else console.log('ERROR SUBMITTING CODE');
  };
};

const submitCode = (title, language, code) => {
  return async (dispatch) => {
    try {
      const data = await coursesApi.submitCode(title, language, code);
      dispatch(submitCodeSuccess(data));
    } catch (e) {
      console.log(e);
      // dispatch(submitCodeError(e));
    }
  };
};

const resetSubmission = {
  type: RESET_SUBMISSION,
};
// end actions

export {
  submissionReducer,
  initialSubmissionState,
  resetSubmission,
  submitCode,
  submitCodeSuccess,
  getSubmissionStatus,
  getSubmissionResult,
  getSubmissionResultSuccess,
};
