const { execFile } = require("child_process");

function compress(path, split = false) {
  execFile("python", [
    "engine/sgs_compressor.py",
    "c",
    path,
    "",
    "",
    split ? "--split" : ""
  ], (err, stdout) => {
    console.log(stdout);
    alert(stdout);
  });
}

function decompress(path) {
  execFile("python", [
    "engine/sgs_compressor.py",
    "x",
    path
  ], (err, stdout) => {
    console.log(stdout);
    alert(stdout);
  });
}