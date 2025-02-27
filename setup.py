#! /usr/bin/env python
#

DESCRIPTION = "pysedm: the SEDmachine pipleine"
LONG_DESCRIPTION = """ Pipeline for generic Transient Typer IFU - option on SEDM built in. """

DISTNAME = 'pysedm'
AUTHOR = 'Mickael Rigault'
MAINTAINER = 'Mickael Rigault' 
MAINTAINER_EMAIL = 'mickael.rigault@clermont.in2p3.fr'
URL = 'https://github.com/MickaelRigault/pysedm/'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/MickaelRigault/pysedm/tarball/0.30'
VERSION = '0.30.0'

try:
    from setuptools import setup, find_packages
    _has_setuptools = True
except ImportError:
    from distutils.core import setup
    _has_setuptools = False

def check_dependencies():
    install_requires = []

    # Just make sure dependencies exist, I haven't rigorously
    # tested what the minimal versions that will work are
    # (help on that would be awesome)
    try:
        import pyifu
    except ImportError:
        install_requires.append('pyifu')

    try:
        import psfcube
    except ImportError:
        install_requires.append('psfcube')
        
    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    if _has_setuptools:
        packages = find_packages()
        print(packages)
    else:
        # This should be updated if new submodules are added
        packages = ['pysedm',
                    "pysedm.script",
                    "pysedm.utils"]

    setup(name=DISTNAME,
          author=AUTHOR,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          scripts=["bin/ccd_to_cube.py" ,
                   "bin/extract_star.py",
                   "bin/extractstar.py",
                   "bin/extractstar_ab.py",
                   "bin/cube_quality.py",
                   "bin/pysedm_report.py",
                   "bin/pysedm_pull.py",
                   "bin/pysedm_io.py",                   
                   "bin/derive_wavesolution.py",
                   "bin/quality_check.py",
                   "bin/build_guider.py",
                   "bin/rm_cubecr.py"],
          packages=packages,
          include_package_data=True,
          package_data={'pysedm': ['data/*.*']},
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.5',              
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Astronomy',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
          )
