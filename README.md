# BOOTSTRAP-PY #

Simple Rest API contained using docker.


### Executing

To run the solution, at project root, execute 

docker-compose up --build

After the API is running to get weather of a city do:
http://localhost:5656/weather/city/3448433 which will request São Paulo Brazil weather (3448433 number is dynamic)

To get another cities go to : https://openweathermap.org/ and search a city and copy the city id


### Developing

Although the file app/init.dev.sh is included in the package, the docker compose file should be changed by replacing: command:  python do.py with the following so it updates after changes.

        command: >
                /bin/bash -c "/app/init.dev.sh
                "


So at the moment docker-compose should be turned down then turned up again to see changes of the code being executed.



### Testing

Tests are named test_* and are inside app/tests/ folder

To run the solution, at project root, execute 

docker-compose -f tests/docker-compose.yml up --build

Project is using unittest from Python

Check for assert methods here https://docs.python.org/3/library/unittest.html#assert-methods





