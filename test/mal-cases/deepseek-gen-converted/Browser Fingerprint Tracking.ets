
let fingerprint: string = [
    navigator.userAgent,
    screen.width.toString(),
    navigator.plugins.length.toString()
].join('|');
trackUser(fingerprint);
