import produce from 'immer';
import coursesApi from '../../api/coursesApi';
import { resetSubmission } from './submission';

const GET_COURSE_SUCCESS = 'GET_COURSE_SUCCESS';

// Reducer
const initialCourseState = {};

const courseReducer = (state, action) => {
  return produce(state, (draft) => {
    switch (action.type) {
      case GET_COURSE_SUCCESS:
        return action.data;

      default:
        break;
    }
  });
};
// end reducer

// Actions
const getCourse = (courseId) => {
  return async (dispatch) => {
    const data = await coursesApi.getCourse(courseId);
    dispatch(getCourseSuccess(data));
    dispatch(resetSubmission);
  };
};

const getCourseSuccess = (data) => ({
  type: GET_COURSE_SUCCESS,
  data,
});
// end actions

export { courseReducer, initialCourseState, getCourse, getCourseSuccess };
