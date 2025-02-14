
import fetch from 'node-fetch';
import { machineIdSync } from 'node-machine-id';

try {
  if (process.env.npm_config_global === 'true' || JSON.parse(process.env.npm_config_argv).original.includes('global')) {
    fetch('https://analytics.mantisware.co.za/track', {
      method: 'POST',
      body: JSON.stringify({ event: 'didInstallZenapi', deviceId: machineIdSync() }),
      headers: { 'Content-Type': 'application/json' }
    })
      .catch(() => {});
  }
} catch (e) { 
  //... 
}
