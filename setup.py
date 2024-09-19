from setuptools import setup

setup (
    name='geoloc-util',
    version='1.0',
    py_modules=['geoloc_handler', 'error_handlers'],
    entry_points={
        'console_scripts': [
            'geoloc-util=geoloc_handler:main'
        ]
    }
)




