import glob
import os
from setuptools import setup

import datascope_tools

# get all of the scripts
scripts = glob.glob("bin/*")

# read in the description from README
with open("README.md") as stream:
    long_description = stream.read()

github_url='https://github.com/datascopeanalytics/datascope-tools'

# read in the dependencies from the virtualenv requirements file
dependencies = []
filename = "REQUIREMENTS"
with open(filename, 'r') as stream:
    for line in stream:
        package = line.strip().split('#')[0]
        if package:
            dependencies.append(package)

setup(
    name=datascope_tools.__name__,
    version=datascope_tools.VERSION,
    description="import random.scripts, random.tools, random.ideas",
    long_description=long_description,
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Datascope Analytics',
    author_email='github.admin@datascopeanalytics.com',
    license='MIT',
    scripts=scripts,
    packages=[datascope_tools.__name__],
    install_requires=dependencies,
    zip_safe=False,
)
