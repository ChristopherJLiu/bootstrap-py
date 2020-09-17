# BOOTSTRAP-PY #

Simple Rest API using Redis as cache and contained using Docker.
Checks if the requested data is in cache and return the data, if not makes a request to OpenWeather and stores in cache and returns the data.

Its the same as master branch only difference that is this cache is made using Redis instead of storing a JSON file

### Executing

To run the solution, at project root, execute 

docker-compose up --build

After the API is running to get weather of a city do:
http://localhost:5656/weather/city/3448433 which will request São Paulo Brazil weather (3448433 number is dynamic)

To get another cities go to : https://openweathermap.org/ search for a city and copy the city id


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








