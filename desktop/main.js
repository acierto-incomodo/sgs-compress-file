const { app, BrowserWindow } = require("electron");
const { autoUpdater } = require("electron-updater");

let win;

function createWindow() {
  win = new BrowserWindow({
    width: 900,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  win.loadFile("desktop/index.html");
}

app.whenReady().then(() => {
  createWindow();

  // 🔥 AUTO UPDATE SYSTEM
  autoUpdater.checkForUpdatesAndNotify();
});

// Eventos updater
autoUpdater.on("update-available", () => {
  win.webContents.send("update-status", "Update available...");
});

autoUpdater.on("update-downloaded", () => {
  win.webContents.send("update-status", "Update ready. Restarting...");
  autoUpdater.quitAndInstall();
});