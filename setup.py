from setuptools import setup, find_packages

setup(
    name="demo_py_ci",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={},
)

