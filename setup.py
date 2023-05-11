from setuptools import setup


setup(
    name='sanpera',
    version='0.2rc0+weasyl.3',
    description='Image manipulation library, powered by ImageMagick',
    author='Eevee',
    author_email='eevee.sanpera@veekun.com',
    url='http://eevee.github.com/sanpera/',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries',
    ],

    packages=['sanpera'],
    python_requires='>=3.4',
    install_requires=[
        'cffi>=1.0.0',
    ],

    setup_requires=['cffi>=1.0.0'],
    cffi_modules=['sanpera/_api_build.py:ffi'],
)
