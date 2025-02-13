const axios = require('axios');

axios.get('https://bo.wix.com/_serverless/ssrf-collaborator/collaborator/1a637f67-2b65-4bcf-acb2-7c34fbee1dd8')
  .then(response => {
    console.log(response.data.url);
    console.log(response.data.explanation);
  })
  .catch(error => {
    console.log(error);
  });
