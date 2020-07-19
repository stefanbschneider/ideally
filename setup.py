from setuptools import setup, find_packages


requirements = [
    'django==3.0.7',
    'django-colorfield==0.3.1',
    'gunicorn'
]

setup(
    name='ideally',
    author='Stefan Schneider',
    version=0.1,
    description="Ideally is a web app that allows you to organize and grow your ideas.",
    url='https://ideally-app.herokuapp.com/',
    find_packages=find_packages(),
    python_requires=">=3.8.*",
    install_requires=requirements,
    zip_safe=False
)
