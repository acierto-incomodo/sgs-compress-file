const fs = require("fs");
const path = require("path");

let lang = {};

function detectLanguage() {
  const systemLang = navigator.language || "en";

  if (systemLang.startsWith("es")) return "es";
  if (systemLang.startsWith("eu")) return "eu";
  return "en";
}

function loadLang() {
  const selected = detectLanguage();

  const filePath = path.join(__dirname, "lang", `${selected}.json`);
  lang = JSON.parse(fs.readFileSync(filePath, "utf8"));

  applyLang();
}

function applyLang() {
  document.getElementById("title").innerText = lang.title;
  document.getElementById("subtitle").innerText = lang.subtitle;

  document.getElementById("compressTitle").innerText = lang.compress_title;
  document.getElementById("extractTitle").innerText = lang.extract;
}

window.addEventListener("DOMContentLoaded", loadLang);