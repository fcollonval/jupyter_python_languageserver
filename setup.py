from setuptools import setup, find_packages
from codecs import open
import os
import io

name = 'jupyter_python_languageserver'

def get_version(file, name='__version__'):
    """Get the version of the package from the given file by
    executing it and extracting the given `name`.
    """
    path = os.path.realpath(file)
    version_ns = {}
    with io.open(path, encoding="utf8") as f:
        exec(f.read(), {}, version_ns)
    return version_ns[name]
# Get our version
version = get_version(os.path.join(name, '_version.py'))

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name=name,
    version=version,
    description='Palantir Python Language Server installed as a Jupyter Notebook Server extension.',
    long_description=long_description,
    url='https://github.com/fcollonval/jupyter_python_languageserver',
    download_url='https://github.com/fcollonval/jupyter_python_languageserver/tarball/' + version,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
    ],
    keywords=['jupyter', 'jupyterlab', 'notebook', 'extension', 'language-server'],
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        # like `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/jupyter_python_languageserver.json"
        ])
    ],
    author='Jupyter Development Team',
    author_email='fcollonval@gmail.com',
    install_requires=install_requires,
    zip_safe=False,
)
