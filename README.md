# BOOTSTRAP-PY #

Boostrap development project for container based Sensefinity Cloud services built in Python.





### What is this repository for? ###

* Everytime a new service needs to be built, this can be a proper base to start with
  
* This service serves as a base assessment for company engineers candidates




### How do I get set up? ###

* git clone git@gitlab.com:sensefinity/support/bootstrap-py.git

rename the folder to your project name

* mv bootstrap-py the-new-name

move in to the folder

* cd the-new-name

and remove the .git folder

* rm -fr .git

now the project have no connection with the original repository, to have it in a new repository create a new project at Gitlab and follow the described steps



### Main files to checkout nomenculatures ###

* Dockerfile

SERVICE_NAME=bootstrap-py
SERVICE_DESC='Boostrap project for Python based services' \
SERVICE_TAGS='local,local-test,sens8,sensefinity-bootstrap-py,bootstrap-py' \


* docker-compose.yml

services:
  bootstrap-py:
  image: local/bootstrap-py  



### Available connectors if needed ###

* Elasticsearch

https://elasticsearch-py.readthedocs.io/en/master/


* Kafka

https://github.com/dpkp/kafka-python


* Redis

https://pypi.org/project/redis/




### Executing

To run the solution, at project root, execute 

docker-compose up --build




### Developing

For development after executing docker-compose, if on a wait status service, e.g. REST, all files while saved will do an automatic re-run of the code thanks to the file app/init.dev.sh 

So for alive services, no need to turn down docker-compose and turn up again to see changes of the code being executed.




### Testing

Tests are named test_* and are inside app/tests/ folder

To run the solution, at project root, execute 

docker-compose -f tests/docker-compose.yml up --build

Project is using unittest from Python

Check for assert methods here https://docs.python.org/3/library/unittest.html#assert-methods





