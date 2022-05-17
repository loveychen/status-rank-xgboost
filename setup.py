"""Python setup.py for status_rank_xgboost package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("status_rank_xgboost", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="status_rank_xgboost",
    version=read("status_rank_xgboost", "VERSION"),
    description="Awesome status_rank_xgboost created by loveychen",
    url="https://github.com/loveychen/status-rank-xgboost/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="loveychen",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["status_rank_xgboost = status_rank_xgboost.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
