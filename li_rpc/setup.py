from setuptools import setup, find_packages

# requirements
install_requires = [
    "six>=1.10.0",
]

setup(name="gm-types",
      version=__import__("gm_types").__version__,
      description="Li_rpc",
      author="li_",
      author_email="youwew@qq.com",
      packages=find_packages(),
      url="http://git.gengmei.cc/backend/gm-types",
      install_requires=install_requires)