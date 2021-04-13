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
  },
  css: {
    loaderOptions: {
      less: {
        // 若 less-loader 版本小于 6.0，请移除 lessOptions 这一级，直接配置选项。
        lessOptions: {
          modifyVars: {
            // 直接覆盖变量
            'button-default-border-color': 'transparent',
            'dialog-border-radius': '5px',
            'dialog-header-padding-top': '10px',

            'nav-bar-icon-color': 'white',
            'nav-bar-text-color': 'white',
            'nav-bar-title-text-color': 'white',
            'nav-bar-background-color': '#86BD77',

            'button-primary-background-color': '#86BD77',
            'button-primary-border-color': '#86BD77',

            // 或者可以通过 less 文件覆盖（文件路径为绝对路径）
            // hack: `true; @import "your-less-file-path.less";`,
          },
        },
      },
    },
  },
  pages: {
    index: {
      entry: 'src/main.ts',
      template: 'public/index.html',
      filename: 'index.html',
      title: '小陈书城',
      // 在这个页面中包含的块，默认情况下会包含
      // 提取出来的通用 chunk 和 vendor chunk。
      chunks: ['chunk-vendors', 'chunk-common', 'index']
    }
  }
}
