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


### Dockerfile

- RUN : executes any Linux command
- COPY . /home/app : copies all files of the current directory and places them in /home/app directory

First parameter of the COPY command refers to the HOST and the second parameter to the source destination.

- CMD : executes an entry point linux command

```
RUN mkdir -p /home/app
COPY . /home/app
CMD ["uvicorn" , "app:app --reload"]
```
