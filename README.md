# land-avilability-api
API backend for Land Availability tool

# Continuous integration status

[![Travis-CI Status](https://secure.travis-ci.org/alphagov/land-availability-api.png?branch=master)](http://travis-ci.org/#!/alphagov/land-availability-api)

# PostgreSQL Setup

Make sure you have **PostgreSQL** (tested with 9.6) installed along with PostGIS
extension. You can find more information for the different operating systems
here: https://docs.djangoproject.com/en/1.10/ref/contrib/gis/install/postgis/

It's strongly suggested to use Postgres.app on OSX and to install all the other
tools and dependencies using **brew**.

## Create DB

```
createdb landavailability
psql landavailability
> CREATE EXTENSION postgis;
```

# Project Configuration

Make sure you have this environment variable set:

```
DATABASE_URL=postgres://USERNAME:PASSWORD@HOST:PORT/DBNAME
```

example:

```
DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability
```

If you are using a Python virtual environment, you can save these values in
$venv_folder/bin/postactivate script:

```
export DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability
```

# Python

The project is being developed and tested with **Python >= 3.5.x**
