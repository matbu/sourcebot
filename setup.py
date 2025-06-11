from setuptools import setup, find_packages

setup(
    name="sourcebot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "faiss-cpu",
        "sentence-transformers",
        "PyMuPDF",
        "llama-index",
        "langdetect",
        "requests",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "sourcebot=sourcebot.main:main",
        ],
    },
    author="Mathieu Bultel",
    description="A bot for ingesting and querying documents using FAISS and LLMs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
