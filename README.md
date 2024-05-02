# social-media

Social media is an online platforms that enable users to create and share content and participate in social networking.

## System dependencies

Python 3.8.9
Pip 24.0

## Project setup

The first thing to do is to clone the repository:

```bash
$ git clone https://github.com/bhumiijoshi/social-media.git
$ cd media_site
```

Now copy .env.example file into your .env file.
-----

Create a virtual environment to install dependencies in and activate it:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```bash
(env)$ pip install -r requirements.txt
```

Once pip has finished downloading the dependencies:

```bash
(env)$ cd project
(env)$ python manage.py runserver
```

And navigate to http://127.0.0.1:8000/
