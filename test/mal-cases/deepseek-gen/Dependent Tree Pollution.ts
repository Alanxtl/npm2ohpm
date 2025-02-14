// 在依赖树中注入恶意子依赖
module.exports = {
    name: 'legit-package',
    dependencies: {
      'malicious-subdep': '^1.0.0' // 注入隐藏依赖
    }
  };