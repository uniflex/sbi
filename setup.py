from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='uniflex_sbi',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/uniflex',
    license='MIT',
    author='Piotr Gawlowicz',
    author_email='gawlowicz@tu-berlin.de',
    description='UniFlex SBI',
    long_description='UniFlex SBI',
    keywords='wireless control',
    install_requires=[]
)
