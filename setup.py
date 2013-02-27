from setuptools import setup

__version__ = 'dev'

description = '''django app to ask questions'''

setup(
    name='django-domande',
    packages=['domande'],
    version=__version__,
    description=description,
    author='Bulkan Evcimen',
    author_email='bulkan@gmail.com',
    url='https://github.com/bulkan/django-domande',
    install_requires=[
        'django_polymorphic'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)
