from setuptools import setup, find_packages

setup(
    name="adformat",
    version="1.12",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "wmi",
    ],
    entry_points={
        "console_scripts": [
            "adformat=adformat.ADFormat:main",
        ],
    },
    author="ARnoLD Digital",
    author_email="arnold_digital@yandex.ru",
    description="Formats multiply USB disks at once",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ARnoLD-Digital-Store/ADFormat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6"
)