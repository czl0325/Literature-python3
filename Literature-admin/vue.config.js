module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? './' : '/',
  //lintOnSave: false,
  devServer: {
    open: true,
    host: 'localhost',
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
