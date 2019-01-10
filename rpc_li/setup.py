from setuptools import setup
from version.version import VERSION


setup(
    name='lrpc',
    author='yanzhe_li',
    version=VERSION,
    packages=[
        'rpc_li',
    ],
    install_requires=[
        'requests>=2.5.1,<3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'li_rpc = rpc_li.base:main',
        ]
    },
)
