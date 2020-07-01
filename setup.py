from setuptools import setup

setup(
    name = "notew",	
    version = "0.1.0",
    author = "Reinny Almonte",
    author_email = "reynsth@gmail.com",
    description = "A command line note taking app",
    entry_points = {
        "console_scripts": [
            "notew = notew.main:main"
        ]
    },
    url = "https://github.com/Jighdan/notew-cli",
    python_requires=">=3.8"
)
