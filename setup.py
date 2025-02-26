from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="rocm_power",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,  # List dependencies here
    author="Cédric Bulteel",
    description="A package for power consumption (in kWh) calculation and monitoring for AMD GPUs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cedricbulteel/rocm-power",  # Change as needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)