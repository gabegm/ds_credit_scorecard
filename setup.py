from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ds_credit_scorecard',
    packages=find_packages(),
    version='0.1.0',
    description='mathematical model attempting to provide a quantitative estimate of the probability that a customer will default on a loan.',
    author='gabegm',
    url="https://github.com/gabegm/ds_credit_scorecard.git",
    author_email="gabriel@gaucimaistre.com",
    license='MIT',
    #include_package_data=True,
    data_files=[("data/raw", ["data/raw/database.sqlite"])],
)
