from setuptools import setup, find_packages

long_desc = """

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
