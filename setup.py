import os
import htmltag

try:
    from setuptools import setup
    from setuptools import Command
except ImportError:
    from distutils.core import setup
    from distutils.cmd import Command
    
# https://pyscaffold.org/en/latest/_modules/pyscaffold/integration.html
def build_cmd_docs():
    """Return Sphinx's BuildDoc if available otherwise a dummy command

    Returns:
        :obj:`~distutils.cmd.Command`: command object
    """
    try:
        from sphinx.setup_command import BuildDoc
    except ImportError:
        class NoSphinx(Command):
            user_options = []

            def initialize_options(self):
                raise RuntimeError("Sphinx documentation is not installed, "
                                   "run: pip install sphinx")

        return NoSphinx
    else:
        return BuildDoc


cmdclass = {'build_sphinx': build_cmd_docs()}

setup(
    name="htmltag",
    version=htmltag.__version__,
    description="Python HTML tag interface",
    author=htmltag.__author__,
    cmdclass=cmdclass,
    author_email="daniel.mcdougall@liftoffsoftware.com",
    url="https://github.com/liftoff/htmltag",
    license="Apache 2.0",
    py_modules=["htmltag"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
