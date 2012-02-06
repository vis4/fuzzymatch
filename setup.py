from setuptools import setup, find_packages

long_desc = """
fuzzymatch uses the Levenshtein package to compute similarity between strings taken from two csv files. In ambiguous cases it will ask the user to chose among top-guesses.

The resulting matches will be stored in a separate JSON file. You can cancel the merging process (ctrl-c) and proceed at the point you stopped later. If you run fuzzymatch on two csv files for the first time (which is when the json db doesn't exist) it will ask you which columns it should use for text matching.
"""


setup(
    name='fuzzymatch',
    version='0.1',
    description="Command line util for merging two tables based on text similarity measurements.",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    keywords='',
    author='Gregor Aisch',
    author_email='gregor.aisch@okfn.org',
    url='http://labs.okfn.org',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests','test.*']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=["python-Levenshtein"],
    tests_require=[],
    entry_points={
        'console_scripts': [
             'fuzzymatch = fuzzymatch:cli'
        ]
    }
)
