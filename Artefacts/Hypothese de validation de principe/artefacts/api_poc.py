# coding: utf-8
import os, sys
# importing the requests library
import requests
import time
import random
from faker import Faker

fake = Faker()
URL = "http://localhost:8999/hospital/reserve_bed"
types = [u"radiologie", u"réanimation"]
duration = 0
headers = {"Content-type: application/json"}

def high_request_amount(nb_of_requests):
  # defining a params dict for the parameters to be sent to the API
  duration = 0
  report = ""

  for x in xrange(1,nb_of_requests):
    gps_position = "47.2108967,-1.5533024"
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = full_name[1]
    chosen_type = random.choice(types)
    url = URL + '?gps_position=&{gps_position}department_type={chosen_type}'.format(gps_position=1, chosen_type=2)
    PARAMS = {'firstName':first_name, 'lastName' :last_name}
    start = time.time()
    response = requests.get(url = URL, params = PARAMS)
    end = time.time()
    request_duration = end - start
    duration += request_duration
    report += '{text} with a duration of {request_duration}s \n'.format(text=response.text, request_duration=request_duration)
  report += '{nb_of_requests} requests. Total duration of {total_duration}s'.format(nb_of_requests=nb_of_requests, total_duration=duration)
  with open('numerous_requests.txt', 'w') as f:
    f.write(report)

high_request_amount(100)

def avg_response_time(nb_of_requests):
  # defining a params dict for the parameters to be sent to the API
  duration = 0
  report = ""


  for x in xrange(1,nb_of_requests):
    gps_position = "47.2108967,-1.5533024"
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = full_name[1]
    chosen_type = random.choice(types)
    url = URL + '?gps_position=&{gps_position}department_type={chosen_type}'.format(gps_position=1, chosen_type=2)
    PARAMS = {'firstName':first_name, 'lastName' :last_name}
    start = time.time()
    response = requests.get(url = URL, params = PARAMS)
    end = time.time()
    request_duration = end - start
    duration += request_duration
    report += '{text} with a duration of {request_duration} \n'.format(text=response.text, request_duration=request_duration)

  avg_duration = duration / nb_of_requests
  report += 'Average duration of {avg_duration}s'.format(avg_duration=avg_duration)

  with open('response_time.txt', 'w') as f:
    f.write(report)

avg_response_time(10)
