import json
import requests
from datetime import datetime
import utils

def planes():
    # user configurable settings
    all = True
    test = True
    save_to_file = False
    airline_code = "CPA"
    airport = "KLAX"
    start = "2023-09-12T18:00:00Z"
    end = "2023-09-12T20:00:00Z"
    good_planes = ["A388 ", "A35K ", "A359 ", "B78X ", "B789 ", "B788 ", "B748 "]

    # api parameters configuration
    auth_header = {'x-apikey':'FYYrizQ1KmzeYWas7Iso1KMlNwziu7Gi'}
    if all:
        params = {"type":"Airline", "max_pages":10, "start":start, "end":end}
        airline_code = "ALL"
    else:
        params = {"airline":airline_code, "max_pages":10, "start":start, "end":end}

    # api data pull, load into dictionary
    #___________________________________________________________#
    #___________________________________________________________#
    #___________________________________________________________#
    #___________________________________________________________#
    if not test:
        response = requests.get('https://aeroapi.flightaware.com/aeroapi/airports/' + airport + "/flights/scheduled_arrivals", params=params, headers=auth_header)
        responseText = response.text
        result = json.loads(responseText)
    else:
        testFile = open('output/' + 'testInfo.txt', 'r')
        responseText = testFile.read()
        result = json.loads(responseText)
    #___________________________________________________________#
    #___________________________________________________________#
    #___________________________________________________________#
    #___________________________________________________________#

    # log raw data into log.txt
    log = open('output/' + 'log.txt', "w")
    log.write(responseText)

    # output dictionary handling
    arrivals = result["scheduled_arrivals"]

    # every flight is a dictionary
    first_flight = arrivals[0]

    # set up special arrays for additional data display
    interesting_info = [("Aircraft", "Registration", "Landing Time")]
    aircraft_count = {}
    cool = []
    special = []
    for flight in arrivals:
        type = flight["aircraft_type"]
        reg = flight["registration"]
        all_info = (type, reg, flight["scheduled_on"])
        interesting_info.append(all_info)
        if type in good_planes:
            cool.append(all_info)
        if type in aircraft_count:
            aircraft_count[type] += 1
        else:
            aircraft_count[type] = 1

    if save_to_file:
        utils.save(airline_code, result, airport, end, special, cool, interesting_info, aircraft_count)
    
    else:
        output_string = ""
        output_string += "Showing next " + str(len(result["scheduled_arrivals"])) + " arrivals into " + str(airport) + "\n"
        output_string += "Scanning from now to " + end + "\n\n"

         # writes special liveries
        if special:
            output_string += "SPECIAL LIVERIES -------------------------------\n"
            for info in special:
                output_string += str(info)
                output_string += "\n"
        else:
            output_string += "THERE ARE NO AIRPLANES OF INTEREST -------------\n"

        # writes cool planes
        if cool:
            output_string += "\nCOOL PLANES ------------------------------------\n"
            for info in cool:
                output_string += str(info)
                output_string += "\n"
        else:
            output_string += "\nTHERE ARE NO AIRPLANES OF INTEREST -------------\n"

        # writes number of every aircraft
        output_string += "\nAIRCRAFT COUNT ---------------------------------\n"
        for pair in aircraft_count.items():
            output_string += str(pair[0]) + " count: " + str(pair[1])
            output_string += "\n"

        # writes all information for each flight
        output_string += "\nALL INFO ---------------------------------------\n"
        for flight in interesting_info:
            output_string += str(flight)
            output_string += "\n"

        output_string = output_string.replace('\n', '<br>')
        return output_string