from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'An API for piu piu game.'
LONG_DESCRIPTION = "A package for VALORANT's skin custom kill sound."

# Setting up
setup(
    name="valorant-killsound",
    version=VERSION,
    author="qing762",
    author_email="threatedblade@outlook.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests', 'setuptools'],
    keywords=['python', 'api', 'python wrapper', 'valorant', 'valorant-api', 'valorant api', 'piu piu game', 'sound effects', 'reaver', 'sovereign', 'ion', 'prime', 'kill sound', 'valorant gun skins'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
