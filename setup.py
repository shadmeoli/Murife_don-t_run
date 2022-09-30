# this file is esential for making python identify this as a package that can be installed and be used to generate build files
from setuptools import setup
from setuptools import find_packages

# defining our CLI and the main function to call on initilization 
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
