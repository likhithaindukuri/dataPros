from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='1.0.0',
    packages=find_packages(),
    license='MIT',  
    author='Likhitha',
    author_email='likhithaindukuri117@gmail.com',
    description='A package for pre-processing the given data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/likhithaindukuri/dataPros',
    install_requires=[
        'numpy',
        'opencv-python',
    ],
)
