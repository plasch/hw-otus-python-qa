#!/bin/bash

docker build -t tests .
docker run --name tests_run --network selenoid tests pytest --browser chrome -n 2
docker cp tests_run:/app/allure-results .
allure serve allure-results
docker rm tests_run
