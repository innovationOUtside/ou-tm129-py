
from setuptools import setup

required = [
    'numpy',
    'pandas',
    'matplotlib',
    'plotly',
    'seaborn',
    'cufflinks', #plotly support for pandas dataframes

    # Rules based systems
    'durable_rules',
    'git+https://github.com/innovationOUtside/durable_rules_magic.git',
    #'chatterbot==1.0.4',
    'noisify',
    #Simulator
    'git+https://github.com/innovationOUtside/nbev3devsim.git',
    
    #Linting
    'flake8',
    'pycodestyle',
    'pycodestyle_magic',
    ## Install additional style convention rules
    'pep8-naming',
    'flake8-bugbear',
    'flake8-docstrings',
    'flake8-builtins',
    ## Provide additional conventions for pandas code
    'pandas-vet',
    ## Autorepair
    'autopep8'
    ]

extras = {
    'jupyter': [
      'jupytext',
      'jupyter-server-proxy',
      'nbzip',
      # Notebook extensions
      'jupyter_contrib_nbextensions',
      'jupyter-wysiwyg',
      #Supported learning
      'nbtutor',
      'RISE',
      'nb-extension-tagstyler',
      'git+https://github.com/innovationOUtside/nb_extension_empinken.git',
      # Updates
      'ipywidgets>=7.5.0',
      'nbconvert>=5.5.0',
      #'jupyter-archive',
      'nbresuse',
      'git+https://github.com/NII-cloud-operation/Jupyter-multi_outputs',
      'nbgitpuller',
      'tqdm',
      # Drawing
      'drawSvg',
      'git+https://github.com/innovationOUtside/flowchart_js_jp_proxy_widget.git'
    ],
    'jupyterAL':[
     # Additional packages for ALs
    ]
    'production':[#For generating interactive web demos
      'nbinteract','voila']
}

setup(
    name='ou-tm129-py',

    version='0.0.1',

    description='Pyhton environment for TM129',
    long_description='',

    author='Tony Hirst',
    author_email='tony.hirst@open.ac.uk',

    license='MIT License',

    packages=[],
    include_package_data=True,
    install_requires=required,
    extras_require=extras,
    zip_safe=False,
)
