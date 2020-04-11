import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='moneyonchain',
    version='0.0.4',
    packages=['moneyonchain'],
    url='https://github.com/moneyonchain/py_Moneyonchain/',
    author='Martin Mulone',
    author_email='martin.mulone@moneyonchain.com',
    description='Python interfaces on Money On Chain infraestructure',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='AGPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    package_data={
        "moneyonchain": ["config.json", "abi/*.abi", "abi/*.bin"]
    },
    python_requires='>=3.6',
    install_requires=[
        'web3'
    ],
)