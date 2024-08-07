# Data-fetch
## Start the app using the following commands using flask command
1) Install virtual env using the command 
    $ python3 -m venv .venv
2) Activate the virtual env using the command
    $ source .venv/bin/activate
3) Install the dependencies from the requirements file with the following command
    $ pip install -r requirements.txt
4) Run the flask app using the following command from the root of project
    $ flask --app app.py run --debug
    the above command will run the flask app on http://127.0.0.1:5000 
5) Import the postman collection for the endpoints
    -  http://127.0.0.1:5000/fetch-data -> to get the shopify mock data
    -  http://127.0.0.1:5000/get-processed-data - pass the data from above response and pass it as body in the second endpoint to get the values of the json in lowercase

## Using docker container
1) Build the docker container with the following command
    $ sudo docker build . -t data
2) Run the docker container with the following command to hit the endpoints using the app running inside container
    $ sudo docker run -d -p 8080:8080 data
    -  call http://0.0.0.0:8080/fetch-data -> to get the shopify mock data from inside container.
    -  http://0.0.0.0:8080/get-processed-data - pass the data from above response and pass it as body in the second endpoint to get the values of the json in lowercase from inside container.