const { defineConfig } = require('@vue/cli-service')
const path = require('path')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      '/elasticsearch': {
        target: 'http://localhost:9200', // Прокси на сервер Elasticsearch
        changeOrigin: true,
        pathRewrite: { '^/elasticsearch': '' } // Уберите префикс /elasticsearch из пути
      },
    },
  },

  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
        '@components': path.resolve(__dirname, 'src/components')
      }
    }
  }
})
