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





## Jenkins WSL Installation

Make an apt update
```
sudo apt update
```

Install Java RunTime Environment (JRE)

```
sudo apt install default-jdk default-jre
```

Test if java is installed

```
javac
```

Setup GPG keys of the Jenkins repository

```
wget -q -0 - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
```

Add Jenkins repository

```
sudo sh -c "echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list"
```

Make an apt update before installing, since you just add a new repository,

```
sudo apt update
```

Install Jenkins via apt

```
sudo apt install jenkins
```

Start Jenkins services by

```
sudo /etc/init.d/jenkins start
```

Launch your browser and navigate to

```
http://{your_ip}:8080
```

Here you are, your personal Jenkins in WSL!!! At the first time you launch your Jenkins, you will need an initial admin password, just “more” this,

```
sudo more /var/lib/jenkins/secrets/initialAdminPassword
```
