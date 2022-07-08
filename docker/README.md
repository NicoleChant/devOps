## Docker on WSL

### Installation

### Containers

Container is a running environment for an IMAGE

### Main Docker Commands

- docker images : lists all the available docker images
- docker run <image_name> : runs the docker image
- docker ps : status of all the running docker containers
- docker stop <container_id>: stops docker container
- docker ps -a : all the containers
- docker start <container_id>: starts docker container
- docker build --tag=image-name .
- docker run -it -e PORT=8000 -p 8000:8000 image-name sh

### Dockerfile

#### Most common instructions

- FROM: selects a base image for our image (the environment in which we will run the code), this usually is
the first instruction
- COPY : copies files and directories inside the image.
For instance, . /home/app copies all the files of the CURRENT directory and places them in /home/app directory
First parameter of the COPY command refers to the HOST and the second parameter to the source destination.

- RUN : executes any Linux command inside the image being built


- CMD : executes an entry point linux command

```
RUN mkdir -p /home/app
COPY . /home/app
CMD ["uvicorn" , "app:app --reload"]
```


### Docker Secrets

```
docker swarm init
docker info
docker secret create <secret_name> <path_to_file>
docker secret ls
docker secret inspect <secret_name>
```

or

```
echo $client_id | docker secret create client_id -
```

### Automatic Merge Github Actions

```
name: Close Pull Request

# only trigger on pull request closed events


on:
  pull_request:
    types: [ closed ]

jobs:
  merge_job:
    # this job will only run if the PR has been merged
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
    - run: |
        echo PR #${{ github.event.number }} has been merged


  close_job:
    # this job will only run if the PR has been closed without being merged
    if: github.event.pull_request.merged == false
    runs-on: ubuntu-latest
    steps:
    - run: |
        echo PR #${{ github.event.number }} has been closed without being merged
```



### Heroku CD

Login on Heroku

```
heroku login
```

Create Heroku APP

```
heroku create <package_name> --region eu
heroku create info
```

```
git remote -v
```

```
git remote rm <remote_name>
```
```
heroku git:remote -a project
```

should display

```
heroku  https://git.heroku.com/parsecraft.git (fetch)
heroku  https://git.heroku.com/parsecraft.git (push)
origin  git@github.com:NicoleChant/parsecraft.git (fetch)
origin  git@github.com:NicoleChant/parsecraft.git (push)
```

To scale dynos

```
heroku ps:scale web=1 --app <package_name>
```

#### Create Procfile

```
touch Procfile && echo 'web: pip install . -U && <package_name>-run' >> Procfile
```


#### CD Heroku

- keep in mind you also need to configure Heroku HEROKU_API_KEY and HEROKU_EMAIL in GitHub secrets
- and replace REPLACE_WITH_YOUR_HEROKU_APP_NAME in this file with the name of your Heroku app

```
  deploy_heroku:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - uses: akhileshns/heroku-deploy@v3.0.4 # This is the action
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "REPLACE_WITH_YOUR_HEROKU_APP_NAME" # Must be unique in Heroku
        heroku_email: ${{secrets.HEROKU_EMAIL}}
```

### Heroku Secrets

HEROKU API KEY

👉 Go to your Heroku account and generate or copy (Reveal) your API key.

👉 Store it as a Secret on your GitHub repository under Settings then Secrets
=> name it HEROKU_API_KEY and paste the API key that you copied from Heroku

HEROKU EMAIL

👉 Store it as a Secret on your GitHub repository under Settings then Secrets
=> name it HEROKU_EMAIL and save the email that you are using in order to login on Heroku

👉 Then from the Terminal, inside of your project, update your code, push it to GitHub and se

 echo $client_id | heroku config:set client_id=$_

 heroku config:get GITHUB_USERNAME

 heroku config:get client_secret
