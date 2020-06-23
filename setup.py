from setuptools import setup

setup(
	name="clarus",
	version="0.0.1",
	packages=["blessings"],
	entry_points = {
		"console_scripts": [
			"clarus = clarus.__main__:main" 
		]
	}
)