<!--- STARTEXCLUDE --->
# Build a Blog With Django and Astra DB
*15 minutes, Intermediate, [Start Building](https://github.com/DataStax-Examples/django-cassandra-blog/blob/master/README.md#quick-start)*

Learn how to build a blog application with Django and connect it to Astra DB by following along with Tomi's video, located [here](https://youtu.be/JH24exA7-CA).
<!--- ENDEXCLUDE --->

![image](https://raw.githubusercontent.com/DataStax-Examples/django-cassandra-blog/master/hero.png)

## Quick Start
<!--- STARTEXCLUDE --->
* [Signup for DataStax Astra](https://dtsx.io/3z81JIa), or login to your already existing account. 
* [Create an Astra DB Database](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#create-an-astra-db) if you don't already have one.
<!--- ENDEXCLUDE --->
* [Create an Astra DB Keyspace](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#create-an-astra-db-keyspace) called `sag_tech_blog` in your database.
* [Generate an Application Token](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#create-an-application-token) with the role of `Database Administrator` for the Organization that your Astra DB is in.
* Click the 'Open in Gitpod' link: [![Open in IDE](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/DataStax-Examples/django-cassandra-blog)
* Once the app is finished launching in the Gitpod IDE, copy the `env.example` file to a file named `.env` and fill the required values in from your Application Token and [Astra DB connection settings](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#get-your-astra-db-connection-settings). (The Django setting `SECRET_KEY` is unrelated to Astra and can be any alphanumeric string.)
* Get your [secure connect bundle](https://github.com/DataStax-Examples/sample-app-template/blob/master/GETTING_STARTED.md#get-an-astra-db-secure-connect-bundle) from the connect page of your database and upload it to your Gitpod instance. Rename it to `bundle.zip`. (To upload the file, drag-and-drop it to the Explorer section of your Gitpod window.)
* Create the project tables in Astra DB by running this command in the console:
```bash
python manage.py syncdb
```
* Run the Django project by running this command in the console:
```bash
python manage.py runserver
```
* The app should open in a new browser tab by itself (if it doesn't, check your popup blocker). If you are on Gitpod,
its URL will be something like `https://8000-sapphire-sailfish-wfxezcum.ws-eu18.gitpod.io/`; if you are running locally,
open `http://127.0.0.1:8000/` in your browser instead.

## Objectives
* Work through a video tutorial to build a blog with Django and Astra DB
  
## How this works
Follow along in this video tutorial: [https://youtu.be/JH24exA7-CA](https://youtu.be/JH24exA7-CA).
