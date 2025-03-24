import sys
from .services.change_windows_themes import ChangeWindowsThemes
from .utils import logger


if __name__ == "__main__":
    logger.info("Starting the application")
    try:
        changer = ChangeWindowsThemes()
        changer.change_themes()
        logger.success("Application finished successfully!")
        sys.exit(0)
    except Exception as e:
        logger.error(e)
        sys.exit(1)
    