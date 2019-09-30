# macadder
A dockerised Flask application to simplify the process of adding MAC addresses to CISCO Wireless Lan Controller (WLC) & Unifi Whitelists. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them

```
Docker
---OR---
*NIX, python3, pip3
```

### Installing

A step by step series of examples that tell you how to get a development env running

#### For Docker:

```
cd macadder
docker build --rm -t macadder .
docker docker run -d --rm --name macadder -p 5000:5000 macadder
```
Now visit localhost:5000/ in your browser and you should see macadder!

#### Using Python:

The following instructions apply for Debian based systems like Ubuntu, but feel free try the equivalent on your operating system.
```
apt-get update && apt-get install -y libsasl2-dev libldap2-dev libssl-dev gcc
cd macadder
pip3 install --no-cache-dir -r requirements.txt
gunicorn -b 0.0.0.0:5000 wsgi:app
```
Now visit localhost:5000/ in your browser and you should see macadder!


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used.
* [Paramiko](http://www.paramiko.org/) - SSH Library.
* [PyUnifi](https://github.com/finish06/pyunifi) - A Python Library for interacting with Unifi Controllers.
* [python-ldap](https://www.python-ldap.org/en/latest/) - An object-oriented API to access LDAP directory servers from Python programs.
* [Gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX.

## Authors

* **Aidan Stansfield** - *Initial work* - [aidanstansfield](https://github.com/aidanstansfield)

See also the list of [contributors](https://github.com/aidanstansfield/macadder/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
