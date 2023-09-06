import setuptools

def getfFromFile(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        return f.read()

__version__ = "0.0.0"
SRC_REPO = "QuickDicom"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= "amaljova",
    author_email= "amaljova@gmail.com",
    url= "https://github.com/amaljova/QuickDicom",
    description= "A small python package for managing DICOM images",
    long_description= getfFromFile("README.md"),
    long_description_content = "text/markdown",
    # project_urls = {},
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where="src")
)

