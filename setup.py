import setuptools

setuptools.setup(
    name='templates-s3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/templates-s3','scripts/templates-s3-create-bucket','scripts/templates-s3-create-full-access-env','scripts/templates-s3-create-read-only-env','scripts/templates-s3-download','scripts/templates-s3-upload']
)
