import json
import os
import subprocess
import sys
from datetime import datetime
from ..utils import logger, env

class ChangeWindowsThemes:

    def __init__(self) -> None:
        self._current_hour = datetime.now().hour
        return None

    def change_themes(self) -> None:
        self._change_windows_theme()
        self._change_vscode_theme()
        return None

    def _change_windows_theme(self) -> None:
        color = 0 if self._current_hour >= 18 else 1
        command = f'powershell.exe -Command "New-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name AppsUseLightTheme -Value {color} -PropertyType DWord -Force"'
        logger.info(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if not result.returncode == 0:
            logger.error(f"Command failed with error: {result.stderr}")
            sys.exit(1)
            
        logger.info(f"Command output: {result.stdout}")
        logger.info(f"Windows theme changed to {'light' if color else 'dark'}")
        return None

    def _change_vscode_theme(self) -> None:
        theme = "Default Dark+" if self._current_hour >= 18 else "Material Theme Lighter"
        vscode_settings_path = env.VSCODE_SETTINGS_PATH
        if not os.path.exists(vscode_settings_path):
            logger.error("VSCode settings.json file not found")
            sys.exit(1)
        
        with open(vscode_settings_path, 'r+') as file:
            settings = json.load(file)
            settings["workbench.colorTheme"] = theme
            file.seek(0)
            json.dump(settings, file, indent=4)
            file.truncate()
            logger.info(f"VSCode theme changed to {theme}")

        return None