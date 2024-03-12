from setuptools import setup, find_packages

README_FILENAME = "README.md"

readme_content = ""
with open(README_FILENAME, "r") as f:
    readme_content = f.read()

packages_found = find_packages()

setup(
    name="msvytemplating",
    version="0.1.0",
    author="MrSevyu",
    author_email="javiermdeb@gmail.com",
    packages=packages_found,
    description="A custom templating engine for Flask applications.",
    long_description=readme_content,
)
# Update de javi
