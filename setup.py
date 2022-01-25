#!/usr/bin/env python
# coding: utf8

"""  Distribution script. """
from setuptools import setup

setup(
    name="google-drive-download",
    version="project_version",
    description="Simple utility package for easy Google Drive downloading",
    author="Félix Voituret",
    author_email="fvoituret@deezer.com",
    url="https://github.com/Faylixe/google-drive-download",
    license="MIT License",
    packages=[
        "gdrive",
    ],
    python_requires=">=3.6, <3.9",
    include_package_data=True,
    install_requires=[
        "google-api-python-client",
        "google-api-support",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ]
)