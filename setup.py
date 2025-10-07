from setuptools import setup, find_packages

with open("README_PYPI.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-factory",
    version="1.0.0",
    author="Valentin",
    author_email="vpavonlopez@gmail.com",
    description="🏭 Create custom AI models in 5 minutes. Local, free, web interface included. No coding required!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valenuser/ai-factory",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai-factory=ai_factory.cli:main",
        ],
    },
    include_package_data=True,
)
