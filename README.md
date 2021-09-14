<!--- STARTEXCLUDE --->
# Build a Blog With Django and Astra DB
*15 minutes, Intermediate, [Start Building](https://github.com/DataStax-Examples/django-cassandra-blog/blob/master/README.md#prerequisites)*

Learn how to build a blog application with Django and connect it to Astra DB by following along with Tomi's video, located [here](https://youtu.be/JH24exA7-CA).
<!--- ENDEXCLUDE --->

![image](https://raw.githubusercontent.com/DataStax-Examples/django-cassandra-blog/master/hero.png)

## Objectives
* Work through a video tutorial to build a blog with Django and Astra DB
  
## How this works
Follow along in this video tutorial: [https://youtu.be/JH24exA7-CA](https://youtu.be/JH24exA7-CA).

## Get Started
To build and play with this app, follow the build instructions that are located here: [https://github.com/DataStax-Examples/django-cassandra-blog/blob/master/README.md#prerequisites](https://github.com/DataStax-Examples/django-cassandra-blog/blob/master/README.md#prerequisites)

<!--- STARTEXCLUDE --->
# Running Build a Blog With Django and Astra DB
Follow the instructions below to get started.

## Prerequisites
Let's do some initial setup by creating a serverless(!) database.

### DataStax Astra
1. Create a [DataStax Astra account](https://dtsx.io/3z81JIa) if you don't already have one:
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-register-basic-auth.png)

2. On the home page. Locate the button **`Create Database`**
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-dashboard.png)

3. Locate the **`Get Started`** button to continue
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-select-plan.png)

4. Define a **database name**, **keyspace name** and select a database **region**, then click **create database**.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-create-db.png)

5. Your Astra DB will be ready when the status will change from *`Pending`* to **`Active`** 💥💥💥 
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-active.png)

6. After your database is provisioned, we need to generate an Application Token for our App. Go to the `Settings` tab in the database home screen.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-settings.png)

7. Select `Admin User` for the role for this Sample App and then generate the token. Download the CSV so that we can use the credentials we need later.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-settings-token.png)


8. After you have your Application Token, head to the database connect screen and select the driver connection that we need. Go ahead and download the `Secure Bundle` for the driver.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-connect-bundle.png)

9. Make note of where to use the `Client Id` and `Client Secret` that is part of the Application Token that we generated earlier.
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/astra-db-connect-bundle-driver.png)

### Github
1. Click `Use this template` at the top of the [GitHub Repository](https://github.com/DataStax-Examples/django-cassandra-blog):
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/github-use-template.png)

2. Enter a repository name and click 'Create repository from template':
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/github-create-repository.png)

3. Clone the repository:
![image](https://raw.githubusercontent.com/DataStax-Examples/sample-app-template/master/screenshots/github-clone.png)

## 🚀 Getting Started Paths:
*Make sure you've completed the [prerequisites](#prerequisites) before starting this step*
  - [Running on Gitpod](#running-on-gitpod)

### Running on Gitpod
1. Click the 'Open in Gitpod' link:
[![Open in IDE](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/DataStax-Examples/django-cassandra-blog)
2. Upload the secure-connect-bundle that you downloaded previously to the gitpod project explorer.
3. When the environment is available, copy `.env.example` to `.env` and enter your secrets from the token that you acquired earlier. Also, add the path to the secure-connect-bundle that you uploaded in the previous step.
4. Create the project tables in Astra DB by running this command in the console:
```bash
python manage.py syncdb
```
5. Run the Django project by running this command in the console:
```bash
python manage.py runserver
```
<!--- ENDEXCLUDE --->