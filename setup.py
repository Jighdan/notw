from setuptools import setup

setup(
    name = "notew",
    author = "Reinny Almonte",
    author_email = "reynsth@gmail.com",
    url = "https://github.com/Jighdan/notew",
    description = "A basic note taking CLI app.",
    version = "0.1.0",
    entry_points = {
	"console_scripts": [
	    "notew = notew.__main__:main"
	]
    },
    python_requires=">=3.8"
)
