import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyFunnels",
    version="0.0.1",
    author="TJ Nicholls",
    author_email="author@example.com",
    description="Aggregates the output of one or more tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/packetvitality/PyFunnels",
    download_url="https://github.com/packetvitality/PyFunnels/archive/0.0.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)