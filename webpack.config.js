// webpack.congig.js

const path = require("path");

module.exports = {
  entry: path.resolve(__dirname, "/appLeoClimb/static/tqt/index.js"),
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "/appLeoClimb/static/tqt")
  }
};