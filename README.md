# CI/CD

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

Everything that starts with a hastag # is a comment in yaml files.
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
