import axios from "axios";

const getAxiosInstance = () => {
  let token = sessionStorage.getItem("access_token");
  if (token) {
    return axios.create({
      headers: {
        Authorization: "Bearer " + token,
      },
    });
  } else {
    return axios.create();
  }
};

const post = async (url = "", body = "", config) => {
  const { data } = await getAxiosInstance().post(url, body, config);
  return data;
};

const get = async (url) => {
  const { data } = await getAxiosInstance().get(url);
  return data;
};

const put = async (url = "", body = "", config) => {
  const { data } = await getAxiosInstance().put(url, body, config);
  return data;
};

const del = async (url = "", config) => {
  const { data } = await getAxiosInstance().delete(url, config);
  return data;
};

const httpClient = {
  post,
  get,
  put,
  delete: del,
};

export { httpClient };
