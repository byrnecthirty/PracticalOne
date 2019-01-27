from setuptools import setup
 
setup(name="clarenight",
    version="0.0.1",
    author="byrnecthirty",
    author_email="author@example.com",
    description="A small example package",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=['clarenight'],
    entry_points={
          'console_scripts': [
              'comp30820_clarenight=clarenight.main:main'
          ]
      },
    
)
