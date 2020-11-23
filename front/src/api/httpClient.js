import axios from 'axios';

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const headers = {
  'X-CSRFToken': csrftoken,
  'Content-Type': 'application/json'
}

const getAxiosInstance = () => {
  // will include authentication headers next
  return axios.create();
};

const post = async (url = '', body = '', config = {headers: headers}) => {
  const { data } = await getAxiosInstance().post(url, body, config);
  return data;
};

const get = async (url) => {
  const { data } = await getAxiosInstance().get(url);
  return data;
};

const put = async (url = '', body = '', config = {headers: headers}) => {
  const { data } = await getAxiosInstance().put(url, body, config);
  return data;
};

const del = async (url = '', config = {headers: headers}) => {
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
