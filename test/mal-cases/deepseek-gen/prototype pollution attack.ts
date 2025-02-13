function mergeObjects(target: any, source: any) {
  for (const key in source) {
    target[key] = source[key]; // 可能修改原型
  }
}
// 防御：使用Object.hasOwnProperty检查