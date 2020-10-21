from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="elasticsearchmappinggenerator",
    version="2.0.0",
    description="""
    Generate Elastic Search Index Mapping Quickly with this helper class see examples on how to use it 
     
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/elasticsearch-mapping-generator",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["elasticsearchmappinggenerator"],
    include_package_data=True,
    install_requires=[]
)