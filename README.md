# SmartTraffic-SmartCityAsuncion
La plataforma del servidor del proyecto SmartTraffic

## REQUIREMENTS

You need to install this to have fun with our project.

### docker & docker-compose
Docker: 18.03 +
Docker Compose: 1.13.0 +
Check that you have the correct docker version, with docker compose too,
if you have linux OS, you have to do it separately:

```
$ docker --version
Docker version 18.03.0-ce, build 0429c243o2
$ docker-compose --version
docker-compose version 1.20.1, build 0429c243o2
```

If not installed yet, follow the official guide in https://docs.docker.com/install/ and docker-compose here: https://docs.docker.com/compose/install/

### Windows Users only

If you are a Linux users, you are good to go, if you are a windows user, im sorry mate, but you need to follow 
the next steps and guides for preparing the deployment.

Set docker for using WSL, following the next guide:
https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly

If you are using Docker Toolbox, because of your Windows build version, you might need to look 
https://gist.github.com/strarsis/44ded0d254066d9cb125ebbb04650d6c for set docker right.

We have already set docker in our WSL, so next we need to make our dev environment properly for our platform.
Windows users for now on, you will work in your new Ubuntu WSL console.

### Python

You need to have install python, check it by using:

```
$ python -V
```
If you have not python, follow the next [guide](https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/)

### Postgresql

Make sure you have postgres 10 with:

```
$ sudo apt-get install -y postgresql-client-10
$ psql --version  
```

### Anyenv

Install this tool, [anyenv](https://github.com/anyenv/anyenv) to have a develop environment.
Make sure that even you close your current console, anyenv persist.

### Developer environment

Now the Linux users can join us, use your WSL if you are Windows user, we need to prepare a develop environment for the server to execute.

Install some packages that we will need later:

```
sudo apt-get update
```
```
sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev binutils libproj-dev gdal-bin
```

Clone the repository:
```
git clone https://github.com/SmartTrafficPY/smartcity-asuncion.git
```
Go to directory of the repository and then, we can install python version 3.7.2 and pip with:
```
cd .../smartcity-asuncion
```

### Python environment

Create a python 3.7.2 environment with:

```
$ pyenv install 3.7.2
$ pip install -U pip
```

Install pipenv:
```
$ pip install pipenv
```
Install the dependencies stated in the pipfile:
```
$ pipenv install --dev
```

And now you can enter pipenv shell 

```
pipenv shell
```
In pipenv shell execute

```
pre-commit install
```
The last one is optional, but will help you, not letting you commit horrible code.

## Deployment

Make sure you have the requirements versions of the session before continue with this README.

Build the container:
```
$ docker-compose build
```

Restart the service:
```
$ docker-compose down
$ docker-compose up 
```

If it is the first time running the project, you'll need to create the database.
The database is created with:

```
python manage.py createdb
```

You'll find the app is running on http://127.0.0.1:8000
or in the docker VM if you are running in docker toolbox, that you may known with the following command

```
$ docker-machine ip
$ 132.145.199.13
```

## SmartParking: understanding server requests
This rant assumes the service is available at 127.0.0.1, port 8000.

### User Management
The platform works with:
- session-based authentication
- token-based authentication (the DRF simple ones)

All requests must be authenticated. Superusers and staff can perform all requests.

Your app needs to use credentials that represent the app itself (as opposed to a normal user account) to perform:

#### List users:
GET /smartparking/users/
```
$ curl -H "Authorization: Token aTokenForTheSmartParkingApp" -iX GET http://127.0.0.1:8000/smartparking/users/
```
(you'll get a long JSON array)


#### Create a user:
POST /smartparking/users/
```
$ curl -d '{"username": "normal_user", "password": "superSecretPassword", "smartparkingprofile": {"birth_date": "2009-01-01", "sex": "M"}}' -H "Content-Type: application/json" -H "Authorization: Token aTokenForTheSmartParkingApp" -iX POST http://127.0.0.1:8000/smartparking/users/

HTTP/1.1 201 Created
Date: Sun, 01 Sep 2019 17:13:01 GMT
Server: WSGIServer/0.2 CPython/3.7.2
Content-Type: application/json
Location: http://127.0.0.1:8000/smartparking/users/1234/
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 181

{"url":"http://127.0.0.1:8000/smartparking/users/1234/","username":"normal_user","smartparkingprofile":{"birth_date":"2009-01-01","sex":"M"}}
```

Get the URL in the `Location:` header to manipulate the user instance you just created.

#### Retrieve a user's token:
```
curl -d '{"username": "normal_user", "password": "superSecretPassword"}' -H "Content-Type: application/json" -H "Authorization: Token aTokenForTheSmartParkingApp" -X POST http://127.0.0.1:8000/smartparking/auth-token/

{"token":"normalUserToken", "url":"http://127.0.0.1:8000/smartparking/users/1234/"}
```


If you want to modify user details, you need to authenticate as that user (or as a superuser or staff).

#### Change user information:
PATCH /smartparking/users/_someUserId_
```
$ curl -d '{"password": "aBetterSuperSecretPassword"}' -H "Content-Type: application/json" -H "Authorization: Token normalUserToken" -iX PATCH http://127.0.0.1:8000/smartparking/users/1234/

HTTP/1.1 200 OK
Date: Sun, 01 Sep 2019 18:10:03 GMT
Server: WSGIServer/0.2 CPython/3.7.2
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 139

{"url":"http://127.0.0.1:8000/smartparking/users/1234/","username":"normal_user","smartparkingprofile":{"birth_date":"2009-01-01","sex":"M"}}
```

## Some notes regarding docker on windows 
If you are getting this error, `docker : /bin/sh^M: bad interpreter: No such file or directory`
You would like to see this page to solve it: https://forums.docker.com/t/error-while-running-docker-code-in-powershell/34059

Other thing that might be useful is restarting docker, that may solve some troubles of network.

```
$ docker-machine restart
```




deploy
define postgres.env and smartcity.env

docker-compose run smartcity python manage.py createdb
docker-compose run smartcity python manage.py migrate
docker-compose run smartcity python manage.py loaddata initial
docker-compose run smartcity python manage.py createsuperuser


docker-compose run smartcity python manage.py migrate
docker-compose run smartcity /build-staticfiles.sh

loading spots
cat spots.geojson | docker-compose run smartcity python manage.py loadspots 1
