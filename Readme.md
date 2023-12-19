create the docker with: 

docker build . --tag pokeapi

run the docker with 

docker run -p 80:80 -p 81:81 -it pokeapi

in the docker exec run:

docker exec <constainer-id> /usr/sbin/nginx
