[![CO Logo](https://github.com/codeocean/branding/raw/main/logo/CO_logo_135x72.png)](https://www.codeocean.com/product/)

# Code Ocean Aux Tools


#### Convenience tools for working in Code Ocean capsules and pipelines.

<hr>

### Background

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Venenatis urna cursus eget nunc scelerisque viverra. Id aliquet lectus proin nibh nisl condimentum id venenatis. Est pellentesque elit ullamcorper dignissim cras. Risus viverra adipiscing at in tellus integer. Cursus mattis molestie a iaculis at erat. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat. Laoreet sit amet cursus sit amet dictum sit amet. Viverra tellus in hac habitasse platea dictumst vestibulum rhoncus est. Non pulvinar neque laoreet suspendisse interdum. Aliquam etiam erat velit scelerisque. Donec ultrices tincidunt arcu non sodales. Aliquam ultrices sagittis orci a scelerisque purus.

<hr>

### Installing *Code Ocean* Aux Tools in your capsule

1. Create a new capsule.
2. Select a starter environment that has Python installed. We recommend a miniconda or mamba starter environment.
3. Copy & paste the following code into your postinstall script

```
# install code ocean aux tools
mkdir -p /opt
cd /opt
git clone https://github.com/codeocean/co_aux_tools.git
cd co_aux_tools/
# git checkout #######  # uncomment and replace with commit hash to pin the version
chmod +x {g,s}et_*
ln -s $PWD/{g,s}et_*.py /usr/local/bin
```

4. In your run script add the following line of code prior to the entry point
    - `export PYTHONPATH="${PYTHONPATH}:/opt/co_aux_tools"`
    - Here is an example of a run script
    
```
export PYTHONPATH="${PYTHONPATH}:/opt/co_aux_tools"
python -u my_python_script.py "$@"
```


<hr>

[Code Ocean](https://codeocean.com/) is a cloud-based computational platform that aims to make it easy for researchers to share, discover, and run code. Visit our [Open Science Library](https://codeocean.com/explore) for free code and to demo our free product. Contact our [sales](https://codeocean.com/contact-us/sales/) for a demo of our [enterprise VPC product](https://codeocean.com/product/).<br /><br />
[![Code Ocean Logo](https://github.com/codeocean/branding/raw/main/logo/CO_logo_68x36.png)](https://www.codeocean.com)