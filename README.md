[![CO Logo](https://github.com/codeocean/branding/raw/main/logo/CO_logo_135x72.png)](https://www.codeocean.com/product/)

# Code Ocean Aux Tools


#### Convenience tools for working in Code Ocean capsules and pipelines.

<hr>

### Background

These convenience tools were created to make working with working with sequencing files more streamlined. Some of the tools in this package are only useful in the Code Ocean platform but many of these tools will be useful outside of the platform.

<hr>

### Installing *Code Ocean* Aux Tools in your capsule

Add one line of code to your postintall script. At a later time this will be a package you can add to pip in the environment UI.

`pip install -i https://test.pypi.org/simple/ co-aux-tools`

---
### List of  Available Commands

The following commands will work at the terminal or in a bash script

    - get_cpu_count
    - get_dir_contents
    - get_fastq_pair
    - get_fwd_fastqs
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
    - get_fwd_fastqs()
    - get_read_direction()
    - get_read_pattern()
    - get_prefix()
    - get_rev_file()

---

### Logging

There is a pre-configured logger that will work seamlessly in bash and/or python and output to the same log file. The format for each log entry is:

`[{Time} {Date} - {log name} - {filename}:{lineno} - {Log Level}] {log message}`]

The available [log levels](https://docs.python.org/3/howto/logging.html) are `debug`, `info`, `warning`, `error`, and `critical`


**Python**

To use the logger in a python script just import it and use it

`from co_tools.get_logger import LOGGER`

To use it just type `LOGGER.{log level}("your log message here")` where `{log level}` is your desired log level.

e.g. `LOGGER.info("logging is fun")`

**Bash**

To use the logger in a bash script, just use the `set_log_msg` command. It takes 1 required argument and an additional optional argument.

The required argument is the log message and the optional argument is for the desired log level.

e.g. `set_log_msg "logging is fun" "INFO"`

### Setting the log level for LOGGER

Create an environment variable called `CO_LOG_LEVEL` and assign it one of the 5 available log levels. The default value is `WARNING`. Ideally you will assign the value to `CO_LOG_LEVEL` in your runscript just before the entry script is executed.

e.g.
```
export CO_LOG_LEVEL="INFO"
python -u main.py "$@"
```
or

```
export CO_LOG_LEVEL="INFO"
bash main.sh "$@"
```


---

[Code Ocean](https://codeocean.com/) is a cloud-based computational platform that aims to make it easy for researchers to share, discover, and run code. Visit our [Open Science Library](https://codeocean.com/explore) for free code and to demo our free product. Contact our [sales](https://codeocean.com/contact-us/sales/) for a demo of our [enterprise VPC product](https://codeocean.com/product/).<br /><br />
[![Code Ocean Logo](https://github.com/codeocean/branding/raw/main/logo/CO_logo_68x36.png)](https://www.codeocean.com)