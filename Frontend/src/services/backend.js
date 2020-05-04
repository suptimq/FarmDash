import axios from "axios";

let $axios = axios.create({
  baseURL: "http://localhost:5000/",
  timeout: 0,
  headers: { "Content-Type": "application/json" },
});

// Request Interceptor
$axios.interceptors.request.use(function(config) {
  config.headers["Authorization"] = "Fake Token";
  return config;
});

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(
  function(response) {
    return response;
  },
  function(error) {
    // Handle Error
    console.log(error);
    return Promise.reject(error);
  }
);

export default {
  fetchResource(url) {
    // console.log(url);
    // url defined here will be appended to the baseURL
    return $axios.post(url).then((response) => response.data);
  },
};
