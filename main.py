import utility as util
from time import time
from datetime import datetime, timedelta, time
import pandas as pd

NW_ROOMS = ["203 Olsson Arena", "201 Olsson", "208 Olsson"]
NE_ROOMS = ["211 Olsson", "217 Olsson", "219 Olsson", "225 Olsson", "227 Olsson"]
SE_ROOMS = ["241 Olsson", "243 Olsson", "245 Olsson", "247 Olsson", "249 Olsson", "251 Olsson", "253 Olsson", "255 Olsson", "257 Olsson", "260 Olsson"]
SW_ROOMS = ["269 Olsson", "271 Olsson", "273 Olsson", "275 Olsson", "277 Olsson", "279 Olsson", "281 Olsson", "283 Olsson", "285 Olsson", "Back wall of 286 Olsson", "274 Olsson", "Back wall of kitchen area Olsson"]

map = {"NW": NW_ROOMS,
        "NE": NE_ROOMS,
        "SE": SE_ROOMS,
        "SW": SW_ROOMS}

def get_data(days, rooms, category, sensor):
    df = pd.read_csv("book_with_grids.csv", encoding='unicode_escape')
    devices = list(df[df['type'] == sensor]['device_id'])
    devices.sort()

    res = {}

    for day, d in days:
        key = "11-%s %s"%(day, d)
        res[key] = {}
        hr = 8
        # room_hours = {}
        while hr < 21:
            start = datetime(2022, 11, day, hr, 0, 0)
            if hr == 20:
                end = datetime(2022, 11, day, 23, 59, 59)
            else:
                end = datetime(2022, 11, day, hr + 4, 0, 0)
            hr += 4
            rs = (util.get_cache_rs(category, start, end, devices))
            for room in rooms:
                hourly_avg = find_avg(find_value(room, rs))
                if room not in res[key]:
                    res[key][room] = []
                res[key][room].append(hourly_avg)
    print("*** %s ***"%(category))
    for date in res:
        print("--[%s]--"%(date))
        for location in res[date]:
            print("[%s]: "%(location), res[date][location])
    return res
                

def find_avg(array):
    if len(array) == 0:
        return "nan"
    res = 0
    for val in array:
        res += val
    res /= len(array)
    return round(res, 2)

def find_value(room, rs):
    res = []
    all_rooms = map[room]
    for r in rs:
        for entry in r:
            if entry['value'] is None:
                continue
            if entry['location_specific'] in all_rooms:
                res.append(entry['value'])
    return res


if __name__ == '__main__':
    rooms = ["NW", "NE", "SE", "SW"]
    days = [(14, "Mon"), (15, "Tue"), (16, "Wed"), (17, "Thur"), (18, "Fri")]
    # days = [(7, "Mon"), (8, "Tue"), (9, "Wed"), (10, "Thur"), (11, "Fri")]
    
    # Temperature
    temp_data = get_data(days, rooms, "Temperature_°C", "temp_humid")

    # Humidity
    humidity_data = get_data(days, rooms, "Humidity_%", "temp_humid")

    # Noise Level
    noise_data = get_data(days, rooms, "spl_a", "awair_element")

    # Air Quality
    air_data = get_data(days, rooms, "awair_score", "awair_element")

    # Light Level
    light_data = get_data(days, rooms, "Illumination_lx", "awair_element")
