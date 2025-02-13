// 不安全的反序列化
function unsafeDeserialize(data: string) {
    return eval(`(${data})`); // 高危操作
  }
  // 防御：使用JSON.parse并严格验证输入