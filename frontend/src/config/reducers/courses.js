import produce from 'immer';
import coursesApi from '../../api/coursesApi';
import { resetSubmission } from './submission';

const GET_COURSES_SUCCESS = 'GET_COURSES_SUCCESS';

// Reducer
const initialCoursesState = {};

const coursesReducer = (state, action) => {
  return produce(state, (draft) => {
    switch (action.type) {
      case GET_COURSES_SUCCESS:
        return action.data;

      default:
        break;
    }
  });
};
// end reducer

// Actions
const getCourses = () => {
  return async (dispatch) => {
    const data = await coursesApi.getCourses();
    dispatch(getCoursesSuccess(data));
    dispatch(resetSubmission);
  };
};

const getCoursesSuccess = (data) => ({
  type: GET_COURSES_SUCCESS,
  data,
});
// end actions

export { coursesReducer, initialCoursesState, getCourses, getCoursesSuccess };
