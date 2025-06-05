Steps
-----

Build container:
-----------------
./build.sh


Run container:
---------------
container1=$(./run.sh)
curl http://localhost:5000/


container2=(./updated-run.sh)
curl http://localhost:5001/
curl http://localhost:5001/greetings
curl http://localhost:5001/listcontents


See container logs:
--------------------
docker logs $container1
docker logs $container2


Stop container:
---------------
docker stop $container1
docker stop $container2
