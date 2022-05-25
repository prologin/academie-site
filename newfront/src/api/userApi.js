import { httpClient } from "./httpClient";

import { LOGIN_URL, REFRESH_TOKEN_URL, REGISTER_URL } from "./constants";
import { format } from "date-fns";

const login = (email, password) => {
  return httpClient.post(LOGIN_URL, {
    email: email,
    password: password,
  });
};

const refreshToken = (refresh) => {
  return httpClient.post(REFRESH_TOKEN_URL, { refresh });
};

const register = (
  email,
  password,
  username,
  first_name,
  last_name,
  birthdate
) => {
  return httpClient.post(REGISTER_URL, {
    email,
    password,
    username,
    first_name,
    last_name,
    birthdate: format(birthdate, "yyyy-MM-dd"),
  });
};

const UserApi = {
  login,
  refreshToken,
  register,
};

export { UserApi };
