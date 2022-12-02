import numpy as np
import matplotlib.pyplot as plt
from slugify import slugify
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



rooms = ["NW", "NE", "SE", "SW"]
days = [(14, "Mon"), (15, "Tue"), (16, "Wed"), (17, "Thur"), (18, "Fri")]

# Temperature
temp_data = get_data(days, rooms, "Temperature_°C", "temp_humid")
# print(temp_data)

# Humidity
humidity_data = get_data(days, rooms, "Humidity_%", "temp_humid")
# print(humidity_data)

# Noise Level
noise_data = get_data(days, rooms, "spl_a", "awair_element")
# print(noise_data)

# Air Quality
air_data = get_data(days, rooms, "awair_score", "awair_element")
# print(air_data)

# Light Level
light_data = get_data(days, rooms, "Illumination_lx", "awair_element")
# print(light_data)


def plot_data_for_each_day(name, data,file_name,y_lim,y_label):
        barWidth = 0.20
        fig = plt.subplots(figsize =(12, 8))

        # Set position of bar on X axis
        br1 = np.arange(4)
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        br4 = [x + barWidth for x in br3]
        bar_list = [br1,br2,br3,br4]
        bar_iter = iter(bar_list)
        color_list = ["tab:blue", "tab:purple", "tab:orange", "tab:gray"]
        color_iter = iter(color_list)
        label_list = ["NW Quadrant", 'NE Quadrant','SE Quadrant','SW Quadrant']
        label_iter = iter(label_list)
        y_max = 0
        for loc, time in data.items():
                if time[0] == 'nan':
                        time = [0,0,0,0]
                for val in time:
                        if y_max < val *1.2:
                                y_max = val *1.2
                plt.bar(next(bar_iter), time, color =next(color_iter), width = barWidth,
                        edgecolor ='grey', label =next(label_iter))
        plt.xlabel('Time of the Day', fontweight ='bold', fontsize = 18)
        plt.ylabel(y_label, fontweight ='bold', fontsize = 18)
        plt.xticks([r + 1.5*barWidth for r in range(4)],
                ['8AM - 12AM', '12AM - 4PM', '4PM - 8PM', '8PM - 12PM'])
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)

        plt.ylim(0, y_max)
        plt.title("{} {} in Link Lab".format(name, file_name), fontweight ='bold', fontsize = 20)
        plt.legend()
        plt.tight_layout()

        # # Save the figures
        # save_name = "figures/"+ slugify("{} {}".format(name.lower(), file_name.lower()))
        # print(save_name)
        # plt.savefig(save_name)
        plt.show()
       

for name, data in temp_data.items():
    plot_data_for_each_day(name,data,"Temperature",30, "Temperature ℃")

# for name, data in humidity_data.items():
#     plot_data_for_each_day(name,data,"Humidity",50, "Humidity %")

# for name, data in noise_data.items():
#     plot_data_for_each_day(name,data,"Noise",80, "Noise (dB)")

# for name, data in air_data .items():
#     plot_data_for_each_day(name,data,"Air Quality",120, "Awair Score")

# for name, data in light_data.items():
#     plot_data_for_each_day(name,data,"Illumination",2000, "Illumination (lx)")