from setuptools import setup, find_packages

setup(
    name='clipper-ai',
    version='0.1.0',
    description='Batch image generation for webui_forge using prompts',
    author='Ernan Hughes',
    author_email='ernanhughes@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'clipper=clipper.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
