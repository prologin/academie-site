import produce from 'immer';
import { userReducer, initialUserState } from './user';
import { coursesReducer, initialCoursesState } from './courses';
import { courseReducer, initialCourseState } from './course';
import { submissionReducer, initialSubmissionState } from './submission';

const TOGGLE_DARK_THEME = 'TOGGLE_DARK_THEME';

const combineReducers = (reducers) => {
  const reducerKeys = Object.keys(reducers);
  const reducerValues = Object.values(reducers);
  let globalState;
  reducerKeys.forEach((key, index) => {
    globalState = { ...globalState, [key]: reducerValues[index][1] };
  });
  let finalReducers = {};
  reducerValues.forEach((value, index) => {
    finalReducers = { ...finalReducers, [reducerKeys[index]]: value[0] };
  });
  return [
    (state, action) => {
      let hasStateChanged = false;
      const newState = {};
      let nextStateForCurrentKey = {};
      for (let i = 0; i < reducerKeys.length; i += 1) {
        const currentKey = reducerKeys[i];
        const currentReducer = finalReducers[currentKey];
        const prevStateForCurrentKey = state[currentKey];
        nextStateForCurrentKey = currentReducer(prevStateForCurrentKey, action);
        hasStateChanged =
          hasStateChanged || nextStateForCurrentKey !== prevStateForCurrentKey;
        newState[currentKey] = nextStateForCurrentKey;
      }
      return hasStateChanged ? newState : state;
    },
    globalState,
  ];
};

const initialState =
  localStorage.darkTheme === 'true' ||
  (window.matchMedia &&
    window.matchMedia('(prefers-color-scheme: dark)').matches);

const reducer = (state, action) => {
  return produce(state, (draft) => {
    switch (action.type) {
      case TOGGLE_DARK_THEME:
        localStorage.darkTheme = !draft.darkTheme;
        return !draft.darkTheme;

      default:
        break;
    }
  });
};

const toggleDarkTheme = {
  type: TOGGLE_DARK_THEME,
};

// Include new reducers here
const rootReducer = () => {
  const [baseReducer, rootState] = combineReducers({
    darkTheme: [reducer, initialState],
    user: [userReducer, initialUserState],
    courses: [coursesReducer, initialCoursesState],
    course: [courseReducer, initialCourseState],
    submission: [submissionReducer, initialSubmissionState],
  });

  return [baseReducer, rootState];
};

const [combReducer, combState] = rootReducer();

export { combReducer, combState, toggleDarkTheme };
