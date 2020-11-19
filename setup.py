from setuptools import setup, find_packages

setup(name='worksheetgen',
      version='0.0.1',
      description='A worksheet generator',
      url='https://github.com/lukew3/worksheetgen',
      author='Luke Weiler',
      author_email='lukew25073@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'': ['base.html']},
      include_package_data=True,
      install_requires=['weasyprint'],
      entry_points={}
      )
