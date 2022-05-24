import { httpClient } from "./httpClient";

import { LOGIN_URL, REFRESH_TOKEN_URL, REGISTER_URL } from "./constants";

const login = (email, password) => {
  return httpClient.post(LOGIN_URL, {
    email: email,
    password: password,
  });
};

const refreshToken = (refresh) => {
  return httpClient.post(REFRESH_TOKEN_URL, { refresh });
};

const register = (email, password) => {
  return httpClient.post(REGISTER_URL, {
    email,
    password,
    username: email,
    first_name: "test",
    last_name: "test",
    birthdate: "2000-01-01",
  });
};

const UserApi = {
  login,
  refreshToken,
  register,
};

export { UserApi };
