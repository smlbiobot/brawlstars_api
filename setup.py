import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brawlstars_api-smlbiobot", # Replace with your own username
    version="0.0.1",
    author="SML / RoyaleAPI",
    author_email="smlbiobot@gmail.com",
    description="Brawl Stars API",
    long_description="A Python implementation of the Brawl Stars API",
    long_description_content_type="A Python implementation of the Brawl Stars API",
    url="https://github.com/smlbiobot/brawlstars_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)