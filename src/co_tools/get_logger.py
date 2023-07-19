import logging
import os

LOGGER_DIR_PATH = "../results/co_logs"  # path to log directory
co_computation_id = os.environ.get("CO_COMPUTATION_ID")
aws_batch_job_id = os.environ.get("AWS_BATCH_JOB_ID")
# name for the log file in ../results/co_logs
LOGGER_FILE_NAME = co_computation_id if co_computation_id else aws_batch_job_id
ENV_LEVEL = os.environ.get("CO_LOG_LEVEL")
DEFAULT_LEVEL = "WARNING" if not ENV_LEVEL else ENV_LEVEL.upper()

"""
Benefit to this logger is that it adds to each log entry a timestamp,
project name, name of .py file, line number and the log level.
[%(asctime)s - %(name)s - %(filename)s:%(lineno)s - %(levelname)s] %(message)s"
How to use:
import the logger -> from get_logger import LOGGER
LOGGER.{mode}("string to log")
How to modify log level:
set the environment variable CO_LOG_LEVEL in the run script
ex. export CO_LOG_LEVEL="INFO"
"""


def get_logger_for_string(*, logger_name: str, level: str):
    """
    :description: A mapping function from strings to logging levels.
    :param logger_name: Name of the logger handle e.g. `stream_handle`.
    :param level: The string describing the logging level to set.
    :return: in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR].
    DEBUG: Detailed information, typically of interest only when diagnosing
    problems.
    INFO: Confirmation that things are working as expected.
    WARNING: An indication that something unexpected happened, or indicative of
    some problem in the near future (e.g. 'disk space low'). The software is
    still working as expected.
    ERROR: Due to a more serious problem, the software has not been able to
    perform some function.
    CRITICAL: A serious error, indicating that the program itself may be unable
    to continue running.
    The default level is WARNING, which means that only events of this level
    and above will be tracked, unless the logging package is configured to
    do otherwise.
    """
    if level == "DEBUG":
        return logging.DEBUG
    elif level == "INFO":
        return logging.INFO
    elif level == "WARNING":
        return logging.WARNING
    elif level == "ERROR":
        return logging.ERROR
    elif level == "CRITICAL":
        return logging.CRITICAL
    else:
        raise Exception(
            f"{logger_name} logging level is not one of [DEBUG, INFO, "
            + "WARNING, ERROR, CRITICAL]"
        )


def generate_logger(
    *,
    name: str = LOGGER_FILE_NAME,
    logging_level: str = DEFAULT_LEVEL,
    format_string: str = (
        "[%(asctime)s - %(name)s - %(filename)s:%(lineno)s - %(levelname)s] "
        + "%(message)s"
    ),
):
    """
    :description: Creates a logger as desired for the global namespace without
    polluting the global namespace.
    :param name: The name of the logger.
    :param logging_level: The logging level to record to the logging file.
    :param format_string: A string to be passed to Python's logger generator
    facility to format logging output.
    :returns: A usable and proper Python logger.
    """

    logging_level = get_logger_for_string(logger_name=name, level=logging_level)

    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    # create console handler with a higher log level

    os.makedirs(LOGGER_DIR_PATH, exist_ok=True)

    file_handle = logging.FileHandler(f"{LOGGER_DIR_PATH}/{name}.log")
    file_handle.setLevel(logging_level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    log_format = logging.Formatter(format_string, "%Y-%m-%d %H:%M:%S")
    file_handle.setFormatter(log_format)

    logger.addHandler(file_handle)
    logger.addHandler(console_handler)

    return logger


LOGGER = None

if not LOGGER:
    LOGGER = generate_logger()
    LOGGER.debug(
        f"co_computation_id={co_computation_id} aws_batch_job_id={aws_batch_job_id}"
    )
