import os
from pathlib import Path
from typing import List

from setuptools import find_namespace_packages, setup



test_requirements = ["pytest", "pytest-subtests", "coverage"]
# develop_requirements = test_requirements + ["pre-commit"]
# demos_requirements = ["ipython", "ipykernel"]

extras_requires = {
    "test": test_requirements,
}

requirements: List[str] = [
    "dacite",

]


setup(
    author="NASA/GFDL",
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 1 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    install_requires=requirements,
    extras_require=extras_requires,
    name="pylibfms",
    license="BSD license",
    packages=find_namespace_packages(include=["pylibfms", "pylibfms.*"]),
    include_package_data=True,
    url="https://github.com/fmalatino/fms2py",
    version="2024.09.00",
    zip_safe=False,
    entry_points={},
)