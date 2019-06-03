from setuptools import find_packages, setup


def author():
    with open("src/{{ cookiecutter.package_name }}/__init__.py") as fh:
        for line in fh:
            if line.startswith("__author__"):
                name, email = line.rsplit(" ", 1)
                break
    name = name.split("=")[1].strip().replace('"', "")
    email = email.strip().replace("<", "").replace(">", "").replace('"', "")
    return name, email


setup(
    name="{{ cookiecutter.package_name }}",
    version=VERSION,
    description="{{ cookiecutter.package_short_description }}",
    long_description=open("README.rst").read().strip(),
    license="MIT",
    url="https://github.com/mdippery/{{ cookiecutter.package_name }}",
    author=author()[0],
    author_email=author()[1],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.__main__:main",
        ]
    },
    setup_requires=["setuptools_scm"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
