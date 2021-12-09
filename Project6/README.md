# Part 1
I installed docker by following their instructions for installing from the official repository. Steps for adding the repository can be found here: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository.<br>
Then I ran `$sudo apt-get update` and `$sudo apt-get install docker-ce docker-ce-cli containerd.io`.<br>
The Dockerfile for building the container image should look something like the following.<br>
> FROM ubuntu:18.04
> 
> RUN apt update && apt install -y apache2
> 
> COPY website/index.html /var/www/html
> 
> EXPOSE 80

With the Dockerfile ready, build the image with `$docker build -t site:1.0 path/to/dockerfile`.<br>
Once the image has been created, run it with the following command `$docker run -dit -p 80:80 site`.<br>
Since COPY uses absolute paths, my version of index.html will overwrite the version found in /var/www/html.<br>
To view a running version of this project, open a web browser and enter the IP address associated with the container. You may or may not need to specify port 80, depending on your browser and network security settings. 
# Part 2

# Part 3
