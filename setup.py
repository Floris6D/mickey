from setuptools import setup, find_packages

setup(
    name="mickey",
    packages=find_packages(include=("mickey*",)),
    version="0.0.1",
    author="Axel Barroso-Laguna · Sowmya Munukutla · Victor Adrian Prisacariu · Eric Brachmann",
    install_requires=open("resources/requirements.txt", "r").read().split("\n"),
)
