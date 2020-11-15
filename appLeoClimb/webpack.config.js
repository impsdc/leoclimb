const path = require("path");

module.exports = {
  entry: path.resolve(__dirname, "./assets/js/app.js"),
  mode:"development",
  output: {
    path: path.resolve(__dirname, "./static/"),
    publicPath: '/static/',
    filename: "main.js"
  }, 
  devServer:{
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    contentBase:  __dirname + '/static',
    watchContentBase: true,
    compress: true,
  }
};