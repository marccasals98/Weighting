import setuptools

setuptools.setup(
    include_package_data=True,
    name='weighting',
    version='0.01',
    description='weight unbalanced data',
    url='https://github.com/marccasals98/Weighting',
    author='Marc',
    author_email='marc.casals8@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'numpy', 'savReaderWriter'],
    long_description='weight a unbalanced pandas dataframe with non-independent variables',
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Os Independent"
    ]
)