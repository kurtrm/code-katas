from setuptools import setup


dependencies = ['ipython', 'pytest']
extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']
}

setup(
    name='Code Katas',
    description='Katas for Day of Code.',
    version=0.1,
    author='Kurt Maurer',
    author_email='kurtrm@gmail.com',
    license='MIT',
    py_modules=[''],
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={
        'console_scripts':
            ''
    }
)
