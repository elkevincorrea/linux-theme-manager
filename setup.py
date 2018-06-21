from setuptools import setup

setup(
    name='theme_manager',
    version='0.1',
    py_modules=['theme_manager'],
    install_requires=[
        'click',
        'GitPython'
    ],
    entry_points='''
        [console_scripts]
        theme_manager=theme_manager:cli
    ''',
)