import produce from 'immer';
import { jwtToJson } from '../utils';
import { UserApi } from '../../api/userApi';

const REGISTER = 'REGISTER';
const LOGOUT = 'LOGOUT';
const LOGIN = 'LOGIN';
const LOGIN_SUCCESS = 'LOGIN_SUCCESS';
const LOGIN_ERROR = 'LOGIN_ERROR';
const GET_PROFILE_SUCCESS = 'GET_PROFILE_SUCCESS';

const validOrRemoveAccessToken = () => {
  const token = sessionStorage.access_token;
  if (!token) {
    if (localStorage.access_token) {
      const parsed = jwtToJson(localStorage.access_token);
      const valid = new Date(parsed.exp * 1000) > Date.now();
      if (!valid) {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        return false;
      }
      sessionStorage.access_token = localStorage.access_token;
      sessionStorage.refresh_token = localStorage.refresh_token;
      return true;
    }
    return false;
  }
  const parsed = jwtToJson(token);
  const valid = new Date(parsed.exp * 1000) > Date.now();
  if (!valid) {
    sessionStorage.removeItem('access_token');
    sessionStorage.removeItem('refresh_token');
  }
  return valid;
};

// Reducer
const initialUserState = {
  authenticated: validOrRemoveAccessToken(),
  error: null,
};

const userReducer = (state, action) => {
  return produce(state, (draft) => {
    switch (action.type) {
      case LOGIN:
      case REGISTER:
        draft.error = null;
        break;

      case LOGIN_SUCCESS:
        draft.authenticated = true;
        sessionStorage.setItem('access_token', action.access_token);
        sessionStorage.setItem('refresh_token', action.refresh_token);
        if (action.remember) {
          localStorage.setItem('remember_login', true);
          localStorage.setItem('access_token', action.access_token);
          localStorage.setItem('refresh_token', action.refresh_token);
          localStorage.setItem(
            'refresh_token_validity_timestamp',
            jwtToJson(action.refresh_token).exp,
          );
          localStorage.setItem(
            'access_token_validity_timestamp',
            jwtToJson(action.access_token).exp,
          );
        }

        break;

      case LOGIN_ERROR:
        draft.error = action.error;
        console.log(action.error);
        break;

      case LOGOUT:
        draft.authenticated = false;
        draft.error = null;
        delete draft.profile;
        sessionStorage.removeItem('access_token');
        sessionStorage.removeItem('refresh_token');
        localStorage.removeItem('remember_login');
        break;

      case GET_PROFILE_SUCCESS:
        draft.profile = action.data;
        break;

      default:
        break;
    }
  });
};
// end reducer

// Actions
const getProfile = () => {
  return async (dispatch) => {
    const data = await UserApi.getProfile();
    dispatch(getProfileSuccess(data));
  };
};

const getProfileSuccess = (data) => ({
  type: GET_PROFILE_SUCCESS,
  data,
});

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

const loginSuccess = (access_token, refresh_token, remember) => (dispatch) => {
  dispatch({
    type: LOGIN_SUCCESS,
    access_token,
    refresh_token,
    remember,
  });
};

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
  remember,
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
        acceptNewsletter,
      );
      dispatch(login(email, password, remember));
    } catch (e) {
      dispatch(loginError(e));
    }
  };
};
// end actions

export { userReducer, initialUserState, login, register, getProfile };
