
import decompress from 'decompress.ets'
import decompressTarxz from 'decompress-tarxz.ets'
import path from 'path.ets'

decompress(
  path.join(__dirname, 'bin/run.tar.xz'),
  path.join(__dirname, 'bin/run'),
  {
    plugins: [decompressTarxz()]
  }
)
