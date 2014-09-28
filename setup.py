from setuptools import setup

setup(
    name='beetle_markdown',
    version='0.1.0'
    author='Esben Sonne',
    author_email='esbensonne+code@gmail.com',
    description='Markdown plugin for the static site generator Beetle',
    url='https://github.com/cknv/beetle-markdown',
    license='MIT',
    packages=[
        'beetle_markdown'
    ],
    install_requires=[
        'Markdown',
    ],
)
