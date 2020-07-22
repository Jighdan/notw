from setuptools import setup

setup(
    name = "notw",
    author = "Reinny Almonte",
    author_email = "reynsth@gmail.com",
    url = "https://github.com/Jighdan/notw",
    description = "A basic note taking CLI app.",
    version = "0.1.0",
    entry_points = {
	"console_scripts": [
	    "notw = notw.__main__:main"
	]
    },
    python_requires=">=3.8"
)
