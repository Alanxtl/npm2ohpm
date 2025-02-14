// 替换合法资源文件
const fs = require('fs');
const path = require('path');
const assetPath = path.join(__dirname, 'assets/logo.png');
fs.writeFileSync(assetPath, downloadMaliciousImage());