# coding: utf-8
import os, sys
# importing the requests library
import requests
import time
import random
from faker import Faker

fake = Faker()
URL = "http://68.183.17.222:8080/hospital/reserve_bed"
types = ["radiologie", "réanimation"]
duration = 0
headers = {'Content-type': 'application/json'}

def high_request_amount(nb_of_requests):
  # defining a params dict for the parameters to be sent to the API
  duration = 0
  report = ""

  for x in xrange(1,nb_of_requests):
    gps_position = "-122.426904,37.759617"
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = full_name[1]
    chosen_type = random.choice(types)
    url = URL + '?gps_position={gps_position}&department_type={chosen_type}'.format(gps_position=gps_position, chosen_type=chosen_type)
    start = time.time()
    response = requests.get(url = url, headers = headers,data = "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}")
    end = time.time()
    request_duration = end - start
    duration += request_duration
    report += '{text} with a duration of {request_duration}s \n'.format(text=response.text, request_duration=request_duration)
  report += '{nb_of_requests} requests. Total duration of {total_duration}s'.format(nb_of_requests=nb_of_requests, total_duration=duration)
  with open('numerous_requests.txt', 'w') as f:
    f.write(report)

def avg_response_time(nb_of_requests):
  # defining a params dict for the parameters to be sent to the API
  duration = 0
  report = ""


  for x in xrange(1,nb_of_requests):
    gps_position = "-122.426904,37.759617"
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = full_name[1]
    chosen_type = random.choice(types)
    url = URL + '?gps_position={gps_position}&department_type={chosen_type}'.format(gps_position=gps_position, chosen_type=chosen_type)
    start = time.time()
    response = requests.get(url = url, headers = headers,data = "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}")
    print url
    print headers
    print response.text
    end = time.time()
    request_duration = end - start
    duration += request_duration
    report += '{text} with a duration of {request_duration} \n'.format(text=response.text, request_duration=request_duration)

  avg_duration = duration / nb_of_requests
  report += 'Average duration of {avg_duration}s'.format(avg_duration=avg_duration)

  with open('response_time.txt', 'w') as f:
    f.write(report)

def high_disponibility_test():
  # defining a params dict for the parameters to be sent to the API
  report = ""

  for x in xrange(1,20):
    gps_position = "-122.426904,37.759617"
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = full_name[1]
    chosen_type = random.choice(types)
    url = URL + '?gps_position={gps_position}&department_type={chosen_type}'.format(gps_position=gps_position, chosen_type=chosen_type)
    start = time.time()
    response = requests.get(url = url, headers = headers,data = "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}")
    print url
    print headers
    print response.text
    end = time.time()
    request_duration = end - start
    report += '{text} with a duration of {request_duration} \n'.format(text=response.text, request_duration=request_duration)
  print 'Serveur n°1 is down ?'
  stoped = input()
  while stoped != "Y":
    print 'Serveur n°1 is down ?'
    stoped = input()
  report += '\nServeur n°1 is down\n\n'
  for x in xrange(1,20):
    gps_position = "-122.426904,37.759617"
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = full_name[1]
    chosen_type = random.choice(types)
    url = URL + '?gps_position={gps_position}&department_type={chosen_type}'.format(gps_position=gps_position, chosen_type=chosen_type)
    start = time.time()
    response = requests.get(url = url, headers = headers,data = "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}")
    print url
    print headers
    print response.text
    end = time.time()
    request_duration = end - start
    report += '{text} with a duration of {request_duration} \n'.format(text=response.text, request_duration=request_duration)

  report += 'Server n°2 working alone'
# avg_response_time(20)
# high_request_amount(100)
avg_response_time(20)
# avg_response_time(10)

# high_request_amount(100)

