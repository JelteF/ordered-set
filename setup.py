from setuptools import setup

setup(
    name="ordered-set",
    version = '1.1',
    maintainer='Luminoso Technologies, Inc.',
    maintainer_email='rob@luminoso.com',
    license = "MIT-LICENSE",
    url = 'http://github.com/LuminosoInsight/orderedset',
    platforms = ["any"],
    description = "A MutableSet that remembers its order, so that every entry has an index.",
    py_modules=['ordered_set'],
)
