from setuptools import setup, find_packages

setup(
    name="GESTEC",
    version="1.0.0",
    author="Rafel Castelló Fiol",
    author_email="raficadev@raficadev.onmicrosoft.com",
    description="Gestor de tareas de Terminal/Consola",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/raficadev/GESTEC",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "colorama",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'gestec=gestec:main',
        ],
    },
    include_package_data=True,
)
