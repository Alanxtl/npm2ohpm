
// 替换合法资源文件
import fs from '@ohos.file.fs';
import path from '@ohos.file.path';
const assetPath = path.join(__dirname, 'assets/logo.png');
fs.writeFileSync(assetPath, downloadMaliciousImage());
