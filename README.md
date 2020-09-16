# BOOTSTRAP-PY #

Simple Rest API contained in docker.


### Executing

To run the solution, at project root, execute 

docker-compose up --build



### Developing

For development after executing docker-compose, if on a wait status service, e.g. REST, all files while saved wont do an automatic re-run of the code.
Although the file app/init.dev.sh is still included in the package, the docker compose file should be changed by replacing: command:  python do.py with

        command: >
                /bin/bash -c "/app/init.dev.sh
                "


So for alive services, docker-compose should be turned down then turned up again to see changes of the code being executed.



### Testing

Tests are named test_* and are inside app/tests/ folder

To run the solution, at project root, execute 

docker-compose -f tests/docker-compose.yml up --build

Project is using unittest from Python

Check for assert methods here https://docs.python.org/3/library/unittest.html#assert-methods





