from setuptools import find_packages, setup

setup(
    name='api_python',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'flask',
        'python-dotenv',
        'click',
        'PyJWT',
        'pytest',
    ],
)
