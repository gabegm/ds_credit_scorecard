python setup.py clean --all
python setup.py sdist bdist_wheel
pip install dist/*.tar.gz