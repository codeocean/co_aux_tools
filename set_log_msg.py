#!/usr/bin/env python
import sys

# local imports
try:
    from get_logger import LOGGER
except ImportError as e:
    print(
        f"ImportError: {e}\n"
        + f"Error importing LOGGER: did you add '/opt/co_aux_tools' to "
        + "PYTHONPATH and PATH ?"
    )


def print_log_msg(msg = None, level = "WARNING"):
    level = level.upper()
    if level == "DEBUG":
        return LOGGER.debug(msg)
    elif level == "INFO":
        return LOGGER.info(msg)
    elif level == "WARNING":
        return LOGGER.warning(msg)
    elif level == "ERROR":
        return LOGGER.error(msg)
    elif level == "CRITICAL":
        return LOGGER.critical(msg)
    else:
        raise Exception(
            f"{logger_name} logging level is not one of [DEBUG, INFO, "
            + "WARNING, ERROR, CRITICAL]"
        )

if len(sys.argv) > 2:
    print(print_log_msg(sys.argv[1], sys.argv[2]))
else:
    print(print_log_msg(sys.argv[1]))
