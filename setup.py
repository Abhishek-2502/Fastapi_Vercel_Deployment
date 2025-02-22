from setuptools import setup, find_packages

setup(
    name="fastapi-hosting-master",
    version="0.1.0",
    packages=find_packages(include=["app", "app.*"]),
    package_dir={'': '.'}, 
    install_requires=[
        "fastapi==0.88.0",
        "uvicorn==0.20.0"
    ],
    entry_points={
        "console_scripts": [
            "start-fastapi = app.cli:main"
        ]
    },
    author="Abhishek Rajput",
    author_email="abhishek25022004@gmail.com",
    description="A simple FastAPI application",
    url="https://github.com/Abhishek-2502/FastAPI_Deploy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
