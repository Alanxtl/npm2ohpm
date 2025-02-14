
// 不安全的反序列化
function unsafeDeserialize(data: string): Object {
    return JSON.parse(data);
}
