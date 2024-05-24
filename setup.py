from setuptools import setup, find_packages

setup(
    name='smart-trajectories',
    version='0.1.10',
    author='Felipe Brito',
    author_email='arrudabritofelipe@gmail.com',
    description='Smart Trajectories for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/britofelipe/smart-trajectories',
    packages=find_packages(),
    install_requires=[
        'attrs==23.2.0',
        'certifi==2024.2.2',
        'click==8.1.7',
        'click-plugins==1.1.1',
        'cligj==0.7.2',
        'contourpy>=1.2.0',
        'cycler==0.12.1',
        'fiona>=1.9.0',
        'fonttools>=4.48.0',
        'geographiclib>=2.0',
        'geopandas>=0.13.0',
        'geopy>=2.3.0',
        'kiwisolver>=1.4.0',
        'matplotlib>=3.7.0',
        'movingpandas>=0.15.0',
        'numpy>=1.24.0',
        'packaging>=21.0',
        'pandas>=1.5.0',
        'pillow>=9.4.0',
        'pyparsing>=3.0.0',
        'pyproj>=3.4.0',
        'python-dateutil>=2.8.0',
        'pytz>=2023.0',
        'Rtree>=1.0.1',
        'shapely>=1.8.5.post1',
        'six>=1.16.0',
        'tzdata>=2023.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)