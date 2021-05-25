import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rdflib_r2r",
    version="0.0.1",
    author="Benno Kruit",
    author_email="bennokr@gmail.com",
    description="Virtual Knowledge Graph access to relational databases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bennokr/rdflib-r2r",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)