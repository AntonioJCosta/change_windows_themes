import functools
import sys
from datetime import datetime
from loguru import logger
from .env_config import env, ENV, ROOT_DIR

LOGGER_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<level>{message}</level> | "
)

# Remove all existing handlers
logger.remove()

def _set_logs_file_path() -> str:

    project_name = env.PROJECT_NAME.replace(" ", "_").lower()

    is_test = "tests" in sys.modules
    if is_test:
        return f"{ROOT_DIR}/tests/logs/{project_name}.log"

    if ENV != "prod":
        return f"{ROOT_DIR}/logs/{project_name}_{ENV}.log"

    today_date = datetime.now().strftime("%d-%m-%Y")
    return f"/var/log/custom_projects/{project_name}/{today_date}.log"

# Log to a file named after the module
logs_path = _set_logs_file_path()
logger.add(
    logs_path,
    format=LOGGER_FORMAT,
    rotation="10 MB",
    level=env.LOG_LEVEL,
)

# Log to console
logger.add(
    sys.stdout,
    format=LOGGER_FORMAT,
    level=env.LOG_LEVEL,
)

logger.info(f"Logs are being saved to {logs_path}")

# Error logging decorator
def log_errors_exceptor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise  # re-throw the last exception

    return wrapper


