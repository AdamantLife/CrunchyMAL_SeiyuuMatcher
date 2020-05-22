import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CrunchyMAL_SeiyuuMatcher-AdamantLife",
    version="0.0.1",
    author="AdamantLife",
    author_email="contact.adamantmedia@gmail.com",
    description="Sauce for Crunchyroll Seiyuu Birthday Posts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',

    install_requries = [
        "opencv-python",
        "requests"
        ]
)