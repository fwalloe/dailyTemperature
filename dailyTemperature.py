#!/bin/python

##
#
# dailyTemperature, by Fredrik Walløe (heavily inspired by example code on met.no)
# Uses statistics from met.no to display the temperature. Can be integrated in Polybar
# TODO: change color of temperature in polybar if today's temperature is coldest/warmest in the specified range, currenly one year
#
##

import sys
import requests # See http://docs.python-requests.org/
import time

# finds the smallest or highest temperature in the temperature range
def getMinMax(today, temperatures):
    if today < 0: 
        low = min([n for n in temperatures if n<0])
        return low
    else:
        high = max([n for n in temperatures if n>0])
        return high

if __name__ == "__main__":

    today = time.strftime("%Y-%m-%d")
    # get data from n years back
    fromYear= time.strftime("2017-%m-%d") # hardcoded value as this is meant to be integrated with polybar, which doesn't like arguments
    element = 'air_temperature'
    source = 'SN18700' # weather station at Oslo Blindern
    # request your key here: https://data.met.no/auth/requestCredentials.html
    APIkey = 
    
    # used to determine whether today was the coldest in the supplied range
    temperatureList = []

    ##
    # issue an HTTP GET request
    # get infomation about available elements here: https://frost.met.no/elementtable
    ## 
    r = requests.get(
        'https://frost.met.no/observations/v0.jsonld',
        {'sources': source , 'elements': element, 'referencetime': fromYear+'/'+today },
        auth=(APIkey, '')
    )

    # extract the time series from the response
    if r.status_code == 200:
        
        for item in r.json()['data']:
            temperature = item['observations'][0]['value']
            temperatureList.append(temperature)

# if the temperature is less than 0 degrees celcius
if temperature < 0:
    # and today's temperature is the lowest recorded temperature in this period
    if temperature < (getMinMax(temperature, temperatureList[:-1])):
        print (str(temperature)+'\nC')  
    else: # today's temperature is negative, but not the lowest recorded
        print (str(temperature))  
else: # today's temperature is above 0 and is the highest temperature in this period
    if temperature > (getMinMax(temperature, temperatureList[:-1])):
        print (str(temperature)+'\nH')
    else: # today's temperature is above 0, but not the highest recorded
        print (str(temperature))

###
# Uncomment for error handling 
###
"""
    else:
        sys.stdout.write('error:\n')
        sys.stdout.write('\tstatus code: {}\n'.format(r.status_code))
        if 'error' in r.json():
            assert(r.json()['error']['code'] == r.status_code)
            sys.stdout.write('\tmessage: {}\n'.format(r.json()['error']['message']))
            sys.stdout.write('\treason: {}\n'.format(r.json()['error']['reason']))
        else:
            sys.stdout.write('\tother error\n')
"""
