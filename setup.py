import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OnlySnarf",
    version="0.0.1",
    author="Skeetzo",
    author_email="WebmasterSkeetzo@gmail.com",
    description="Only Snarf Automation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skeetzo/onlysnarf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)