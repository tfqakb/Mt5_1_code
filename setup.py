from setuptools import find_packages, setup

setup(
name="mcqgenerator",
version="0.0.1",
author="taufique",
author_email="taufiqueakbar@gmail.com",
install_requires=[
    "langchain",
    "pandas",
    "numpy",
    "streamlit",
    "python-dotenv",
    "langgraph",
    "crewai",
    "langchain-core",
    "langchain-community",
    "langchain-groq",
    "langchain-classic",
    "Pydantic",
    "langchain-tavily",
    "langchain-huggingface",
    "uvicorn",
    "PyPDF2",
    "MetaTrader5",
    "ta",
    "yfinance",
    "scikit-learn",
    "transformers",
    "torch",
    "requests",
    "matplotlib"
],
packages=find_packages()

)