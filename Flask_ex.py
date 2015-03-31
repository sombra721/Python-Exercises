'''
This guide will walk you through using this web application to get the weather data.

The web application uses the following APIs:
1. weathersource API : To obtain the weather history data.
2. openweathermap API : To obtain the current weather data.

Usage

Command to execute the web application:
python Flask_ex.py 8080

Once the web application is executed, we could manipulate it to receive the expected weather information.
1. GET /api/v1/location/{postal_code}/temperature-stats
Look up the current temperature for the provided postal code and return historical data for the last 5 days.
ex. If we want to view the current and history weather at San Jose, CA 95134, we could use the following address to receive the data.
http://127.0.0.1:8080/api/v1/location/95134/temperature-stats

2. GET /api/v1/temperature-stats?postal_codes={postal_codes}
This API will provide the same data as the temperature-stats API above, but for up-to 10 postal codes.
ex. If we want to view the current and history weather at San Jose, CA 95134 and San Jose CA, 95134, we could use the following address to receive the data.
http://127.0.0.1:8080/api/v1/temperature-stats/?postal_codes=95131,95134
'''

import requests
import json
import datetime
import sys
from rfc3339 import rfc3339
from flask import Flask, jsonify, request
app = Flask(__name__)

api_key = "f538ffb20e5a93bf2957"
port_num = int(sys.argv[1])
end_date = datetime.date.today() + datetime.timedelta(days=-1)
start_date = end_date + datetime.timedelta(days=-5)
days =(end_date-start_date).days

# get the weather history data using zip_code
def get_history(zip_code):
    global api_key
    global start_date
    global end_date
    get_history_link = "https://api.weathersource.com/v1/" + api_key + "/history_by_postal_code.json?period=day&postal_code_eq=" + zip_code + "&country_eq=US&timestamp_between=" + str(start_date) + "," + str(end_date) + "&fields=postal_code,country,timestamp,tempMax,tempAvg,tempMin"
    r = requests.get(get_history_link)
    json_data = json.loads(r.text)
    return json_data

# get the current weather data using zip_code    
def get_current(zip_code):
    get_current = "http://api.openweathermap.org/data/2.5/weather?q=" + zip_code
    r = requests.get(get_current)
    json_data = json.loads(r.text)
    return json_data    

# parse the multiple zip codes and store them in a list then return it, every element in the list is single zip_code
def get_postal_codes(zid_codes):
    zip_codes_list = []
    while zid_codes and len(zip_codes_list) < 10:
        if len(zid_codes) > 5:
            zip_codes_list.append(zid_codes[:zid_codes.index(",")])
            zid_codes = zid_codes[zid_codes.index(",") + 1:]
        else:
            zip_codes_list.append(zid_codes)
            zid_codes = ""
    return zip_codes_list

# extract the weather history data by each date and store the extracted data into a list then return it.
def get_history_info(json_data):
    global days
    history_list = []
    for i in range(days):
        current_dict = {}
        target_day = str(rfc3339(start_date + datetime.timedelta(days=i)))
        target = filter(lambda t: t['timestamp'] == target_day, json_data)
        current_dict["date"] = target_day
        current_dict["min"] = target[0]["tempMin"]
        current_dict["max"] = target[0]["tempMax"]
        history_list.append(current_dict)
    return history_list


@app.route('/api/v1/location/<zip_code>/temperature-stats', methods=['GET'])
def sinlge_zip_code(zip_code):    
    global start_date
    history_json_data = get_history(zip_code)
    current_json_data = get_current(zip_code)
    get_history_info(history_json_data)
    day = rfc3339(start_date)
    task = filter(lambda t: t['timestamp'] == "2015-03-15T00:00:00-07:00", history_json_data)
    if len(task) == 0:
        pass

    return jsonify({"current": current_json_data["main"]["temp"],"history": get_history_info(history_json_data)})

@app.route('/api/v1/temperature-stats/', methods=['GET'])
def multiple_zip_codes(): 
    zip_codes = request.args.get('postal_codes')
    zip_codes_list = get_postal_codes(zip_codes)
    results_list = []
    for i in zip_codes_list:
        weather_info = {}
        history_json_data = get_history(i)
        current_json_data = get_current(i)
        weather_info["postal_code"] = i
        weather_info["current"] = current_json_data["main"]["temp"]
        weather_info["history"] = get_history_info(history_json_data)
        results_list.append(weather_info)
    return jsonify({"results": results_list})
    
if __name__ == '__main__':
    global port_num
    app.run(host='127.0.0.1', port=port_num)