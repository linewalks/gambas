from setuptools import setup, find_packages


setup(
    name="gambas", 
    version="0.0.2",
    description="Config Key Validator",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    url="https://github.com/linewalks/gambas",
    author="Linewalks", 
    author_email="yy.chung@linewalks.com", 
    packages=find_packages(exclude=["tests"]), 
    install_requires=[
        "configparser>=4.0.2",
    ],
    python_requires=">= 3.6",
    entry_points={
        "console_scripts": [
            "gambas = gambas.run:main"
        ]
    },
    setup_requires=["pytest-runner"],
    test_suite="tests",
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
)
