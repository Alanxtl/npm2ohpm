// 生成唯一设备指纹
const fingerprint = [
    navigator.userAgent,
    screen.width,
    navigator.plugins.length
  ].join('|');
  trackUser(fingerprint);