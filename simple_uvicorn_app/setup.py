import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="simple-uvicorn-app-me",
    version="0.0.1",
    author="mariserts",
    author_email="mariserts84@gmail.com",
    description="Simple uvicorn app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mariserts/simple_uvicorn_app",
    project_urls={
        "Bug Tracker": (
            "https://github.com/mariserts/simple_uvicorn_app/issues"),
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
