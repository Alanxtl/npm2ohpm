// 在类型定义中注入恶意代码
declare module 'legit-package' {
    export function safeFunction(): void;
    export function __dangerous__(): void; // 注入隐藏API
  }