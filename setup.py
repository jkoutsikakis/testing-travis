from setuptools import setup, find_packages


setup(
    name='testing-travis',
    version='0.0.1',
    description='testing_travis',
    packages=find_packages(exclude=['tests']),
    author='John Koutsikakis',
    author_email="jkoutsikakis@gmail.com",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'numpy>=1.14,<2',
        'scikit-learn>=0.19,<1',
        'six>=1.11,<2',
        'torch>=1,<2',
        'tqdm>=4.36.1,<5',
        'hyperopt>=0.1,<0.2'
    ],
    tests_require=['nose', 'python-coveralls'],
    test_suite='nose.collector'
)
