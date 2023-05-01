from setuptools import setup, find_packages

setup(
    name="PyVecDB",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "annoy",
        "msgpack",
        "sqlite3",
    ],
    author="Your Name",
    author_email="north.tyronejr@gmail.com",
    description="A Python library for efficient similarity search using high-dimensional vectors.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tyronenorth/PyVecDB",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
