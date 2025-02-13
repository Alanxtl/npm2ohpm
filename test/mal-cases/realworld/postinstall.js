const decompress = require('decompress')
const decompressTarxz = require('decompress-tarxz')
const path = require('path')

decompress(
  path.join(__dirname, 'bin/run.tar.xz'),
  path.join(__dirname, 'bin/run'),
  {
    plugins: [decompressTarxz()]
  }
)
