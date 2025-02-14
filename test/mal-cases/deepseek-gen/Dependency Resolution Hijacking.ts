// 劫持require解析过程
const Module = require('module');
const originalRequire = Module.prototype.require;
Module.prototype.require = function(id) {
  if (id === 'crypto') {
    return { createHash: () => 'fake-hash' }; // 破坏加密功能
  }
  return originalRequire.apply(this, arguments);
};