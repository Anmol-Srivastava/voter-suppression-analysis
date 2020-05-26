from setuptools import setup, find_packages

PACKAGES = find_packages()
DESCRIPTION = "Desc."
URL = "https://google.com"

OPTS = dict(
  name="vsa",
  description=DESCRIPTION,
  url=URL,
  license="MIT",
  author="me",
  version="1.0",
  packages=PACKAGES
)

if __name__ == '__main__':
  setup(**OPTS)
