# **Structure of `SETUP_JENKINS_DOCKER.md`**

# Jenkins and Docker Setup
## Reference: https://www.jenkins.io/doc/book/installing/docker/

Follow these steps to set up Jenkins and Docker for CI/CD:

## 1. Configure Docker for Windows
- Switch to Linux containers in Docker Desktop.
- Enable Docker Experimental Features (optional).

## 2. Create a Docker Network
```bash
docker network create jenkins
```

## 3. Run Docker-in-Docker (DinD) Container
```bash
   docker run --name jenkins-docker --rm --detach ^
  --privileged --network jenkins --network-alias docker ^
  --env DOCKER_TLS_CERTDIR=/certs ^
  --volume jenkins-docker-certs:/certs/client ^
  --volume jenkins-data:/var/jenkins_home ^
  --publish 2376:2376 ^
  docker:dind
```
### Attributes and Commands Explained

- docker run:
  - Starts a new Docker container.

- --name jenkins-docker:
  - Assigns the name jenkins-docker to the container for easy reference.

- --rm:
  - Automatically removes the container when it stops. This is useful for temporary containers.

- --detach (or -d):
  - Runs the container in the background (detached mode).

- --privileged:
  - Gives the container elevated privileges, allowing it to run Docker commands inside the container (required for DinD).

- --network jenkins:
  - Connects the container to the jenkins Docker network (created earlier).

- --network-alias docker:
  - Assigns the alias docker to the container within the jenkins network. This allows Jenkins to connect to the DinD container using the hostname docker.

- --env DOCKER_TLS_CERTDIR=/certs:
  - Sets the environment variable DOCKER_TLS_CERTDIR to /certs. This tells Docker to store TLS certificates in the /certs directory.

- --volume jenkins-docker-certs:/certs/client:
  - Mounts a Docker volume named jenkins-docker-certs to /certs/client inside the container. This stores TLS certificates for secure communication.

- --volume jenkins-data:/var/jenkins_home:
  - Mounts a Docker volume named jenkins-data to /var/jenkins_home inside the container. This stores Jenkins data (e.g., configurations, jobs).

- --publish 2376:2376:
  - Exposes port 2376 on the host and maps it to port 2376 in the container. This is the Docker daemon’s TLS port.

- docker:dind:
  - Specifies the Docker image to use (docker:dind), which is the official Docker-in-Docker image.

4. Create a Custom Jenkins Image
   1. Create a Dockerfile, in any place of your computer to create the image below:
   ```dockerfile
   FROM jenkins/jenkins:2.492.2-jdk17
   USER root
    RUN apt-get update && apt-get install -y lsb-release
    RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
      https://download.docker.com/linux/debian/gpg
    RUN echo "deb [arch=$(dpkg --print-architecture) \
      signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
      https://download.docker.com/linux/debian \
      $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
    RUN apt-get update && apt-get install -y docker-ce-cli
    USER jenkins
    RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
   ```
   ### Attributes and Commands Explained
- FROM jenkins/jenkins:2.492.2-jdk17:
  - Specifies the base image (jenkins/jenkins:2.492.2-jdk17), which is the official Jenkins image with JDK 17.

- USER root:
  - Switches to the root user to perform administrative tasks.

- RUN apt-get update && apt-get install -y lsb-release:
  - Updates the package list and installs the lsb-release package, which provides information about the Linux distribution.

- RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc ...:
  - Downloads the Docker GPG key and saves it to /usr/share/keyrings/docker-archive-keyring.asc.

- RUN echo "deb [arch=$(dpkg --print-architecture) ...:
  - Adds the Docker repository to the system’s package sources list.

- RUN apt-get update && apt-get install -y docker-ce-cli:
  - Updates the package list and installs the Docker CLI (docker-ce-cli).

- USER jenkins:
  - Switches back to the jenkins user for security reasons.

- RUN jenkins-plugin-cli --plugins "blueocean docker-workflow":
  - Installs Jenkins plugins (blueocean and docker-workflow) using the jenkins-plugin-cli tool.


   2. Build the image:
   ```bash
      docker build -t myjenkins-blueocean:2.492.2-1 .
   ```
5. Run the Custom Jenkins Container
```bash
    docker run --name jenkins-blueocean --restart=on-failure --detach ^
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 ^
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 ^
  --volume jenkins-data:/var/jenkins_home ^
  --volume jenkins-docker-certs:/certs/client:ro ^
  --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.492.2-1
```
### Attributes and Commands Explained

- docker run:
  - Starts a new Docker container.

- --name jenkins-blueocean:
  - Assigns the name jenkins-blueocean to the container.

- --restart=on-failure:
  - Automatically restarts the container if it fails.

- --detach (or -d):
  - Runs the container in the background (detached mode).

- --network jenkins:
  - Connects the container to the jenkins Docker network.

- --env DOCKER_HOST=tcp://docker:2376:
  - Sets the DOCKER_HOST environment variable to tcp://docker:2376. This tells Jenkins to connect to the Docker daemon running in the jenkins-docker container.

- --env DOCKER_CERT_PATH=/certs/client:
   - Sets the DOCKER_CERT_PATH environment variable to /certs/client. This tells Jenkins where to find the TLS certificates for secure communication.

- --env DOCKER_TLS_VERIFY=1:
  - Enables TLS verification for secure communication with the Docker daemon.

- --volume jenkins-data:/var/jenkins_home:
  - Mounts the jenkins-data volume to /var/jenkins_home inside the container. This stores Jenkins data (e.g., configurations, jobs).

- --volume jenkins-docker-certs:/certs/client:ro:
  - Mounts the jenkins-docker-certs volume to /certs/client inside the container as read-only (ro). This provides access to the TLS certificates.

- --publish 8080:8080:
  - Exposes port 8080 on the host and maps it to port 8080 in the container. This is the Jenkins web UI port.

- --publish 50000:50000:
  - Exposes port 50000 on the host and maps it to port 50000 in the container. This is used for Jenkins agent communication.

- myjenkins-blueocean:2.492.2-1:
  - Specifies the custom Jenkins image to use (myjenkins-blueocean:2.492.2-1), which was built earlier.

7. Access Jenkins
   1. Open http://localhost:8080.

   2. Retrieve the initial admin password:
   ```
   docker logs jenkins-blueocean
   ```
   3. Complete the Jenkins setup wizard.

7. Configure Jenkins for Your Project
Install the required plugins:

    - Docker Pipeline Plugin
    - Git Plugin 
    - Pipeline Plugin 
    - Blue Ocean Plugin (optional).

8. Run the Pipeline
