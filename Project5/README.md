1. The /etc/hosts file is setup with a private IP and the corresponding hostname. E.g. `10.0.0.20 Nate`
2. I opened 3 terminals and used "sudo ssh -i /path/to/key ubuntu@relevant_public_ip" to connect to each system. The systems talk to each other thanks to the hosts file.
3. To setup and configure HAProxy, I first used `sudo apt-get install haproxy`. I then restarted the machine. 
   - Then, I modified the configuration file at `/etc/haproxy/haproxy.cfg`. I configured the "frontend" to be bound to the proxy machine via private ip. I also configured it to use the default backend of the backend I named "web servers". For the backend, I specified each ubuntu server running apache2's private ip address. I formatted it so that the server name in the configuration file is the same as the hostname on the machine. 
   - I restarted the service using `$sudo systemctl restart haproxy.service`.
   - I used the lectures from Professor Kayleigh Duncan on 11/8/2021 and 11/10/2021, as well as https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/.
4. To setup and configure Apache2, I used `sudo apt-get install apache2`. I then restarted the machine(s). 
   - I deleted the contents of the file at `/var/www/html/index.html` and replaced them with the provided text for each server.
   - I restarted the apache2 service using `$sudo systemctl reload apache2`.
   - I made no further changes to the apache2 service.
   - I used this website as a resource https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
5. Pictures
![server 1](Images/sofarsogood.PNG)
![server 2](Images/success.PNG)
