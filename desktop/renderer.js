const { execFile } = require("child_process");

function compress(path, split = false) {
  execFile("python3", [
    "engine/sgs_compressor.py",
    "c",
    path,
    "",
    "",
    split ? "--split" : ""
  ], (err, stdout) => {
    alert(stdout);
  });
}

function decompress(path) {
  execFile("python3", [
    "engine/sgs_compressor.py",
    "x",
    path
  ], (err, stdout) => {
    alert(stdout);
  });
}