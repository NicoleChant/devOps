# CI/CD

## Introduction

In software engineering, CI/CD or CICD is the combined practices of continuous integration (CI) and continuous deployment (CD).

CI/CD bridges the gaps between development and operation activities and teams by enforcing automation in building, testing and deployment of applications. CI/CD services compile the incremental code changes made by developers, then link and package them into software deliverables. Automated tests verify the software functionality, and automated deployment services deliver them to end users.

The aim of CI/CD is to:
- increase early defect discovery,
- increase productivity, and
- provide faster release cycles.

The process contrasts with traditional methods where a collection of software updates were integrated into one large batch before deploying the newer version. Modern-day DevOps practices involve continuous development, continuous testing, continuous integration, continuous deployment and continuous monitoring of software applications throughout its development life cycle.

### CI

Continuous integration (CI) is the practice of merging all developers' working copies to a shared mainline several times a day. Grady Booch first proposed the term CI in his 1991 method.

When embarking on a change, a developer takes a copy of the current code base on which to work. As other developers submit changed code to the source code repository, this copy gradually ceases to reflect the repository code

The longer development continuous on a branch without merging back to the mainline, the great the risk of multiple integration conflicts and failures when the developer branch is eventually merged back.


### CD

Continuous deployment (CD)


### CI/CD with Github Actions ❤️


Whenever we create a new repository on github we can see a tab named "Actions".

Let's create a new repository.

```
gh create repo
```

You can clone locally the current repository for the purposes of this challenge. We will try to build an API which provides real time data about current laptop prices available in the market by utilizing Pythons FastAPI module. We will scrape these data from the large greek website Skroutz by utilizing the following link "https://www.skroutz.gr/c/25/laptop.html?o=laptop".

If you don't follow the code 100% don't worry about it. The purpose of this challenge is to teach us the basic pillars of CI/CD workflow.

We can run the api locally by running
```
uvicorn <name of the module>:<name of the API object> --reload
```

In our case, we will run
```
uvicorn app:app --reload
```

Lets go to Github Actions tab. We can already see some templates related to the task we want to perform. We will use Python application template. Let's configure!

We can see an automatically generated template yaml file which will perform the CI/CD workflow for us.
We will try to decipher this template step by step but let's first make an important remark.
When we work in our project we can simply create a .github/workflows directory within our existing repo. Then we can add the .yaml file which we want to monitor our CI/CD process. Hence, we can simply run

```
mkdir -p .github/workflows && touch .github/workflows/$(workflowName).yml
```

Then we can modify the workflow yaml to achieve our CI/CD. When we add, commit and push the changes, github will run the instructions present in the yaml file.

Let's try to decipher the generated workflow yaml file.

```
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
```

First we have the name of the workflow. The name is OPTIONAL. These are the events Github recognizes:

```
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```

"on" is REQUIRED! Everytime an event occurs (event-driven programming) Github TRIGGERS the workflow.
The class "on" is where we define events that will trigger the workflow. In our current example, everytime someone pushes to main branch or a pull_request is being made on main branch the workflow is being triggered.
Other events could be creating an issue.

You can see a complete list of events that trigger workflows on the following link:

https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

The jobs section is being executed when an event in the "on" section occurs. We have jobs and the names of the job appear as members of the class and groups a set of actions that weill be executed.

```
jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
```

actions path in github are were predefined actions are hosted. Insofar lets see whats happening

```
name: Optional
on: Required
jobs: Required
  - one or more jobs job.job_id
  - sequence of tasks (steps)
  - steps can run commands, setup tasks OR run an action
  uses - selects an action
under path action the reusable code is hosted
```

The second step is setting up a python environment with the specified version. Then we use a prespecified yaml file which has the necessary instructions to setup python environment. The final with: specifies the python version we want to use.

Whenever we are reffering to an action we write "uses:". When we use a unix command we write "run:".

## YAML

Yaml is a data serialization language like XML & JSON

- standard format to transfer data
- extensions: .yaml .yml

### Introduction


key-value pairs

```
app: user-authentication
port: 9000
version: 1.7
```

Everything that starts with a hashtag # is a comment in yaml files.
We can create an object 'microservice' by identing (tabbing) the block that follows:

```
microservice:
  app: user-authentication
  port: 9000
  version: 1.7
```

In yaml true is also equivalent to yes or on and false to no and off.
Lists are declared by a dash -

```
microservice:
  - app: user-authentication
    port: 9000
    version: 1.7
    deployed: false
  - app: shopping-cart
    port: 9002
    versions:
    - 1.9
    - 2.0
    - 2.1
```

We can also express a list as follows: versions: [1.9, 2.0, 2.1]

```
microservices:
  - user-authentication
  - shopping-cart
```
