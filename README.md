[![CO Logo](https://github.com/codeocean/branding/raw/main/logo/CO_logo_135x72.png)](https://www.codeocean.com/product/)

# Code Ocean Aux Tools

[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
![Code Style](https://img.shields.io/badge/code%20style-black-black)

#### Convenience tools for working in Code Ocean capsules and pipelines.

---

### Background

These convenience tools were created to make working with files common in bioinformatics more streamlined. Some of the tools in this package are only useful in the Code Ocean platform but many of these tools will be useful outside of the platform.

---

### Requirements

Python>=3.8

---

### Installing *Code Ocean* Aux Tools in your capsule

Add the following package using pip in the environment UI `Code-Ocean-Aux-Tools`
or use the following command at the terminal.

`pip install Code-Ocean-Aux-Tools`

[Code-Ocean-Aux-Tools on Pypi](https://pypi.org/project/Code-Ocean-Aux-Tools/)

---
### List of  Available Commands

The following commands will work at the terminal or in a bash script. Each of these commands has a `--help` flag which provides more information about using the command.

    - get_cpu_count
    - get_dir_contents
    - get_fasta_file
    - get_fastq_pair
    - get_fastqs
    - get_groups
    - get_pipeline_confirm
    - get_read_direction
    - get_read_pattern
    - get_read_prefix
    - get_rev_file
    - set_log_msg

---

### List of Available Python Functions

There are 2 modules you can import (`co_utils` & `co_fastq`)
At the top of your python script, import them 
```
from co_tools import co_utils
from co_tools import co_fastq
```

**co_utils**

    - get_cpu_limit()
    - get_dir_contents()
    - get_groups()
    - is_pipeline()

**co_fastq**

    - get_fastq_pair()
    - get_fastqs()
    - get_read_direction()
    - get_read_pattern()
    - get_prefix()
    - get_rev_file()

---

## Logging

There is a pre-configured logger that will work seamlessly in bash and/or python and output to the same log file (when configured to output to a file). The format for each log entry is:

`[{Date} {Time} - {filename}:{funcName}:{lineno} - {Log Level}] {log message}`

The available [log levels](https://docs.python.org/3/howto/logging.html) are `debug`, `info`, `warning`, `error`, and `critical`


**Python**

To use the logger in a python script just import it and use it

`from co_tools.get_logger import LOGGER`

To use it just type `LOGGER.{log level}("your log message here")` where `{log level}` is your desired log level.

e.g. `LOGGER.info("logging is fun")`

**Bash**

To use the logger in a bash script, just use the `set_log_msg` command. It takes 1 required argument and an additional optional flag `--log-level`

The required argument is the log message and the optional flag is for the desired log level. The default log level is `"WARNING"` when no flag is used.

e.g. `set_log_msg "logging is fun" --log-level "INFO"`

---
## Configuring the LOGGER


### Activating the LOGGER 

The Code Ocean LOGGER is turned off by default. To turn it on, create an environment variable called `CO_LOG_TYPE` and assign it one of `FILE`, `CONSOLE`, `BOTH`. If you do not create this environment variable to activate the logger, there will be no logging.


    - FILE - The logger will only output to a log file
    - CONSOLE - The logger will only output to the console
    - BOTH - The logger will output to both a log file and the console


e.g.
```
export CO_LOG_TYPE="FILE"
```

### Assigning the log level

Create an environment variable called `CO_LOG_LEVEL` and assign it one of the 5 available [log levels](https://docs.python.org/3/howto/logging.html). The recommended method is to assign the value to `CO_LOG_LEVEL` in your runscript (`run`) just before the entry script is executed.

e.g.
```
export CO_LOG_TYPE="FILE"
export CO_LOG_LEVEL="INFO"
python -u main.py "$@"
```
or

```
export CO_LOG_TYPE="FILE"
export CO_LOG_LEVEL="INFO"
bash main.sh "$@"
```

---

[Code Ocean](https://codeocean.com/) is a cloud-based dry lab for scientific computing with a focus on guaranteeing reproducibility, collaboration and organizing scientific projects. Code Ocean automates best practices allowing users of the platform to focus on science yet follow best practices. Visit our [Open Science Library](https://codeocean.com/explore) for free code and to demo our free product. Contact our [sales](https://codeocean.com/contact-us/sales/) for a demo of our [enterprise VPC product](https://codeocean.com/product/).<br /><br />
[![Code Ocean Logo](https://github.com/codeocean/branding/raw/main/logo/CO_logo_68x36.png)](https://www.codeocean.com)
