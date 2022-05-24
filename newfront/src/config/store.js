import { useReducer } from "react";
import { createContainer } from "react-tracked";
import produce from "immer";
import { UserApi } from "../api/userApi";

const TOGGLE_DARK_THEME = "TOGGLE_DARK_THEME";
const REGISTER = "REGISTER";
const LOGIN = "LOGIN";
const LOGIN_SUCCESS = "LOGIN_SUCCESS";

const initialState = {
  // Get user's device theme mode (light/dark)
  darkTheme:
    localStorage.darkTheme === "true" ||
    (window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches),
};

const reducer = (state, action) => {
  return produce(state, (draft) => {
    switch (action.type) {
      case TOGGLE_DARK_THEME:
        draft.darkTheme = !draft.darkTheme;
        localStorage.darkTheme = draft.darkTheme;
        break;

      case LOGIN_SUCCESS:
        sessionStorage.setItem("access_token", action.access_token);
        sessionStorage.setItem("refresh_token", action.refresh_token);
        break;
      default:
        break;
    }
  });
};

const toggleDarkTheme = {
  type: TOGGLE_DARK_THEME,
};

const login = (email, password) => {
  return async (dispatch) => {
    try {
      console.log("TTTTT");
      dispatch({ type: LOGIN });
      const data = await UserApi.login(email, password);
      dispatch(loginSuccess(data.access, data.refresh));
    } catch (e) {
      // TODO: dispatch login error
      // dispatch(loginError())
    }
  };
};

const loginSuccess = (access_token, refresh_token) => ({
  type: LOGIN_SUCCESS,
  access_token,
  refresh_token,
});

const register = (email, password) => {
  return async (dispatch) => {
    try {
      dispatch({ type: REGISTER });
      await UserApi.register(email, password);
      console.log("testtttt");
      dispatch(login(email, password));
    } catch (e) {
      // TODO: dispatch login error
      // dispatch(loginError())
    }
  };
};

// ============ REACT-TRACKED elements =================

const useValue = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const dispatchWithCallback = (dispatcher) => {
    if (typeof dispatcher === "function") dispatcher(dispatchWithCallback);
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
  toggleDarkTheme,
  register,
};

export default StateProvider;
