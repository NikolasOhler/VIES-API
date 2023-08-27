from setuptools import setup, find_packages

setup(
    name='vies_eu_vat',
    packages=['vies_eu_vat'],
    version='0.1',
    description='A Python library for checking VAT numbers using the VIES SOAP APIsetup',
    author='Nikolay Oleynikov',
    author_email='nikolay.oleynikov96@gmail.com',
    url='https://github.com/OleynikovNikolay/vies_eu_vat',
    keywords=['VAT', 'SOAP', 'API'],
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    install_requires=[
       'requests',
    ],
)
