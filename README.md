mincoinchange
=============
A Python Web-app for Google App Engine. It computes the minimum number of coins to create change, when the different 
denominations are given as input and the value as input.

* URL:/getgender?name=<input name>
* returns: Json object with name and the predicted gender
Note: <input name> is the place to input the name

Example usage:
* Go to the url
* Login with your google credentials
* In this page enter the list of denominations and



## Docker Notes
Download this continer and then
```
gzip -d proj1.tar.gz
docker import proj1.tar
```

Run `/startme.sh` in the docker container to start the web server.

Example starting this container:
```
docker run -it cloudcomp /startme.sh
```
* This will start the container and the webserver.
* Then test it using
```
curl http://localhost:80/getgender?name=sandra
```

Future work:
=============
* We can further work towards adding localizations to the names, like chinese or danish.
* Also we can add provisions for putting multiple names in a single request

