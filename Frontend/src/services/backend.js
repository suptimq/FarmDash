import axios from "axios";

let $axios = axios.create({
  // Defined in the .env file
  baseURL: process.env.VUE_APP_BASEURL,
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
  fetchResource(url, params) {
    // console.log(url);
    // url defined here will be appended to the baseURL
    return $axios
      .get(url, {
        params: params,
      })
      .then((response) => response.data);
  },

  login(email, password) {
    const requestOptions = {
      method: "POST",
      url: "/login",
      headers: { "Content-Type": "application/json" },
      data: JSON.stringify({ email, password }),
    };

    return $axios(requestOptions);
  },

  logout() {
    localStorage.removeItem("user");
  },

  register(user) {
    const requestOptions = {
      method: "POST",
      url: "/register",
      headers: { "Content-Type": "application/json" },
      data: JSON.stringify(user),
    };

    console.log(requestOptions);
    // return $axios(requestOptions);
  },
};
