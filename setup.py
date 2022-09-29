from setuptools import setup
from setuptools import find_packages


setup(
	name="murife",
	version='0.0.1',
	packages=find_packages(),
	install_requires=[
	"click"
	],
	entry_points='''
	[console_scripts]
	murife=murife:murife
	'''	
)