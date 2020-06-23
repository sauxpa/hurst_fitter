from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hurst_fitter',
    version='0.0.1',
    author="Patrick Saux",
    author_email="patrick.jr.saux@gmail.com",
    description="Library to estimate Hurst index of time series.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sauxpa/hurst_fitter",
    install_requires=['numpy', 'scipy', 'pandas', 'statsmodels'],
    python_requires='>=3.6',
)
