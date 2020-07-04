# ou-tm129-py
Python package for installing Pyhton packages required for TM129

This repo is exploring how we might distribute Python packages to students via a single installable package.

A Python package can be "empty" other than requiring the presence of particular packages.

We can define multiple levels of requirement using `install_requires=[]` for necessary packages and `extras_require={}` for optional packages.

Optional package collections can be installed via eg `pip install .[jupyter,production]` where specifiy the `extras_require` dictionary keys for the additional package collections we want to install.

So for example, we could deliver:

- core packages that configure a base Python environment: `pip install PACKAGE`;
- core packages and packages that customise a Jupyter environment in a particular way: `pip install PACKAGE[jupyter]`;
- core packages and packages that customise a Jupyter environment in a particular way and provide additional packages for ALs: `pip install PACKAGE[jupyter,AL]`;
- core packages plus production / development packages: `pip install PACKAGE[dev]`;
- core packages plus packages required to customise an OU hosted environment: `pip install PACKAGE[ouhosted]`;
- etc.

We could also use a package to deliver payloads to the student desktop, either in terms of files or services. eg we could supply command line utilites, a simple webserver/homepage, or a data files via a Python package.


Note that installing from repos is increasingly tricky to do; it's no longer supported from PyPi installed packages, so if things were only available from a (public) repo they'd have to be done manually. (We could provide a cli tool to do this, installed from the package; eg `tm129_utils install-extras` that runs a `pip git+...` set of installs.)
