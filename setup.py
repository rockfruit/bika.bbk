from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='bika.bbk',
      version=version,
      description="Bika BBK",
      long_description="",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Bika Lab Systems',
      author_email='support@bikalabs.com',
      url='http://www.bikalabs.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bika'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'bika.wine',
          'archetypes.schemaextender',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
