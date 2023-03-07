#!/usr/bin/env python
import sys

# local imports
try:
    from get_logger import LOGGER
except ImportError as e:
    print(
        f"ImportError: {e}\n"
        + "Error importing LOGGER: did you add '/opt/co_aux_tools/src' to "
        + "PYTHONPATH"
    )


def print_log_msg(msg=None, level="WARNING"):
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
            "logging level is not one of [DEBUG, INFO, WARNING, ERROR, CRITICAL]"
        )


def main(argv=None):
    if len(argv) == 1:
        sys.exit("You failed to provide a log message")
    elif len(argv) == 2:
        return print_log_msg(argv[1])
    return print_log_msg(argv[1], argv[2])


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))