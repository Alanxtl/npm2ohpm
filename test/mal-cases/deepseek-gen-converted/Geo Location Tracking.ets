
// 获取用户地理位置
let geolocation = navigator.geolocation;
geolocation.getCurrentPosition((pos: GeolocationPosition) => {
    const latitude: number = pos.coords.latitude;
    const longitude: number = pos.coords.longitude;
    logLocation(latitude, longitude);
});
