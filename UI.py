import os
from os import system
system('mode con: cols=200 lines=49')

print("*********************************************************")
print("**Formula One Pit Stop Strategy Decision Support System**")
print("*********************************************************")
print()
print("Team: Scuderia Ferrari F1 Team")
print("Driver 1: Charles Leclerc")
print("Driver 2: Carlos Sainz")
print()
# print("Model 1: Pit Stop Strategy")
# print("Model 2: Safety Car Scenario")
# print()
# modelNo = input("Please enter the model to be used, or press ENTER to exit the program:\nModel ")
modelNo = input("End of prediction, please enter the model to be used, or press ENTER to exit the program:\n\nModel 1: Pit Stop Strategy\nModel 2: Safety Car Scenario\n\nModel ")

# os.system('cls')
while (modelNo != ""):
    if (modelNo == "1"):
        # define the input shape, which follows ["initial_pos", "no_of_pits", 
        # "tyre_grid", "tyre_1", "tyre_2", "tyre_grid_distance", "tyre_1_distance", 
        # "tyre_2_distance", "sc", "Temperature", "Humidity", "Altitude", "Turns", 
        # "RaceDistance", "TrackLength", "TeamAbility", "DriverAbility"]]
        print()
        print("******************************")
        print("**Model 1: Pit Stop Strategy**")
        print("******************************")
        print()
        print("Please select the circuit")
        print("""
        1. Abu Dhabi: Yas Marina
        2. Australian: Albert Park
        3. Austrian: Red Bull Ring
        4. Azerbaijan: Baku
        5. Bahrain: Bahrain
        6. Bahrain: Sakhir
        7. Belgian: Spa
        8. Brazilian: São Paulo
        9. British: Silverstone
        10. Canada: Montreal
        11. Chinese: Shanghai
        12. French: Paul Ricard
        13. German: Hockenheimring
        14. German: Nürburging
        15. Hungarian: Hungaroring
        16. Italian: Monza
        17. Italian: Imola
        18. Italian: Tuscan (Mugello)
        19. Japanese: Suzuka
        20. Mexican: Mexico City
        21. Monaco: Monte Carlo
        22. Portuguese: Portimão
        23. Russian: Sochi
        24. Singapore: Marina Bay
        25. Spanish: Barcelona-Catalunya
        26. Turkish: Istanbul
        27. UnitedStates: Austin
        28. Others
        """)
        circuitNo = input("Please enter the circuit:\nCircuit ")
        if (circuitNo == "1"):
            Altitude = 10.7
            Turns = 21
            RaceDistance = 55
            TrackLength = 5.554
        elif (circuitNo == "2"):
            Altitude = 2.6
            Turns = 16
            RaceDistance = 58
            TrackLength = 5.303
        elif (circuitNo == "3"):
            Altitude = 63.5
            Turns = 8
            RaceDistance = 71
            TrackLength = 4.318
        elif (circuitNo == "4"):
            Altitude = 26.8
            Turns = 20
            RaceDistance = 51
            TrackLength = 6.003
        elif (circuitNo == "5"):
            Altitude = 16.9
            Turns = 15
            RaceDistance = 57
            TrackLength = 5.412
        elif (circuitNo == "6"):
            Altitude = 19.4
            Turns = 11
            RaceDistance = 87
            TrackLength = 3.543
        elif (circuitNo == "7"):
            Altitude = 102.2
            Turns = 19
            RaceDistance = 44
            TrackLength = 7.004
        elif (circuitNo == "8"):
            Altitude = 43
            Turns = 15
            RaceDistance = 71
            TrackLength = 4.309
        elif (circuitNo == "9"):
            Altitude = 11.3
            Turns = 18
            RaceDistance = 52
            TrackLength = 5.891
        elif (circuitNo == "10"):
            Altitude = 5.2
            Turns = 17
            RaceDistance = 70
            TrackLength = 4.430
        elif (circuitNo == "11"):
            Altitude = 7.4
            Turns = 16
            RaceDistance = 56
            TrackLength = 5.451
        elif (circuitNo == "12"):
            Altitude = 33
            Turns = 15
            RaceDistance = 53
            TrackLength = 5.842
        elif (circuitNo == "13"):
            Altitude = 4.3
            Turns = 15
            RaceDistance = 64
            TrackLength = 5.148
        elif (circuitNo == "14"):
            Altitude = 56.7
            Turns = 15
            RaceDistance = 60
            TrackLength = 5.148
        elif (circuitNo == "15"):
            Altitude = 34.6
            Turns = 13
            RaceDistance = 70
            TrackLength = 3.975
        elif (circuitNo == "16"):
            Altitude = 12.8
            Turns = 11
            RaceDistance = 59
            TrackLength = 5.793
        elif (circuitNo == "17"):
            Altitude = 32
            Turns = 15
            RaceDistance = 63
            TrackLength = 4.909
        elif (circuitNo == "18"):
            Altitude = 43.2
            Turns = 14
            RaceDistance = 58
            TrackLength = 5.338
        elif (circuitNo == "19"):
            Altitude = 40.4
            Turns = 18
            RaceDistance = 53
            TrackLength = 5.807
        elif (circuitNo == "20"):
            Altitude = 2.8
            Turns = 17
            RaceDistance = 71
            TrackLength = 4.304
        elif (circuitNo == "21"):
            Altitude = 42
            Turns = 19
            RaceDistance = 78
            TrackLength = 3.337
        elif (circuitNo == "22"):
            Altitude = 30
            Turns = 15
            RaceDistance = 66
            TrackLength = 4.653
        elif (circuitNo == "23"):
            Altitude = 1.9
            Turns = 18
            RaceDistance = 53
            TrackLength = 5.848
        elif (circuitNo == "24"):
            Altitude = 5.3
            Turns = 23
            RaceDistance = 61
            TrackLength = 5.065
        elif (circuitNo == "25"):
            Altitude = 29.6
            Turns = 16
            RaceDistance = 66
            TrackLength = 4.655
        elif (circuitNo == "26"):
            Altitude = 40.8
            Turns = 15
            RaceDistance = 59
            TrackLength = 5.245
        elif (circuitNo == "27"):
            Altitude = 30.9
            Turns = 20
            RaceDistance = 56
            TrackLength = 5.513
        else:
            # Never raced on this circuit, prompt user to input details
            print("We have never raced in this circuit yet:")
            Altitude = input("Please enter the maximum altitude change of the circuit:\nMaximum altitude change: ")
            Turns = input("Please enter the total number of turns in a lap of the circuit:\nNumber of turns: ")
            RaceDistance = input("Please enter the total number of laps of the circuit:\nNumber of laps: ")
            TrackLength = input("Please enter the length of the circuit:\nTrack Length: ")
        
        # os.system('cls')

        print()
        print("******************************")
        print("**Model 1: Pit Stop Strategy**")
        print("******************************")
        print()
        print("Which team is it?")
        print("""
        1. Scuderia Ferrari F1 Team
        2. Mercedes-AMG Petronas Formula One Team    
        3. Red Bull Racing
        4. Aston Martin Cognizant Formula One Team
        5. McLaren F1 Team
        6. Alpine F1 Team
        7. Scuderia AlphaTauri Honda
        8. Alfa Romeo Racing ORLEN
        9. Williams Racing
        10. Uralkali Haas F1 Team
        11. Others
        """)
        teamNo = input("Please enter the team:\nTeam ")
        print()
        if (teamNo == "1"):
            TeamAbility = 131
            print("Team: Scuderia Ferrari F1 Team")
            print("""
        Driver 1: Charles Leclerc
        Driver 2: Carlos Sainz
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 98
            else:
                DriverAbility = 105
        elif (teamNo == "2"):
            TeamAbility = 573
            print("Team: Mercedes-AMG Petronas Formula One Team")
            print("Driver 1: Lewis Hamilton")
            print("Driver 2: Valtteri Bottas")
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 347
            else:
                DriverAbility = 223
        elif (teamNo == "3"):
            TeamAbility = 319
            print("Team: Red Bull Racing")
            print("""
        Driver 1: Max Verstappen
        Driver 2: Sergio Pérez
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 214
            else:
                DriverAbility = 125
        elif (teamNo == "4"):
            TeamAbility = 195
            print("Team: Aston Martin Cognizant Formula One Team")
            print("""
        Driver 1: Lance Stroll
        Driver 2: Sebastian Vettel
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 75
            else:
                DriverAbility = 33
        elif (teamNo == "5"):
            TeamAbility = 202
            print("Team: McLaren F1 Team")
            print("""
        Driver 1: Lando Norris
        Driver 2: Daniel Ricciardo
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 97
            else:
                DriverAbility = 119
        elif (teamNo == "6"):
            TeamAbility = 181
            print("Team: Alpine F1 Team")
            print("""
        Driver 1: Esteban Ocon
        Driver 2: Fernando Alonso
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 62
            else:
                DriverAbility = 100 # I value Fernando ALonso at this range
        elif (teamNo == "7"):
            TeamAbility = 107
            print("Team: Scuderia AlphaTauri Honda")
            print("""
        Driver 1: Pierre Gasly
        Driver 2: Yuki Tsunoda
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 75
            else:
                DriverAbility = 0
        elif (teamNo == "8"):
            TeamAbility = 8
            print("Team: Alfa Romeo Racing ORLEN")
            print("""
        Driver 1: Kimi Räikkönen
        Driver 2: Antonio Giovinazzi
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 4
            else:
                DriverAbility = 4
        elif (teamNo == "9"):
            TeamAbility = 0
            print("Team: Williams Racing")
            print("""
        Driver 1: George Russell
        Driver 2: Nicholas Latifi
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 3
            else:
                DriverAbility = 0
        elif (teamNo == "10"):
            TeamAbility = 3
            print("Team: Uralkali Haas F1 Team")
            print("""
        Driver 1: Mick Schumacher
        Driver 2: Nikita Mazepin
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 0
            else:
                DriverAbility = 0
        else:
            # Never have this team, prompt user to input details
            print("We have never raced this F1 Team yet:")
            TeamAbility = input("Please enter the predicted Team Ability index, where Mean is 171.9, Max is 573, Min is 0:\nTeam Ability Index: ")
            DriverAbility = input("Please enter the predicted Driver Ability index, where Mean is 82.6, Max is 347, Min is 0:\nDriver Ability Index: ")

        # os.system('cls')

        print()
        print("******************************")
        print("**Model 1: Pit Stop Strategy**")
        print("******************************")
        print()
        initial_pos = input("Please enter the initial position\nInitial Position is: P")
        no_of_pits = input("Please enter the total number of pit stops\nTotal number of pit stops is: ")
        print("Tyre compound choices: C1/C2/C3/C4/C5")
        tyre_grid = input("Please enter the tyre compound used at grid\nTyre Grid is: C")
        tyre_1 = input("Please enter the tyre compound used after 1st pit stop\nTyre 1 is: C")
        tyre_2 = input("Please enter the tyre compound used after 2nd pit stop\nTyre 2 is: C")
        tyre_grid_distance = input("Please enter the travelled distance of the grid tyre compound\nTyre Grid Distance is (in laps): ")
        tyre_1_distance = input("Please enter the travelled distance of the tyre compound after 1st pit stop\nTyre 1 Distance is (in laps): ")
        tyre_2_distance = input("Please enter the travelled distance of the tyre compound after 2nd pit stop\nTyre 2 Distance is (in laps): ")
        sc = input("Please enter the number of pit stops made under safety car conditions\nNumber of pit stops under safety car: ")
        Temperature = input("Please enter the temperature today, you may reference https://www.google.com/search?q=weather as well\nTemperature is (in °F): ")
        Humidity = input("Please enter the humidity today, you may reference https://www.google.com/search?q=weather as well\nHumidity is (in %): ")
        Humidity = float(Humidity) / 100

        # os.system('cls')

        print()
        print("******************************")
        print("**Model 1: Pit Stop Strategy**")
        print("******************************")
        print()
        print("Predicting...")

        # To stop all warnings from outputing
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
        import tensorflow as tf
        tf.autograph.experimental.do_not_convert()
        import warnings
        warnings.filterwarnings("ignore")
        import logging
        logging.getLogger('tensorflow').disabled = True

        
        input_layer = []
        input_layer.append([float(initial_pos), float(no_of_pits), float(tyre_grid), float(tyre_1), float(tyre_2), float(tyre_grid_distance), float(tyre_1_distance), float(tyre_2_distance), 
        float(sc), float(Temperature), float(Humidity), float(Altitude), float(Turns), float(RaceDistance), float(TrackLength), float(TeamAbility), float(DriverAbility)])
        # print(input_layer)

        import keras
        model = keras.models.load_model('saved_model', compile=False)
        prediction = model.predict(input_layer)
        print()
        print("******************************")
        print("**Model 1: Pit Stop Strategy**")
        print("******************************")
        print()
        print("The given conditions are:")
        print("""
        Initial Position: """, float(initial_pos), """
        Number of Pits: """, float(no_of_pits), """
        Tyre grid: """, float(tyre_grid), """
        Tyre 1: """, float(tyre_1), """
        Tyre 2: """, float(tyre_2), """
        tyre_grid_distance: """, float(tyre_grid_distance), """
        tyre_1_distance: """, float(tyre_1_distance), """
        tyre_2_distance: """, float(tyre_2_distance), """
        Pit stops under safety car: """, float(sc), """
        Temperature: """, float(Temperature), """
        Humidity: """, float(Humidity), """
        Altitude: """, float(Altitude), """
        Turns: """, float(Turns), """
        RaceDistance: """, float(RaceDistance), """
        TrackLength: """, float(TrackLength), """
        TeamAbility: """, float(TeamAbility), """
        DriverAbility: """, float(DriverAbility), """
        """)
        print("The predicted final position gained is:", prediction[0][0], "positions")
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        print("Predicted final position is:", ordinal(int(initial_pos)-int(prediction[0][0])))
        print()
        modelNo = input("End of prediction, please enter the model to be used, or press ENTER to exit the program:\n\nModel 1: Pit Stop Strategy\nModel 2: Safety Car Scenario\n\nModel ")
    
    elif (modelNo == "2"):
        # define the input shape, which follows ['initial_pos', 'sc_lap', 'sc_decision', 
        # 'sc_laps_travelled','sc_laps_remaining', 'sc_tyre_compound', 'before_pit_pos', 
        # 'Temperature', 'Humidity', 'Altitude', 'Turns', 'RaceDistance', 'TrackLength', 
        # 'TeamAbility', 'DriverAbility']
       
        print()
        print("********************************")
        print("**Model 2: Safety Car Scenario**")
        print("********************************")
        print()
        print("Please select the circuit")
        print("""
        1. Abu Dhabi: Yas Marina
        2. Australian: Albert Park
        3. Austrian: Red Bull Ring
        4. Azerbaijan: Baku
        5. Bahrain: Bahrain
        6. Bahrain: Sakhir
        7. Belgian: Spa
        8. Brazilian: São Paulo
        9. British: Silverstone
        10. Canada: Montreal
        11. Chinese: Shanghai
        12. French: Paul Ricard
        13. German: Hockenheimring
        14. German: Nürburging
        15. Hungarian: Hungaroring
        16. Italian: Monza
        17. Italian: Imola
        18. Italian: Tuscan (Mugello)
        19. Japanese: Suzuka
        20. Mexican: Mexico City
        21. Monaco: Monte Carlo
        22. Portuguese: Portimão
        23. Russian: Sochi
        24. Singapore: Marina Bay
        25. Spanish: Barcelona-Catalunya
        26. Turkish: Istanbul
        27. UnitedStates: Austin
        28. Others
        """)
        circuitNo = input("Please enter the circuit:\nCircuit ")
        if (circuitNo == "1"):
            Altitude = 10.7
            Turns = 21
            RaceDistance = 55
            TrackLength = 5.554
        elif (circuitNo == "2"):
            Altitude = 2.6
            Turns = 16
            RaceDistance = 58
            TrackLength = 5.303
        elif (circuitNo == "3"):
            Altitude = 63.5
            Turns = 8
            RaceDistance = 71
            TrackLength = 4.318
        elif (circuitNo == "4"):
            Altitude = 26.8
            Turns = 20
            RaceDistance = 51
            TrackLength = 6.003
        elif (circuitNo == "5"):
            Altitude = 16.9
            Turns = 15
            RaceDistance = 57
            TrackLength = 5.412
        elif (circuitNo == "6"):
            Altitude = 19.4
            Turns = 11
            RaceDistance = 87
            TrackLength = 3.543
        elif (circuitNo == "7"):
            Altitude = 102.2
            Turns = 19
            RaceDistance = 44
            TrackLength = 7.004
        elif (circuitNo == "8"):
            Altitude = 43
            Turns = 15
            RaceDistance = 71
            TrackLength = 4.309
        elif (circuitNo == "9"):
            Altitude = 11.3
            Turns = 18
            RaceDistance = 52
            TrackLength = 5.891
        elif (circuitNo == "10"):
            Altitude = 5.2
            Turns = 17
            RaceDistance = 70
            TrackLength = 4.430
        elif (circuitNo == "11"):
            Altitude = 7.4
            Turns = 16
            RaceDistance = 56
            TrackLength = 5.451
        elif (circuitNo == "12"):
            Altitude = 33
            Turns = 15
            RaceDistance = 53
            TrackLength = 5.842
        elif (circuitNo == "13"):
            Altitude = 4.3
            Turns = 15
            RaceDistance = 64
            TrackLength = 5.148
        elif (circuitNo == "14"):
            Altitude = 56.7
            Turns = 15
            RaceDistance = 60
            TrackLength = 5.148
        elif (circuitNo == "15"):
            Altitude = 34.6
            Turns = 13
            RaceDistance = 70
            TrackLength = 3.975
        elif (circuitNo == "16"):
            Altitude = 12.8
            Turns = 11
            RaceDistance = 59
            TrackLength = 5.793
        elif (circuitNo == "17"):
            Altitude = 32
            Turns = 15
            RaceDistance = 63
            TrackLength = 4.909
        elif (circuitNo == "18"):
            Altitude = 43.2
            Turns = 14
            RaceDistance = 58
            TrackLength = 5.338
        elif (circuitNo == "19"):
            Altitude = 40.4
            Turns = 18
            RaceDistance = 53
            TrackLength = 5.807
        elif (circuitNo == "20"):
            Altitude = 2.8
            Turns = 17
            RaceDistance = 71
            TrackLength = 4.304
        elif (circuitNo == "21"):
            Altitude = 42
            Turns = 19
            RaceDistance = 78
            TrackLength = 3.337
        elif (circuitNo == "22"):
            Altitude = 30
            Turns = 15
            RaceDistance = 66
            TrackLength = 4.653
        elif (circuitNo == "23"):
            Altitude = 1.9
            Turns = 18
            RaceDistance = 53
            TrackLength = 5.848
        elif (circuitNo == "24"):
            Altitude = 5.3
            Turns = 23
            RaceDistance = 61
            TrackLength = 5.065
        elif (circuitNo == "25"):
            Altitude = 29.6
            Turns = 16
            RaceDistance = 66
            TrackLength = 4.655
        elif (circuitNo == "26"):
            Altitude = 40.8
            Turns = 15
            RaceDistance = 59
            TrackLength = 5.245
        elif (circuitNo == "27"):
            Altitude = 30.9
            Turns = 20
            RaceDistance = 56
            TrackLength = 5.513
        else:
            # Never raced on this circuit, prompt user to input details
            print("We have never raced in this circuit yet:")
            Altitude = input("Please enter the maximum altitude change of the circuit:\nMaximum altitude change: ")
            Turns = input("Please enter the total number of turns in a lap of the circuit:\nNumber of turns: ")
            RaceDistance = input("Please enter the total number of laps of the circuit:\nNumber of laps: ")
            TrackLength = input("Please enter the length of the circuit:\nTrack Length: ")
        
        # os.system('cls')

        print()
        print("********************************")
        print("**Model 2: Safety Car Scenario**")
        print("********************************")
        print()
        print("Which team is it?")
        print("""
        1. Scuderia Ferrari F1 Team
        2. Mercedes-AMG Petronas Formula One Team    
        3. Red Bull Racing
        4. Aston Martin Cognizant Formula One Team
        5. McLaren F1 Team
        6. Alpine F1 Team
        7. Scuderia AlphaTauri Honda
        8. Alfa Romeo Racing ORLEN
        9. Williams Racing
        10. Uralkali Haas F1 Team
        11. Others
        """)
        teamNo = input("Please enter the team:\nTeam ")
        print()
        if (teamNo == "1"):
            TeamAbility = 131
            print("Team: Scuderia Ferrari F1 Team")
            print("""
        Driver 1: Charles Leclerc
        Driver 2: Carlos Sainz
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 98
            else:
                DriverAbility = 105
        elif (teamNo == "2"):
            TeamAbility = 573
            print("Team: Mercedes-AMG Petronas Formula One Team")
            print("Driver 1: Lewis Hamilton")
            print("Driver 2: Valtteri Bottas")
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 347
            else:
                DriverAbility = 223
        elif (teamNo == "3"):
            TeamAbility = 319
            print("Team: Red Bull Racing")
            print("""
        Driver 1: Max Verstappen
        Driver 2: Sergio Pérez
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 214
            else:
                DriverAbility = 125
        elif (teamNo == "4"):
            TeamAbility = 195
            print("Team: Aston Martin Cognizant Formula One Team")
            print("""
        Driver 1: Lance Stroll
        Driver 2: Sebastian Vettel
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 75
            else:
                DriverAbility = 33
        elif (teamNo == "5"):
            TeamAbility = 202
            print("Team: McLaren F1 Team")
            print("""
        Driver 1: Lando Norris
        Driver 2: Daniel Ricciardo
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 97
            else:
                DriverAbility = 119
        elif (teamNo == "6"):
            TeamAbility = 181
            print("Team: Alpine F1 Team")
            print("""
        Driver 1: Esteban Ocon
        Driver 2: Fernando Alonso
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 62
            else:
                DriverAbility = 100 # I value Fernando ALonso at this range
        elif (teamNo == "7"):
            TeamAbility = 107
            print("Team: Scuderia AlphaTauri Honda")
            print("""
        Driver 1: Pierre Gasly
        Driver 2: Yuki Tsunoda
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 75
            else:
                DriverAbility = 0
        elif (teamNo == "8"):
            TeamAbility = 8
            print("Team: Alfa Romeo Racing ORLEN")
            print("""
        Driver 1: Kimi Räikkönen
        Driver 2: Antonio Giovinazzi
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 4
            else:
                DriverAbility = 4
        elif (teamNo == "9"):
            TeamAbility = 0
            print("Team: Williams Racing")
            print("""
        Driver 1: George Russell
        Driver 2: Nicholas Latifi
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 3
            else:
                DriverAbility = 0
        elif (teamNo == "10"):
            TeamAbility = 3
            print("Team: Uralkali Haas F1 Team")
            print("""
        Driver 1: Mick Schumacher
        Driver 2: Nikita Mazepin
        """)
            driverNo = input("Please enter the Driver\nDriver ")
            if (driverNo == "1"):
                DriverAbility = 0
            else:
                DriverAbility = 0
        else:
            # Never have this team, prompt user to input details
            print("We have never raced this F1 Team yet:")
            TeamAbility = input("Please enter the predicted Team Ability index, where Mean is 171.9, Max is 573, Min is 0:\nTeam Ability Index: ")
            DriverAbility = input("Please enter the predicted Driver Ability index, where Mean is 82.6, Max is 347, Min is 0:\nDriver Ability Index: ")

        # os.system('cls')

        print()
        print("********************************")
        print("**Model 2: Safety Car Scenario**")
        print("********************************")
        print()
        initial_pos = input("Please enter the initial position\nInitial Position is: P")
        sc_lap = input("Please enter the lap when safety car is deployed\nLap when safety car is deployed: Lap ")
        sc_laps_travelled = input("Please enter how many laps have been travelled on the current tyre compound\nLaps travelled is: ")
        sc_laps_remaining = input("Please enter how many laps are remained for the race\nLaps remained is: ")
        print("Tyre compound choices: C1/C2/C3/C4/C5")
        sc_tyre_compound = input("Please enter the currently used tyre compound\nTyre compound is: C")
        before_pit_pos = input("Please enter the current position\nCurrent position is: P")
        Temperature = input("Please enter the temperature today, you may reference https://www.google.com/search?q=weather as well\nTemperature is (in °F): ")
        Humidity = input("Please enter the humidity today, you may reference https://www.google.com/search?q=weather as well\nHumidity is (in %): ")
        Humidity = float(Humidity) / 100

        # os.system('cls')

        print()
        print("********************************")
        print("**Model 2: Safety Car Scenario**")
        print("********************************")
        print()
        print("Predicting...")

        # To stop all warnings from outputing
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
        import tensorflow as tf
        tf.autograph.experimental.do_not_convert()
        import warnings
        warnings.filterwarnings("ignore")
        import logging
        logging.getLogger('tensorflow').disabled = True

        
        input_layer_nopit = []
        input_layer_pitin = []
        
        input_layer_nopit.append([float(initial_pos), float(sc_lap), float(0), float(sc_laps_travelled), float(sc_laps_remaining), float(sc_tyre_compound), float(before_pit_pos), 
        float(Temperature), float(Humidity), float(Altitude), float(Turns), float(RaceDistance), float(TrackLength), float(TeamAbility), float(DriverAbility)])

        input_layer_pitin.append([float(initial_pos), float(sc_lap), float(1), float(sc_laps_travelled), float(sc_laps_remaining), float(sc_tyre_compound), float(before_pit_pos), 
        float(Temperature), float(Humidity), float(Altitude), float(Turns), float(RaceDistance), float(TrackLength), float(TeamAbility), float(DriverAbility)])

        import keras
        model = keras.models.load_model('safetycar/saved_model', compile=False)
        prediction_nopit = model.predict(input_layer_nopit)
        prediction_pitin = model.predict(input_layer_pitin)

        print()
        print("********************************")
        print("**Model 2: Safety Car Scenario**")
        print("********************************")
        print()
        print("The given conditions are:")
        print("""
        Initial Position: """, float(initial_pos), """
        Lap of safety car: """, float(sc_lap), """
        Laps travelled: """, float(sc_laps_travelled), """
        Laps remained: """, float(sc_laps_remaining), """
        Current tyre compound: """, float(sc_tyre_compound), """
        Current position: """, float(before_pit_pos), """
        Temperature: """, float(Temperature), """
        Humidity: """, float(Humidity), """
        Altitude: """, float(Altitude), """
        Turns: """, float(Turns), """
        RaceDistance: """, float(RaceDistance), """
        TrackLength: """, float(TrackLength), """
        TeamAbility: """, float(TeamAbility), """
        DriverAbility: """, float(DriverAbility), """
        """)
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        print("If you choose not to go into the pit now, the predicted final position gained is:", prediction_nopit[0][0], "positions")
        print("Predicted final position is:", ordinal(int(initial_pos)-int(prediction_nopit[0][0])))
        print("If you choose not to go into the pit now, the predicted final position gained is:", prediction_pitin[0][0], "positions")
        print("Predicted final position is:", ordinal(int(initial_pos)-int(prediction_pitin[0][0])))
        if (int(prediction_nopit[0][0]) > int(prediction_pitin[0][0])):
            print("The model suggest that you should go into the pit now!")
        elif (int(prediction_nopit[0][0]) < int(prediction_pitin[0][0])):
            print("The model suggest that you should stay out now!")
        else:
            print("The model suggests no difference in final position changes whether you go into the pit or not.")
        print()
        modelNo = input("End of prediction, please enter the model to be used, or press ENTER to exit the program:\n\nModel 1: Pit Stop Strategy\nModel 2: Safety Car Scenario\n\nModel ")

input("Thank you for using F1 Pit Stop Strategy Prediction model program. Click any button to leave the program!")