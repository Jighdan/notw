from setuptools import setup, find_packages

setup(
    name = "notew-jighdan",	
    version = "0.0.5",
    author = "Reinny Almonte",
    author_email = "reynsth@gmail.com",
    description = "A command line note taking app",
    packages = find_packages(),
    entry_points = {
        "console_scripts": [
            "notew = notew.__main__:main"
        ]
    },
    url = "https://github.com/Jighdan/notew-cli",
    keyword = "productivity, sqlite3, notes",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: GNU :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8"
)
