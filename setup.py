from setuptools import setup, find_packages


setup(name='pydepta',
      version='0.2',
      description="A Python implementation of DEPTA",
      long_description="A Python implementation of DEPTA (Data Extraction with Partial Tree Alignment)",
      author="Terry Peng",
      author_email="pengtaoo@gmail.com",
      install_requires=['w3lib', 'lxml'],
      packages=find_packages()
)
