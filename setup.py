from setuptools import setup, find_packages

setup(
    name='pytaxcloud',
    version='1.0',
    description="A library for integration with taxcloud.net. Taxcloud.net uses SOAP and this library uses SUDS for the SOAP integration.",
    long_description=open('README').read(),
    author='Jeff Tchang',
    author_email='jeff.tchang@gmail.com',
    url='http://github.com/tachang/pytaxcloud',
    packages=find_packages(),
    namespace_packages=['pytaxcloud'],
    install_requires=['setuptools'],
    license='BSD',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
    keywords = 'taxcloud api'
)
