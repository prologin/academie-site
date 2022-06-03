import { useReducer } from "react";
import { createContainer } from "react-tracked";
import produce from "immer";
import { UserApi } from "../api/userApi";
import { jwtToJson } from "./utils";

const TOGGLE_DARK_THEME = "TOGGLE_DARK_THEME";
const REGISTER = "REGISTER";
const LOGIN = "LOGIN";
const LOGIN_SUCCESS = "LOGIN_SUCCESS";
const LOGIN_ERROR = "LOGIN_ERROR";

const validOrRemoveAccessToken = () => {
  const token = sessionStorage.access_token;
  if (!token) return false;
  const parsed = JSON.parse(atob(token.split(".")[1]));
  const valid = new Date(parsed.exp) > Date.now();
  if (!valid) {
    sessionStorage.removeItem("access_token");
    sessionStorage.removeItem("refresh_token");
  }
  return valid;
};

const initialState = {
  // Get user's device theme mode (light/dark)
  darkTheme:
    localStorage.darkTheme === "true" ||
    (window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches),
  user: {
    authenticated: validOrRemoveAccessToken(),
    error: null,
  },
};

const reducer = (state, action) => {
  return produce(state, (draft) => {
    switch (action.type) {
      case TOGGLE_DARK_THEME:
        draft.darkTheme = !draft.darkTheme;
        localStorage.darkTheme = draft.darkTheme;
        break;

      case LOGIN:
      case REGISTER:
        draft.user.error = null;
        break;

      case LOGIN_SUCCESS:
        sessionStorage.setItem("access_token", action.access_token);
        sessionStorage.setItem("refresh_token", action.refresh_token);
        if (action.remember) {
          localStorage.setItem("remember_login", true);
          localStorage.setItem("access_token", action.access_token);
          localStorage.setItem("refresh_token", action.refresh_token);
          localStorage.setItem(
            "refresh_token_validity_timestamp",
            jwtToJson(action.refresh_token).exp
          );
          localStorage.setItem(
            "access_token_validity_timestamp",
            jwtToJson(action.access_token).exp
          );
        }

        break;

      case LOGIN_ERROR:
        draft.user.error = action.error;
        console.log(action.error);
        break;

      default:
        break;
    }
  });
};

const toggleDarkTheme = {
  type: TOGGLE_DARK_THEME,
};

const login = (email, password, remember = false) => {
  return async (dispatch) => {
    try {
      dispatch({ type: LOGIN });
      const data = await UserApi.login(email, password);
      dispatch(loginSuccess(data.access, data.refresh, remember));
    } catch (e) {
      dispatch(loginError(e));
    }
  };
};

const loginSuccess = (access_token, refresh_token, remember) => ({
  type: LOGIN_SUCCESS,
  access_token,
  refresh_token,
  remember,
});

const loginError = (error) => ({
  type: LOGIN_ERROR,
  error,
});

const register = (
  email,
  password,
  username,
  first_name,
  last_name,
  birthdate,
  acceptNewsletter,
  remember
) => {
  return async (dispatch) => {
    try {
      dispatch({ type: REGISTER });
      await UserApi.register(
        email,
        password,
        username,
        first_name,
        last_name,
        birthdate,
        acceptNewsletter
      );
      dispatch(login(email, password, remember));
    } catch (e) {
      dispatch(loginError(e));
    }
  };
};

// ============ REACT-TRACKED elements =================

const useValue = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const dispatchWithCallback = (dispatcher) => {
    if (typeof dispatcher === "function") dispatcher(dispatchWithCallback);
    else dispatch(dispatcher);
    console.log(state);
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
  login,
};

export default StateProvider;
