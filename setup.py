from setuptools import _install_setup_requires, find_packages, setup

setup(
    name='gray_encorder',
    version='0.0.1',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'autopep8~=1.5.7',
        'Click~=7.0',
        'colorama~=0.4.4',
        'numpy~=1.21.1',
        'opencv-python~=4.5.3.56',
        'pycodestyle~=2.7.0',
        'toml~=0.10.2',
    ],
    entry_points={
        'console_scripts': [
            'gray_encorder=gray_encorder.core:cli'
        ]
    }
)
