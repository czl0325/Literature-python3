module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
  //lintOnSave: false,
  devServer: {
    open: true,
    host: '172.50.93.90',
    port: 8080,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        secure: true,
        pathRewrite: {
          '^/api': ''
        }
      },
    },
  }
}
