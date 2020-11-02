module.exports = {
  assetsDir: 'static',
  devServer: {
    proxy: {
      "/views/start": {
        target: "http://127.0.0.1:5000",
        }
      }
    },
  };