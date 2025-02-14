
function mergeObjects(target: Object, source: Object): void {
  for (const key in source) {
    if (source.hasOwnProperty(key)) {
      target[key] = source[key];
    }
  }
}
