from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sams-clustering",
    version="1.0.0",
    author="Implementation of Hyrien & Baran (2017)",
    description="Fast Nonparametric Density-Based Clustering using Stochastic Approximation Mean-Shift",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sams-clustering",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="clustering, machine-learning, density-based, mean-shift, stochastic-approximation",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/sams-clustering/issues",
        "Source": "https://github.com/yourusername/sams-clustering",
        "Documentation": "https://github.com/yourusername/sams-clustering#readme",
    },
)