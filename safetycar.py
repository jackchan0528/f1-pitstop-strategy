from numpy.core.fromnumeric import transpose
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import activations
import pandas as pd
import numpy as np
import sys

## Trick to run by CPU, rather than GPU ##
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
##########################################

from tensorflow.python.keras.layers.core import Dropout
pd.options.mode.chained_assignment = None  # default='warn'

def safety_car_checker(file_location):
    race = pd.read_excel(
        file_location, sheet_name="compoundchange",
        index_col = 0
    )

    # drop the unwanted rows:
    for i in race.index:
        if (
            pd.isna(race["tyre_2"][i]) 
            or pd.isna(race["final_pos_gained"][i])
            or race["tyre_grid"][i] == "W" 
            or race["tyre_grid"][i] == "I"
            or race["tyre_1"][i] == "W" 
            or race["tyre_1"][i] == "I"
            or race["tyre_2"][i] == "W" 
            or race["tyre_2"][i] == "I" 
            ):
            race = race.drop([i])

    for i in race.sc:
        if (i>0):
            print(file_location)
            return True
    return False

def excel_unboxer(file_location):
    safetycar = pd.read_excel(
        file_location, sheet_name="sc", index_col = None
    )

    # 4. Track temperature
    weather = pd.read_excel(
        file_location, sheet_name="weather",
        index_col = 0
    ).T

    temperature = weather[["Temperature"]]
    temperature["Temperature"] = temperature["Temperature"].str[:-2]
    temperature["Temperature"] = temperature["Temperature"].astype(float)
    
    humidity = weather[["Humidity"]]
    humidity["Humidity"] = humidity["Humidity"].astype(float)

    # 5. Track altitude
    altitude = pd.read_excel(
        file_location, sheet_name="altitude",
        dtype={"delta": float},
        index_col = 0
    )

    fastestlap = pd.read_excel(
        file_location, sheet_name="fastestlap",
        dtype={"No.": str, "Team": str, "Time": str},
        index_col = 0
    )

    combined_table =  safetycar[["No.", "initial_pos", "final_pos_gained", "sc_lap", "sc_decision", "sc_laps_travelled", "sc_laps_remaining", "sc_tyre_compound", "before_pit_pos"]]

    for i in combined_table.index:
        if (pd.isna(combined_table["final_pos_gained"][i])):
            print("error at: ", file_location)

    combined_table["Temperature"] = ""
    combined_table["Humidity"] = ""
    combined_table["Altitude"] = ""
    combined_table["Turns"] = ""
    combined_table["RaceDistance"] = ""
    combined_table["TrackLength"] = ""
    combined_table["TeamAbility"] = ""
    combined_table["DriverAbility"] = ""
    for i in combined_table.index:
        combined_table["Temperature"][i] = float(temperature.values)
        combined_table["Humidity"][i] = float(humidity.values)
        combined_table["Altitude"][i] = float(altitude.columns.values[0])
        
        if ("australian" in file_location):
            combined_table["Turns"][i] = 16
            combined_table["RaceDistance"][i] = 58
            combined_table["TrackLength"][i] = 5.303
        elif ("bahrain" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 57
            combined_table["TrackLength"][i] = 5.412
        elif ("chinese" in file_location):
            combined_table["Turns"][i] = 16
            combined_table["RaceDistance"][i] = 56
            combined_table["TrackLength"][i] = 5.451
        elif ("azerbaijan" in file_location or "european2016" in file_location):
            combined_table["Turns"][i] = 20
            combined_table["RaceDistance"][i] = 51
            combined_table["TrackLength"][i] = 6.003
        elif ("spanish" in file_location):
            combined_table["Turns"][i] = 16
            combined_table["RaceDistance"][i] = 66
            combined_table["TrackLength"][i] = 4.655
        elif ("monaco" in file_location):
            combined_table["Turns"][i] = 19
            combined_table["RaceDistance"][i] = 78
            combined_table["TrackLength"][i] = 3.337
        elif ("canada" in file_location):
            combined_table["Turns"][i] = 17
            combined_table["RaceDistance"][i] = 70
            combined_table["TrackLength"][i] = 4.430
        elif ("french" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 53
            combined_table["TrackLength"][i] = 5.842
        elif ("austrian" in file_location or "styrian2020" in file_location):
            combined_table["Turns"][i] = 8
            combined_table["RaceDistance"][i] = 71
            combined_table["TrackLength"][i] = 4.318
        elif ("british" in file_location or "70thanniversary2020" in file_location):
            combined_table["Turns"][i] = 18
            combined_table["RaceDistance"][i] = 52
            combined_table["TrackLength"][i] = 5.891
        elif ("german" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 64
            combined_table["TrackLength"][i] = 5.148
        elif ("hungarian" in file_location):
            combined_table["Turns"][i] = 13
            combined_table["RaceDistance"][i] = 70
            combined_table["TrackLength"][i] = 3.975
        elif ("belgian" in file_location):
            combined_table["Turns"][i] = 19
            combined_table["RaceDistance"][i] = 44
            combined_table["TrackLength"][i] = 7.004
        elif ("italian" in file_location):
            combined_table["Turns"][i] = 11
            combined_table["RaceDistance"][i] = 59
            combined_table["TrackLength"][i] = 5.793
        elif ("singapore" in file_location):
            combined_table["Turns"][i] = 23
            combined_table["RaceDistance"][i] = 61
            combined_table["TrackLength"][i] = 5.065
        elif ("russian" in file_location):
            combined_table["Turns"][i] = 18
            combined_table["RaceDistance"][i] = 53
            combined_table["TrackLength"][i] = 5.848
        elif ("japanese" in file_location):
            combined_table["Turns"][i] = 18
            combined_table["RaceDistance"][i] = 53
            combined_table["TrackLength"][i] = 5.807
        elif ("mexican" in file_location):
            combined_table["Turns"][i] = 17
            combined_table["RaceDistance"][i] = 71
            combined_table["TrackLength"][i] = 4.304
        elif ("unitedstates" in file_location):
            combined_table["Turns"][i] = 20
            combined_table["RaceDistance"][i] = 56
            combined_table["TrackLength"][i] = 5.513
        elif ("brazilian" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 71
            combined_table["TrackLength"][i] = 4.309
        elif ("abudhabi" in file_location):
            combined_table["Turns"][i] = 21
            combined_table["RaceDistance"][i] = 55
            combined_table["TrackLength"][i] = 5.554
        elif ("eifel2020" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 60
            combined_table["TrackLength"][i] = 5.148
        elif ("imola2020" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 63
            combined_table["TrackLength"][i] = 4.909
        elif ("portuguese2020" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 66
            combined_table["TrackLength"][i] = 4.653
        elif ("sakhir2020" in file_location):
            combined_table["Turns"][i] = 11
            combined_table["RaceDistance"][i] = 87
            combined_table["TrackLength"][i] = 3.543
        elif ("turkish2020" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 59
            combined_table["TrackLength"][i] = 5.245
        elif ("tuscan2020" in file_location):
            combined_table["Turns"][i] = 14
            combined_table["RaceDistance"][i] = 58
            combined_table["TrackLength"][i] = 5.338
        elif ("malaysian2017" in file_location):
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 56
            combined_table["TrackLength"][i] = 5.543
        else:
            combined_table["Turns"][i] = 15
            combined_table["RaceDistance"][i] = 50
            combined_table["TrackLength"][i] = 5
            print("Can't find the corresponding track...")
            
        for n in fastestlap.index:

            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2020" in file_location):
                if (str(fastestlap["Team"][n]).startswith("Mercedes-AMG Petronas Formula One Team")):
                    combined_table["TeamAbility"][i] = 573
                elif (str(fastestlap["Team"][n]).startswith("Scuderia Ferrari")):
                    combined_table["TeamAbility"][i] = 131
                elif (str(fastestlap["Team"][n]).startswith("Aston Martin Red Bull Racing")):
                    combined_table["TeamAbility"][i] = 319
                elif (str(fastestlap["Team"][n]).startswith("McLaren F1 Team")):
                    combined_table["TeamAbility"][i] = 202
                elif (str(fastestlap["Team"][n]).startswith("Renault DP World F1 Team")):
                    combined_table["TeamAbility"][i] = 181
                elif (str(fastestlap["Team"][n]).startswith("Scuderia AlphaTauri Honda")):
                    combined_table["TeamAbility"][i] = 107
                elif (str(fastestlap["Team"][n]).startswith("BWT Racing Point F1 Team")):
                    combined_table["TeamAbility"][i] = 195
                elif (str(fastestlap["Team"][n]).startswith("Alfa Romeo Racing ORLEN")):
                    combined_table["TeamAbility"][i] = 8
                elif (str(fastestlap["Team"][n]).startswith("Haas F1 Team")):
                    combined_table["TeamAbility"][i] = 3
                elif (str(fastestlap["Team"][n]).startswith("Williams Racing")):
                    combined_table["TeamAbility"][i] = 0
                else:
                    combined_table["TeamAbility"][i] = 0

            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2020" in file_location):
                if (str(fastestlap["Driver"][n]) == "Lewis Hamilton"):
                    combined_table["DriverAbility"][i] = 347
                elif (str(fastestlap["Driver"][n]) == "Valtteri Bottas"):
                    combined_table["DriverAbility"][i] = 223
                elif (str(fastestlap["Driver"][n]) == "Max Verstappen"):
                    combined_table["DriverAbility"][i] = 214
                elif (str(fastestlap["Driver"][n]) == "Charles Leclerc"):
                    combined_table["DriverAbility"][i] = 98
                elif (str(fastestlap["Driver"][n]) == "Sebastian Vettel"):
                    combined_table["DriverAbility"][i] = 33
                elif (str(fastestlap["Driver"][n]) == "Carlos Sainz"):
                    combined_table["DriverAbility"][i] = 105
                elif (str(fastestlap["Driver"][n]) == "Pierre Gasly"):
                    combined_table["DriverAbility"][i] = 75
                elif (str(fastestlap["Driver"][n]) == "Alexander Albon"):
                    combined_table["DriverAbility"][i] = 105
                elif (str(fastestlap["Driver"][n]) == "Daniel Ricciardo"):
                    combined_table["DriverAbility"][i] = 119
                elif (str(fastestlap["Driver"][n]) == "Sergio Pérez"):
                    combined_table["DriverAbility"][i] = 125
                elif (str(fastestlap["Driver"][n]) == "Lando Norris"):
                    combined_table["DriverAbility"][i] = 97
                elif (str(fastestlap["Driver"][n]) == "Kimi Räikkönen"):
                    combined_table["DriverAbility"][i] = 4
                elif (str(fastestlap["Driver"][n]) == "Daniil Kvyat"):
                    combined_table["DriverAbility"][i] = 32
                elif (str(fastestlap["Driver"][n]) == "Nico Hülkenberg"):
                    combined_table["DriverAbility"][i] = 10
                elif (str(fastestlap["Driver"][n]) == "Lance Stroll"):
                    combined_table["DriverAbility"][i] = 75
                elif (str(fastestlap["Driver"][n]) == "Kevin Magnussen"):
                    combined_table["DriverAbility"][i] = 1
                elif (str(fastestlap["Driver"][n]) == "Antonio Giovinazzi"):
                    combined_table["DriverAbility"][i] = 4
                elif (str(fastestlap["Driver"][n]) == "Romain Grosjean"):
                    combined_table["DriverAbility"][i] = 2
                elif (str(fastestlap["Driver"][n]) == "Nicholas Latifi"):
                    combined_table["DriverAbility"][i] = 0
                elif (str(fastestlap["Driver"][n]) == "George Russell"):
                    combined_table["DriverAbility"][i] = 3
                else:
                    combined_table["DriverAbility"][i] = 0
            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2019" in file_location):
                if (str(fastestlap["Team"][n]).startswith("Mercedes-AMG Petronas Motorsport")):
                    combined_table["TeamAbility"][i] = 739
                elif (str(fastestlap["Team"][n]).startswith("Scuderia Ferrari")):
                    combined_table["TeamAbility"][i] = 504
                elif (str(fastestlap["Team"][n]).startswith("Aston Martin Red Bull Racing")):
                    combined_table["TeamAbility"][i] = 417
                elif (str(fastestlap["Team"][n]).startswith("McLaren F1 Team")):
                    combined_table["TeamAbility"][i] = 145
                elif (str(fastestlap["Team"][n]).startswith("Renault F1 Team")):
                    combined_table["TeamAbility"][i] = 91
                elif (str(fastestlap["Team"][n]).startswith("Red Bull Toro Rosso Honda")):
                    combined_table["TeamAbility"][i] = 85
                elif (str(fastestlap["Team"][n]).startswith("SportPesa Racing Point F1 Team")):
                    combined_table["TeamAbility"][i] = 73
                elif (str(fastestlap["Team"][n]).startswith("Alfa Romeo Racing")):
                    combined_table["TeamAbility"][i] = 57
                elif (str(fastestlap["Team"][n]).startswith("Haas F1 Team")):
                    combined_table["TeamAbility"][i] = 28
                elif (str(fastestlap["Team"][n]).startswith("ROKiT Williams Racing")):
                    combined_table["TeamAbility"][i] = 1
                else:
                    combined_table["TeamAbility"][i] = 0

            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2019" in file_location):
                if (str(fastestlap["Driver"][n]) == "Lewis Hamilton"):
                    combined_table["DriverAbility"][i] = 413
                elif (str(fastestlap["Driver"][n]) == "Valtteri Bottas"):
                    combined_table["DriverAbility"][i] = 326
                elif (str(fastestlap["Driver"][n]) == "Max Verstappen"):
                    combined_table["DriverAbility"][i] = 278
                elif (str(fastestlap["Driver"][n]) == "Charles Leclerc"):
                    combined_table["DriverAbility"][i] = 264
                elif (str(fastestlap["Driver"][n]) == "Sebastian Vettel"):
                    combined_table["DriverAbility"][i] = 240
                elif (str(fastestlap["Driver"][n]) == "Carlos Sainz"):
                    combined_table["DriverAbility"][i] = 96
                elif (str(fastestlap["Driver"][n]) == "Pierre Gasly"):
                    combined_table["DriverAbility"][i] = 95
                elif (str(fastestlap["Driver"][n]) == "Alexander Albon"):
                    combined_table["DriverAbility"][i] = 92
                elif (str(fastestlap["Driver"][n]) == "Daniel Ricciardo"):
                    combined_table["DriverAbility"][i] = 54
                elif (str(fastestlap["Driver"][n]) == "Sergio Pérez"):
                    combined_table["DriverAbility"][i] = 52
                elif (str(fastestlap["Driver"][n]) == "Lando Norris"):
                    combined_table["DriverAbility"][i] = 49
                elif (str(fastestlap["Driver"][n]) == "Kimi Räikkönen"):
                    combined_table["DriverAbility"][i] = 43
                elif (str(fastestlap["Driver"][n]) == "Daniil Kvyat"):
                    combined_table["DriverAbility"][i] = 37
                elif (str(fastestlap["Driver"][n]) == "Nico Hülkenberg"):
                    combined_table["DriverAbility"][i] = 37
                elif (str(fastestlap["Driver"][n]) == "Lance Stroll"):
                    combined_table["DriverAbility"][i] = 21
                elif (str(fastestlap["Driver"][n]) == "Kevin Magnussen"):
                    combined_table["DriverAbility"][i] = 20
                elif (str(fastestlap["Driver"][n]) == "Antonio Giovinazzi"):
                    combined_table["DriverAbility"][i] = 14
                elif (str(fastestlap["Driver"][n]) == "Romain Grosjean"):
                    combined_table["DriverAbility"][i] = 8
                elif (str(fastestlap["Driver"][n]) == "Robert Kubica"):
                    combined_table["DriverAbility"][i] = 1
                elif (str(fastestlap["Driver"][n]) == "George Russell"):
                    combined_table["DriverAbility"][i] = 0
                else:
                    combined_table["DriverAbility"][i] = 0

            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2018" in file_location):
                if (str(fastestlap["Team"][n]).startswith("Mercedes AMG Petronas Motorsport")):
                    combined_table["TeamAbility"][i] = 655
                elif (str(fastestlap["Team"][n]).startswith("Scuderia Ferrari")):
                    combined_table["TeamAbility"][i] = 571
                elif (str(fastestlap["Team"][n]).startswith("Aston Martin Red Bull Racing")):
                    combined_table["TeamAbility"][i] = 419
                elif (str(fastestlap["Team"][n]).startswith("Renault Sport Formula One Team")):
                    combined_table["TeamAbility"][i] = 122
                elif (str(fastestlap["Team"][n]).startswith("Haas F1 Team")):
                    combined_table["TeamAbility"][i] = 93
                elif (str(fastestlap["Team"][n]).startswith("McLaren F1 Team")):
                    combined_table["TeamAbility"][i] = 62
                elif (str(fastestlap["Team"][n]).startswith("Sahara Force India F1 Team")):
                    combined_table["TeamAbility"][i] = 52
                elif (str(fastestlap["Team"][n]).startswith("Alfa Romeo Sauber F1 Team")):
                    combined_table["TeamAbility"][i] = 48
                elif (str(fastestlap["Team"][n]).startswith("Red Bull Toro Rosso Honda")):
                    combined_table["TeamAbility"][i] = 33
                elif (str(fastestlap["Team"][n]).startswith("Williams Martini Racing")):
                    combined_table["TeamAbility"][i] = 7
                else:
                    combined_table["TeamAbility"][i] = 0

            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2018" in file_location):
                # print(combined_table["No."][i], fastestlap["No."][n])
                # print(str(fastestlap["Driver"][n]))
                if (str(fastestlap["Driver"][n]) == "Lewis Hamilton"):
                    combined_table["DriverAbility"][i] = 408
                elif (str(fastestlap["Driver"][n]) == "Sebastian Vettel"):
                    combined_table["DriverAbility"][i] = 320
                elif (str(fastestlap["Driver"][n]) == "Kimi Räikkönen"):
                    combined_table["DriverAbility"][i] = 251
                elif (str(fastestlap["Driver"][n]) == "Max Verstappen"):
                    combined_table["DriverAbility"][i] = 249
                elif (str(fastestlap["Driver"][n]) == "Valtteri Bottas"):
                    combined_table["DriverAbility"][i] = 247
                elif (str(fastestlap["Driver"][n]) == "Daniel Ricciardo"):
                    combined_table["DriverAbility"][i] = 170
                elif (str(fastestlap["Driver"][n]) == "Nico Hülkenberg"):
                    combined_table["DriverAbility"][i] = 69
                elif (str(fastestlap["Driver"][n]) == "Sergio Pérez"):
                    combined_table["DriverAbility"][i] = 62
                elif (str(fastestlap["Driver"][n]) == "Kevin Magnussen"):
                    combined_table["DriverAbility"][i] = 56
                elif (str(fastestlap["Driver"][n]) == "Carlos Sainz"):
                    combined_table["DriverAbility"][i] = 53
                elif (str(fastestlap["Driver"][n]) == "Fernando Alonso"):
                    combined_table["DriverAbility"][i] = 50
                elif (str(fastestlap["Driver"][n]) == "Esteban Ocon"):
                    combined_table["DriverAbility"][i] = 49
                elif (str(fastestlap["Driver"][n]) == "Charles Leclerc"):
                    combined_table["DriverAbility"][i] = 39
                elif (str(fastestlap["Driver"][n]) == "Romain Grosjean"):
                    combined_table["DriverAbility"][i] = 37
                elif (str(fastestlap["Driver"][n]) == "Pierre Gasly"):
                    combined_table["DriverAbility"][i] = 29
                elif (str(fastestlap["Driver"][n]) == "Stoffel Vandoorne"):
                    combined_table["DriverAbility"][i] = 12
                elif (str(fastestlap["Driver"][n]) == "Marcus Ericsson"):
                    combined_table["DriverAbility"][i] = 9
                elif (str(fastestlap["Driver"][n]) == "Lance Stroll"):
                    combined_table["DriverAbility"][i] = 6
                elif (str(fastestlap["Driver"][n]) == "Brendon Hartley"):
                    combined_table["DriverAbility"][i] = 4               
                elif (str(fastestlap["Driver"][n]) == "Sergey Sirotkin"):
                    combined_table["DriverAbility"][i] = 1
                else:
                    combined_table["DriverAbility"][i] = 0


            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2017" in file_location):
                if (str(fastestlap["Team"][n]).startswith("Mercedes AMG Petronas F1 Team")):
                    combined_table["TeamAbility"][i] = 668
                elif (str(fastestlap["Team"][n]).startswith("Scuderia Ferrari")):
                    combined_table["TeamAbility"][i] = 522
                elif (str(fastestlap["Team"][n]).startswith("Red Bull Racing")):
                    combined_table["TeamAbility"][i] = 368
                elif (str(fastestlap["Team"][n]).startswith("Sahara Force India F1 Team")):
                    combined_table["TeamAbility"][i] = 187
                elif (str(fastestlap["Team"][n]).startswith("Williams Martini Racing")):
                    combined_table["TeamAbility"][i] = 83
                elif (str(fastestlap["Team"][n]).startswith("Renault Sport Formula One Team")):
                    combined_table["TeamAbility"][i] = 57
                elif (str(fastestlap["Team"][n]).startswith("Scuderia Toro Rosso")):
                    combined_table["TeamAbility"][i] = 53
                elif (str(fastestlap["Team"][n]).startswith("Haas F1 Team")):
                    combined_table["TeamAbility"][i] = 47
                elif (str(fastestlap["Team"][n]).startswith("McLaren Honda Formula 1 Team")):
                    combined_table["TeamAbility"][i] = 30
                elif (str(fastestlap["Team"][n]).startswith("Sauber F1 Team")):
                    combined_table["TeamAbility"][i] = 5
                else:
                    combined_table["TeamAbility"][i] = 0

            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2017" in file_location):
                if (str(fastestlap["Driver"][n]) == "Lewis Hamilton"):
                    combined_table["DriverAbility"][i] = 363
                elif (str(fastestlap["Driver"][n]) == "Sebastian Vettel"):
                    combined_table["DriverAbility"][i] = 317
                elif (str(fastestlap["Driver"][n]) == "Valtteri Bottas"):
                    combined_table["DriverAbility"][i] = 305
                elif (str(fastestlap["Driver"][n]) == "Kimi Räikkönen"):
                    combined_table["DriverAbility"][i] = 205
                elif (str(fastestlap["Driver"][n]) == "Daniel Ricciardo"):
                    combined_table["DriverAbility"][i] = 200
                elif (str(fastestlap["Driver"][n]) == "Max Verstappen"):
                    combined_table["DriverAbility"][i] = 168
                elif (str(fastestlap["Driver"][n]) == "Sergio Pérez"):
                    combined_table["DriverAbility"][i] = 100
                elif (str(fastestlap["Driver"][n]) == "Esteban Ocon"):
                    combined_table["DriverAbility"][i] = 87
                elif (str(fastestlap["Driver"][n]) == "Carlos Sainz"):
                    combined_table["DriverAbility"][i] = 54              
                elif (str(fastestlap["Driver"][n]) == "Nico Hülkenberg"):
                    combined_table["DriverAbility"][i] = 43
                elif (str(fastestlap["Driver"][n]) == "Felipe Massa"):
                    combined_table["DriverAbility"][i] = 43
                elif (str(fastestlap["Driver"][n]) == "Lance Stroll"):
                    combined_table["DriverAbility"][i] = 40
                elif (str(fastestlap["Driver"][n]) == "Romain Grosjean"):
                    combined_table["DriverAbility"][i] = 28
                elif (str(fastestlap["Driver"][n]) == "Kevin Magnussen"):
                    combined_table["DriverAbility"][i] = 19
                elif (str(fastestlap["Driver"][n]) == "Fernando Alonso"):
                    combined_table["DriverAbility"][i] = 17
                elif (str(fastestlap["Driver"][n]) == "Stoffel Vandoorne"):
                    combined_table["DriverAbility"][i] = 13
                elif (str(fastestlap["Driver"][n]) == "Jolyon Palmer"):
                    combined_table["DriverAbility"][i] = 8                
                elif (str(fastestlap["Driver"][n]) == "Pascal Wehrlein"):
                    combined_table["DriverAbility"][i] = 5                
                elif (str(fastestlap["Driver"][n]) == "Daniil Kvyat"):
                    combined_table["DriverAbility"][i] = 5
                else:
                    combined_table["DriverAbility"][i] = 0
                
            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2016" in file_location):
                if (str(fastestlap["Team"][n]).startswith("Mercedes AMG Petronas F1 Team")):
                    combined_table["TeamAbility"][i] = 765
                elif (str(fastestlap["Team"][n]).startswith("Red Bull Racing")):
                    combined_table["TeamAbility"][i] = 468
                elif (str(fastestlap["Team"][n]).startswith("Scuderia Ferrari")):
                    combined_table["TeamAbility"][i] = 398
                elif (str(fastestlap["Team"][n]).startswith("Sahara Force India F1 Team")):
                    combined_table["TeamAbility"][i] = 173
                elif (str(fastestlap["Team"][n]).startswith("Williams Martini Racing")):
                    combined_table["TeamAbility"][i] = 138
                elif (str(fastestlap["Team"][n]).startswith("McLaren Honda")):
                    combined_table["TeamAbility"][i] = 76
                elif (str(fastestlap["Team"][n]).startswith("Scuderia Toro Rosso")):
                    combined_table["TeamAbility"][i] = 63
                elif (str(fastestlap["Team"][n]).startswith("Haas F1 Team")):
                    combined_table["TeamAbility"][i] = 29
                elif (str(fastestlap["Team"][n]).startswith("Renault Sport F1 Team")):
                    combined_table["TeamAbility"][i] = 8
                elif (str(fastestlap["Team"][n]).startswith("Sauber F1 Team")):
                    combined_table["TeamAbility"][i] = 2
                elif (str(fastestlap["Team"][n]).startswith("Manor Racing MRT")):
                    combined_table["TeamAbility"][i] = 1
                else:
                    combined_table["TeamAbility"][i] = 0

            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2016" in file_location):
                if (str(fastestlap["Driver"][n]) == "Nico Rosberg"):
                    combined_table["DriverAbility"][i] = 385
                elif (str(fastestlap["Driver"][n]) == "Lewis Hamilton"):
                    combined_table["DriverAbility"][i] = 380
                elif (str(fastestlap["Driver"][n]) == "Daniel Ricciardo"):
                    combined_table["DriverAbility"][i] = 256
                elif (str(fastestlap["Driver"][n]) == "Sebastian Vettel"):
                    combined_table["DriverAbility"][i] = 212
                elif (str(fastestlap["Driver"][n]) == "Max Verstappen"):
                    combined_table["DriverAbility"][i] = 204               
                elif (str(fastestlap["Driver"][n]) == "Kimi Räikkönen"):
                    combined_table["DriverAbility"][i] = 186            
                elif (str(fastestlap["Driver"][n]) == "Sergio Pérez"):
                    combined_table["DriverAbility"][i] = 101             
                elif (str(fastestlap["Driver"][n]) == "Valtteri Bottas"):
                    combined_table["DriverAbility"][i] = 85
                elif (str(fastestlap["Driver"][n]) == "Nico Hülkenberg"):
                    combined_table["DriverAbility"][i] = 72
                elif (str(fastestlap["Driver"][n]) == "Fernando Alonso"):
                    combined_table["DriverAbility"][i] = 54
                elif (str(fastestlap["Driver"][n]) == "Felipe Massa"):
                    combined_table["DriverAbility"][i] = 53               
                elif (str(fastestlap["Driver"][n]) == "Carlos Sainz"):
                    combined_table["DriverAbility"][i] = 46              
                elif (str(fastestlap["Driver"][n]) == "Romain Grosjean"):
                    combined_table["DriverAbility"][i] = 29
                elif (str(fastestlap["Driver"][n]) == "Daniil Kvyat"):
                    combined_table["DriverAbility"][i] = 25
                elif (str(fastestlap["Driver"][n]) == "Jenson Button"):
                    combined_table["DriverAbility"][i] = 21
                elif (str(fastestlap["Driver"][n]) == "Kevin Magnussen"):
                    combined_table["DriverAbility"][i] = 7
                elif (str(fastestlap["Driver"][n]) == "Felipe Nasr"):
                    combined_table["DriverAbility"][i] = 2
                elif (str(fastestlap["Driver"][n]) == "Stoffel Vandoorne"):
                    combined_table["DriverAbility"][i] = 1
                elif (str(fastestlap["Driver"][n]) == "Jolyon Palmer"):
                    combined_table["DriverAbility"][i] = 1                
                elif (str(fastestlap["Driver"][n]) == "Pascal Wehrlein"):
                    combined_table["DriverAbility"][i] = 1                          
                else:
                    combined_table["DriverAbility"][i] = 0

    # reorder the columns
    combined_table = combined_table[["initial_pos", "sc_lap", "sc_decision", "sc_laps_travelled", "sc_laps_remaining", "sc_tyre_compound", "before_pit_pos", 
    "Temperature", "Humidity", "Altitude", "Turns", "RaceDistance", "TrackLength", "TeamAbility", "DriverAbility", "final_pos_gained"]]

    combined_table = combined_table.astype(float)
    return combined_table

# -----------------------------------------------------------------------------------------------------------------

file_names_2020 = ["70thanniversary2020", "abudhabi2020", "austrian2020", "bahrain2020", "belgian2020", "british2020", 
"eifel2020", "hungarian2020", "imola2020", "italian2020", "portuguese2020", "russian2020",
"sakhir2020", "spanish2020", "styrian2020", "turkish2020", "tuscan2020"]
file_names_2019 = ["abudhabi2019", "australian2019", "austrian2019", "azerbaijan2019", "bahrain2019", "belgian2019", 
"brazilian2019", "british2019", "canada2019", "chinese2019", "french2019", "german2019", 
"hungarian2019", "italian2019", "japanese2019", "mexican2019", "monaco2019", "russian2019", 
"singapore2019", "spanish2019", "unitedstates2019"]
file_names_2018 = ["abudhabi2018", "australian2018", "austrian2018", "azerbaijan2018", "bahrain2018", "belgian2018", 
"brazilian2018", "british2018", "canada2018", "chinese2018", "french2018", "german2018", 
"hungarian2018", "italian2018", "japanese2018", "mexican2018", "monaco2018", "russian2018", 
"singapore2018", "spanish2018", "unitedstates2018"]
file_names_2017 = ["abudhabi2017", "australian2017", "austrian2017", "azerbaijan2017", "bahrain2017", "belgian2017", 
"brazilian2017", "british2017", "canada2017", "chinese2017", "malaysian2017",
"hungarian2017", "italian2017", "japanese2017", "mexican2017", "monaco2017", "russian2017", 
"singapore2017", "spanish2017", "unitedstates2017"]
file_names_2016 = ["abudhabi2016", "australian2016", "austrian2016", "belgian2016", 
"british2016", "canada2016", "european2016",
"hungarian2016", "italian2016", "japanese2016", "mexican2016", "monaco2016", "russian2016"]

dataset = pd.DataFrame()

for i in file_names_2020:
    if (safety_car_checker("./data2020/"+i+".xlsx")):
        temp_dataset = excel_unboxer("./data2020/"+i+".xlsx")
        dataset = pd.concat([dataset, temp_dataset], axis = 0)
for i in file_names_2019:
    if (safety_car_checker("./data2019/"+i+".xlsx")):
        temp_dataset = excel_unboxer("./data2019/"+i+".xlsx")
        dataset = pd.concat([dataset, temp_dataset], axis = 0)
for i in file_names_2018:
    if (safety_car_checker("./data2018/"+i+".xlsx")):
        temp_dataset = excel_unboxer("./data2018/"+i+".xlsx")
        dataset = pd.concat([dataset, temp_dataset], axis = 0)
for i in file_names_2017:
    if (safety_car_checker("./data2017/"+i+".xlsx")):
        temp_dataset = excel_unboxer("./data2017/"+i+".xlsx")
        dataset = pd.concat([dataset, temp_dataset], axis = 0)
for i in file_names_2016:
    if (safety_car_checker("./data2016/"+i+".xlsx")):
        temp_dataset = excel_unboxer("./data2016/"+i+".xlsx")
        dataset = pd.concat([dataset, temp_dataset], axis = 0)

dataset = dataset.reset_index(drop=True)

print(dataset.dtypes)

to_be_deleted_index_n1 = []
to_be_deleted_index_0 = []
to_be_deleted_index_1 = []
to_be_deleted_index_2 = []
to_be_deleted_index_3 = []
to_be_deleted_index_4 = []

for index, row in dataset.iterrows():
    if (row['final_pos_gained']==0):
        to_be_deleted_index_0.append(index)
    elif (row['final_pos_gained']==-1):
        to_be_deleted_index_n1.append(index)
    elif (row['final_pos_gained']==1):
        to_be_deleted_index_1.append(index)
    elif (row['final_pos_gained']==2):
        to_be_deleted_index_2.append(index)
    elif (row['final_pos_gained']==3):
        to_be_deleted_index_3.append(index)
    elif (row['final_pos_gained']==4):
        to_be_deleted_index_4.append(index)

dataset.to_csv('dataset_safetycar.csv')

# apply tensorflow logics
import tensorflow as tf
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# split the dataset into train data and test data
from sklearn.model_selection import train_test_split

dataset = dataset.reset_index(drop=True)

print(dataset)

train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop("final_pos_gained")
test_labels = test_features.pop("final_pos_gained")


from tensorflow.keras.layers.experimental import preprocessing
normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(train_features))

from tensorflow.keras import regularizers

model = keras.Sequential([normalizer,
        layers.Dense(256, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(256, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(128, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(128, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(64, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(32, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(16, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(16, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1)
        ])

def soft_accuracy(y_true, y_pred):
    return keras.backend.mean(keras.backend.equal(keras.backend.round(y_true), keras.backend.round(y_pred)))

noOfEpochs = 1000

model.compile(loss='mean_absolute_error', optimizer='rmsprop')
print(model.summary())
history = model.fit(train_features, train_labels, epochs=noOfEpochs, verbose=1, validation_split=0.2, shuffle=True)

# plot both graphs in one graph
import matplotlib.pyplot as plt
# plt.subplot(1, 2, 1)
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(range(noOfEpochs), history.history['loss'], label='loss')
plt.plot(range(noOfEpochs), history.history['val_loss'], label='val_loss')
# plt.plot(range(500), history.history['soft_accuracy'], label='accuracy')
plt.legend(['train', 'test'], loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

print("now evaluating:")
results = model.evaluate(test_features, test_labels, batch_size=128, verbose=1)
print("test loss, test acc:", results)

# save the model
model.save('safetycar/saved_model/')
print("Finished training the model")