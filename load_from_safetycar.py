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
            return True
    # exist = "1" in race.sc
    return False

def excel_unboxer(file_location):
    # print out which document is being read
    print(file_location)

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

    # Combine all factors
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
    combined_table = combined_table[["initial_pos", "sc_lap", "sc_decision", "sc_laps_travelled", "sc_laps_remaining", "sc_tyre_compound", "before_pit_pos", "Temperature", "Humidity", "Altitude", "Turns", "RaceDistance", "TrackLength", "TeamAbility", "DriverAbility", "final_pos_gained"]]

    combined_table = combined_table.astype(float)
    return combined_table

# -----------------------------------------------------------------------------------------------------------------



# apply tensorflow logics
import tensorflow as tf
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# split the dataset into train data and test data
from sklearn.model_selection import train_test_split

target_testing_race = "tuscan2020"

test_dataset = excel_unboxer("./data2020/" + target_testing_race + ".xlsx")

test_features = test_dataset.copy()

test_labels = test_features.pop("final_pos_gained")

def soft_accuracy(y_true, y_pred):
    return keras.backend.mean(keras.backend.equal(keras.backend.round(y_true), keras.backend.round(y_pred)))

# load the model, no need to train a model again
model = keras.models.load_model('safetycar/saved_model', compile=False, custom_objects={'soft_accuracy': soft_accuracy})

result_list = []
ct = 0
for i in test_features.values.tolist():
    prediction = model.predict(([i]))[0][0]
    answer = int(test_labels.values.tolist()[ct])
    result_list.append([i[1], i[2], i[3], i[4], i[5], i[6], prediction, answer, i[0], int(i[0])-prediction, int(i[0])-answer])
    ct+=1
from datetime import datetime
result_df = pd.DataFrame(result_list, columns=["sc_lap", "sc_decision", "sc_laps_travelled", "sc_laps_remaining", "sc_tyre_compound", "before_pit_pos", "prediction", "answer_final_pos_gained", "initial_position", "predicted_final_pos", "answer_final_pos"])
result_df.to_excel("./safetycar_results/new_predictions/" + target_testing_race + "_" + str(datetime.now().strftime("%Y%m%d_%H%M%S")) + "_prediction_result.xlsx", index=False)