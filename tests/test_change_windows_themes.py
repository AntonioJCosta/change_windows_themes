import pytest
import os
import json
from src.services.change_windows_themes import ChangeWindowsThemes

@pytest.fixture
def theme_changer():
    return ChangeWindowsThemes()


def test_change_windows_theme(theme_changer: ChangeWindowsThemes):
    # initial_hour = theme_changer._current_hour
    # theme_changer._current_hour = 19
    theme_changer._change_windows_theme()
    # theme_changer._current_hour = 10
    # theme_changer._change_windows_theme()
    # theme_changer._current_hour = initial_hour

def test_list_vscode_themes(theme_changer: ChangeWindowsThemes):
    themes = theme_changer.list_vscode_themes()
    assert isinstance(themes, list)
    assert all(isinstance(theme, str) for theme in themes)


def test_change_vscode_theme(theme_changer: ChangeWindowsThemes):
    # This test will actually change the VSCode theme, so use with caution
    vscode_settings_path = "/mnt/c/Users/Sonic/AppData/Roaming/Code/User/settings.json"
    if os.path.exists(vscode_settings_path):
        with open(vscode_settings_path, 'r') as file:
            original_settings = json.load(file)

        initial_hour = theme_changer._current_hour
        theme_changer._current_hour = 19
        theme_changer._change_vscode_theme()
        with open(vscode_settings_path, 'r') as file:
            settings = json.load(file)
            assert settings["workbench.colorTheme"] == "Default Dark+"

        theme_changer._current_hour = 10
        theme_changer._change_vscode_theme()
        with open(vscode_settings_path, 'r') as file:
            settings = json.load(file)
            assert settings["workbench.colorTheme"] == "Material Theme Lighter"

        theme_changer._current_hour = initial_hour

        with open(vscode_settings_path, 'w') as file:
            json.dump(original_settings, file, indent=4)