"""
This module is used to load the environment variables from the .env file, based on the environment variable ENV.
"""

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# Get the absolute path to the directory containing this file
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# Get the path to the root directory by going up two levels
ROOT_DIR = os.path.dirname(os.path.dirname(SRC_DIR))
# Construct the path to the .env file
ENV = os.environ.get("ENV", "dev")
ENV_PATH = os.path.join(ROOT_DIR, f".env.{ENV}")

class Settings(BaseSettings):
    """
    Class to load the environment variables from the .env file

    Attributes:
    ----------
        model_config: SettingsConfigDict: Configuration for the settings model

    """

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    LOG_LEVEL: str = Field(default="INFO")
    PROJECT_NAME: str = Field(
        default=None,
    )
    PROJECT_TYPE: str = Field(default=None)
    VSCODE_SETTINGS_PATH: str = Field(default=None)

env = Settings()