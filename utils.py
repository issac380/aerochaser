import datetime

def save(airline_code, result, airport, end, special, cool, interesting_info, aircraft_count):
    # configure ouput file
    now = datetime.now()
    current_time = now.strftime("%d_%m_%Y %H_%M_%S")
    path_to_file = 'output/' + airline_code + " "+ current_time + '.txt'

    # saving to output file
    output = open(path_to_file, "w")

    # writes total num flights
    output.write("Showing next " + str(len(result["scheduled_arrivals"])) + " arrivals into " + str(airport) + "\n")
    output.write("Scanning from now to " + end + "\n\n")

    # writes special liveries
    if special:
        output.write("SPECIAL LIVERIES -------------------------------\n")
        for info in special:
            output.write(str(info))
            output.write("\n")
    else:
        output.write("THERE ARE NO AIRPLANES OF INTEREST -------------\n")

    # writes cool planes
    if cool:
        output.write("\nCOOL PLANES ------------------------------------\n")
        for info in cool:
            output.write(str(info))
            output.write("\n")
    else:
        output.write("\nTHERE ARE NO AIRPLANES OF INTEREST -------------\n")

    # writes number of every aircraft
    output.write("\nAIRCRAFT COUNT ---------------------------------\n")
    for pair in aircraft_count.items():
        output.write(str(pair[0]) + " count: " + str(pair[1]))
        output.write("\n")

    # writes all information for each flight
    output.write("\nALL INFO ---------------------------------------\n")
    for flight in interesting_info:
        output.write(str(flight))
        output.write("\n")
