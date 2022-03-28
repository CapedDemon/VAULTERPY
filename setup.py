import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vaulter-py",
    version="0.0.2",
    author="Shreejan Dolai",
    author_email="dolaishreejan@gmail.com",
    description="VAULTERPY is a python program with which you can secure your precious passwords very easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shreejan-35/VAULTERPY",
    project_urls={
        "Bug Tracker": "https://github.com/Shreejan-35/VAULTERPY/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    keywords=['password manager', 'password', 'vaulter', 'py', 'manager', 'safe'],
    install_requires=[
          'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'vaulterpy = vaulter_py.passvault:main',
        ],
    }
)