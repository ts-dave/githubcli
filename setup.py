from setuptools import setup

setup(
    name='githubcli',
    author='Tsatsu Dave',
    author_email='emsonjunior@gmail.com',
    license='MIT License',
    version='0.01',
    py_modules=['githubcli'],
    install_requires=['selenium', 'python-decouple'],
    entry_points='''
    [console_scripts]
    github=githubcli:main
    ''',
)