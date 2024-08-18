from setuptools import setup, find_packages

setup(
    name='gpt-connect',
    version='0.0.1',
    description='A Python wrapper for interacting with GPT models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abhinav Sinha',
    author_email='sinhabhinv@gmail.com',
    url='https://github.com/sinhadotabhinav/gpt-connect',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv==0.19.2',
        'pyyaml==6.0'
    ],
    extras_require={
        'dev': [
            'pytest==7.1.2',
            'black',
            'flake8'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
