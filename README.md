<!-- Generated with Nexin Django powered API template -->


# Diet Planner Api

API for the Diet Planner app


<!-- Default instructions -->

## GET STARTED

> If anything goes wrong, you can ask Jova Nissi for further assistance.

**Database**

This project is pre-configured with postgres. Follow this documentation on how to get started with postgres.

> [Install Postgres on Linux/Windows/Mac](http://postgresguide.com/setup/install.html)

After creating user(s) and database for this project, create a _**DATABASE URL**_, and add it to the **DATABASE_URL** in **env.sh** file.

The url must be formatted as this example bellow:
> postgres://user:password@host:port/db_name

_For localhost, host is **localhost**, and default port is **5432**_

**Create virtualenv**
```bash
virtualenv -p python3 venv
```

**Activate the virtualenv**
```bash
source venv/bin/activate
```

**Install requirements**
```bash
pip install -r requirements.txt
```

**Generate [env.sh](#) and [settings.ini](#) files** (For windows users, create the files manually):
```bash
cat env.sh.example > env.sh

cat settings.ini.example > settings.ini
```

*Open **[env.sh](#)** and **[settings.ini](#)** files, and fill in all necessary **values.***


**Export environment variables**
```bash
. ./env.sh
```
>Keep in mind that environment variables should be exported for every instance of venv started.

<br>

**Migrate**
```bash
python manage.py migrate
```

**Runserver**
```bash
python manage.py runserver
```

**Running tests**
```bash
python manage.py test
```
**Documentation**

By default, this project has a Swagger based documentation package called [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/).

> For full documentation on configurations, please follow the [guide link.](https://drf-yasg.readthedocs.io/en/stable/)







**Deployment**

Django applications can be deployed in many ways, and on many different servers. Here are some useful documentations for some popular servers.

> [Ningx/gunicorn/postgresql on ubuntu server](https://rahmonov.me/posts/run-a-django-app-with-gunicorn-in-ubuntu-16-04/)

> [Heroku](https://devcenter.heroku.com/categories/working-with-django)

<!-- 
## CONFIGURE [PRE-COMMIT](https://pre-commit.com/)

**Install pre-commit requirements**
```bash
pre-commit install
```

**Run against all the files**
```bash
pre-commit run --all-files
``` -->
