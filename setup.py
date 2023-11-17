from setuptools import find_packages, setup

VERSION = "0.1.0"
DESCRIPTION = "newpy is a tool to help you create new python projects with ease "
LONG_DESCRIPTION = """
newpy is a tool to help you create new python projects with ease 
"""

# Setup
setup(
    name="newpy",
    version=VERSION,
    author="Axis (blankRiot96)",
    email="blankRiot96@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["click"],
    python_requires=">=3.11",
    keywords=["dir", "template", "new", "newpy"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["newpy=newpy:main"]},
)
