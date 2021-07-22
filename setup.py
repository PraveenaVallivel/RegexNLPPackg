import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='regexnlp',
    version='0.1',
    scripts=['regexnlp'] ,
    author="Praveena, Kathiresan, Soumya and Sandeep",
    author_email="",
    description="Text standardization library",
    long_description="A general purpose library to transform any text to structured data and tokenize the same to words and sentences",
    long_description_content_type="text/markdown",
    url="https://github.com/PraveenaVallivel/RegexNLPPackg",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: v3.9",
    "License :: OSI Approved :: GPL v3.0 License",
    "Operating System :: OS Independent"],
    )
