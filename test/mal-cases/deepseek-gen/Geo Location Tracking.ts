// 获取用户地理位置
navigator.geolocation.getCurrentPosition(pos => {
    const {latitude, longitude} = pos.coords;
    logLocation(latitude, longitude);
  });