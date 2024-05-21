from setuptools import setup, find_packages

setup(
    name="GESTEC",
    version="1.0.0",
    author="Rafel Castelló Fiol",
    author_email="raficadev@raficadev.onmicrosoft.com",
    description="Gestor de tareas de consola GESTEC",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/raficadev/GESTEC",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "colorama",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gestec=gestec:main',
        ],
    },
    include_package_data=True,
)