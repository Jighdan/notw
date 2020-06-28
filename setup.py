from setuptools import setup

setup(
	name="clarus",
	version="0.1.0",
	entry_points = {
		"console_scripts": [
			"clarus = clarus.__main__:main" 
		]
	},
  python_requires=">=3.8"
)
