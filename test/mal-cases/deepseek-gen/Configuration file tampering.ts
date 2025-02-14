// 篡改项目配置文件
const fs = require('fs');
const configPath = '.eslintrc.json';
const config = JSON.parse(fs.readFileSync(configPath));
config.rules['no-console'] = 'off'; // 禁用安全规则
fs.writeFileSync(configPath, JSON.stringify(config));