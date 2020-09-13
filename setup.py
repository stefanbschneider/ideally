from setuptools import setup, find_packages


requirements = [
    'django==3.0.7',
    'Pillow>=7.2.0',
    'django-colorfield==0.3.1',
    'django-registration==3.1',
    'gunicorn>=20.0.4',
    'dj-database-url>=0.5.0',
    'psycopg2-binary>=2.8.5',
    'freezegun',
    'django-pwa',
    'whitenoise>=5.2.0'
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
