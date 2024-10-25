from setuptools import setup, find_packages


setup(
  name="musalb",
  version="0.1",
  packages=find_packages(),
  install_requires=[],
  author="IacopoScandale",
  author_email="iacopo.scandale.is@gmail.com",
  description="simple line-command music album manager",
  license="GNU General Public License",
  entry_points={
    "console_scripts": [
      "musalb=musalb.cli:main"
    ],
  },
)