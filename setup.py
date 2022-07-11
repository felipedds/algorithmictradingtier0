from setuptools import find_packages, setup

def read(filename):
    return [
        req.strip()
        for req in open(filename).readlines()   
    ]

setup(
    name="algotradingtier0",
    version="0.1.0", # major, minor, patch
    description="algotrading app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"]
)

