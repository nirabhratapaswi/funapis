import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='funapis',
    version='0.2',
    author="Nirabhra Tapaswi",
    author_email="nirabhratapaswi@gmail.com",
    description="Command line tool for some fun api usage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nirabhratapaswi/funapis",
    packages=["numapi"],
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['numn=numapi.numapi_command_line:main'],
    },
    package_data={'numapi': ['numapi/token.txt']},
    include_package_data=True
 )