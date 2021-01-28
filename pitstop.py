from numpy.core.fromnumeric import transpose
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import activations
import pandas as pd
import numpy as np
import sys


from tensorflow.python.keras.layers.core import Dropout
pd.options.mode.chained_assignment = None  # default='warn'
# np.set_printoptions(threshold=sys.maxsize)

def excel_unboxer(file_location):
    # 1. Undercut VS Probability of Undercut
    # 2. Overcut VS Probability of Overcut
    undercut = pd.read_excel(
        file_location, sheet_name="lapsundercut",
        dtype={"No.": str, "laps_undercut_overcut": str, "delta_position": str},
        index_col = 0
    )

    # 3. Compound chnage
    compound = pd.read_excel(
        file_location, sheet_name="compoundchange",
        dtype={"tyre_grid": str, "tyre_1": str, "tyre_2": str, "tyre_grid_distance": str, "tyre_1_distance": str, "tyre_2_distance": str, "sc": str, "final_pos_gained": str},
        index_col = None
    )

    # 4. Track temperature
    weather = pd.read_excel(
        file_location, sheet_name="weather",
        dtype={"Skycondition": str, "Precipation type": str, "Temperature": str, "Humidity": str, "Wind speed": str, "Wind bearing": str},
        index_col = 0
    ).T

    temperature = weather[["Temperature"]]
    temperature["Temperature"] = temperature["Temperature"].str[:-2]
    temperature["Temperature"] = temperature["Temperature"].astype(float)
    # temperature["Temperature"] = temperature["Temperature"].str[0]
    
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

    print("Reading from: " + file_location)
    # Combine all factors
    # combined_table = undercut[["laps_undercut_overcut", "delta_position"]]
    combined_table = compound[["No.", "initial_pos", "final_pos", "no_of_pits", "tyre_grid", "tyre_1", "tyre_2", "tyre_grid_distance", "tyre_1_distance", "tyre_2_distance", "sc", "final_pos_gained"]]
    combined_table["Temperature"] = ""
    combined_table["Humidity"] = ""
    combined_table["Altitude"] = ""
    combined_table["TeamAbility"] = ""
    combined_table["DriverAbility"] = ""
    for i in combined_table.index:
        combined_table["Temperature"][i] = float(temperature.values)
        combined_table["Humidity"][i] = float(humidity.values)
        combined_table["Altitude"][i] = float(altitude.columns.values[0])
        # combined_table["TeamAbility"][i] = 0
        for n in fastestlap.index:
            
            if (str(combined_table["No."][i]) == str(fastestlap["No."][n]) and "2019" in file_location):
                # print(combined_table["No."][i], fastestlap["No."][n])
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
                # print(combined_table["No."][i], fastestlap["No."][n])
                # print(str(fastestlap["Driver"][n]))
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
                # print(combined_table["No."][i], fastestlap["No."][n])
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
                # print(combined_table["No."][i], fastestlap["No."][n])
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
                # print(combined_table["No."][i], fastestlap["No."][n])
                # print(str(fastestlap["Driver"][n]))
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


    # reorder the columns
    combined_table = combined_table[["No.", "initial_pos", "no_of_pits", "tyre_grid", "tyre_1", "tyre_2", "tyre_grid_distance", "tyre_1_distance", "tyre_2_distance", "sc", "Temperature", "Humidity", "Altitude", "TeamAbility", "DriverAbility", "final_pos_gained"]]
    # combined_table = combined_table[["initial_pos", "final_pos", "no_of_pits", "tyre_grid","final_pos_gained"]]


    for i in combined_table.index:
        # to drop NaN records
        # if (pd.isna(combined_table["laps_undercut_overcut"][i]) or pd.isna(combined_table["delta_position"][i]) ):
        #     combined_table = combined_table.drop([i])
        if (
            pd.isna(combined_table["tyre_2"][i]) 
            or pd.isna(combined_table["final_pos_gained"][i])
            or combined_table["tyre_grid"][i] == "W" 
            or combined_table["tyre_grid"][i] == "I"
            or combined_table["tyre_1"][i] == "W" 
            or combined_table["tyre_1"][i] == "I"
            or combined_table["tyre_2"][i] == "W" 
            or combined_table["tyre_2"][i] == "I"
            
            # or (combined_table["No."][i] == 44
            # or combined_table["No."][i] == 77
            # or combined_table["No."][i] == 33
            # or combined_table["No."][i] == 5
            # or combined_table["No."][i] == 16)

            # or (combined_table["No."][i] != 44
            # and combined_table["No."][i] != 77
            # and combined_table["No."][i] != 33
            # and combined_table["No."][i] != 5
            # and combined_table["No."][i] != 16)
            # or combined_table["final_pos"][i] == "DNF"
            # or combined_table["final_pos"][i] == "DSQ"  
            ):
            combined_table = combined_table.drop([i])

    # combined_table = combined_table[["initial_pos", "no_of_pits", "tyre_grid", "tyre_1", "tyre_2", "tyre_grid_distance", "tyre_1_distance", "tyre_2_distance", "Temperature", "Humidity", "Altitude", "final_pos_gained"]]
    combined_table = combined_table[["initial_pos", "no_of_pits", "tyre_grid", "tyre_1", "tyre_2", "tyre_grid_distance", "tyre_1_distance", "tyre_2_distance", "sc", "TeamAbility", "DriverAbility", "final_pos_gained"]]

    # change data from pandas object to numpy object
    # combined_table_numpy = combined_table.to_numpy()
    # change data type from string to integer
    # combined_table_numpy = combined_table_numpy.astype(float)

    # change data type of input and result
    # combined_table_numpy_input = combined_table_numpy[:,:4].astype(float) # redundant to set to float again
    # combined_table_numpy_input = combined_table_numpy[:,:11]
    # combined_table_numpy_result = combined_table_numpy[:,-1].astype(int)

    # return combined_table_numpy_input, combined_table_numpy_result
    combined_table = combined_table.astype(float)
    return combined_table

# -----------------------------------------------------------------------------------------------------------------

# calling all data2019.xlsx files
file_names_2019 = ["abudhabi2019", "austrian2019", "azerbaijan2019", "bahrain2019", "belgian2019", 
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
# make australian 2019 as the first one to be read in, so to make the numpy array not null when concatenating
# numpy_input, numpy_result = excel_unboxer("./data2018/australian2018.xlsx")
dataset = excel_unboxer("./data2019/australian2019.xlsx")
for i in file_names_2019:
    temp_dataset = excel_unboxer("./data2019/"+i+".xlsx")
    dataset = pd.concat([dataset, temp_dataset], axis = 0)
for i in file_names_2018:
    temp_dataset = excel_unboxer("./data2018/"+i+".xlsx")
    dataset = pd.concat([dataset, temp_dataset], axis = 0)
for i in file_names_2017:
    temp_dataset = excel_unboxer("./data2017/"+i+".xlsx")
    dataset = pd.concat([dataset, temp_dataset], axis = 0)

# # read in team ability and driver ability data
# undercut = pd.read_excel(
#     "./data2014-2020/data.xlsx", sheet_name="2019_constructors",
#     dtype={"Team": str, "Pos.": str, "Points": str},
#     index_col = 0
# )



# print(dataset)


# apply tensorflow logics
import tensorflow as tf
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# split the dataset into train data and test data
from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(numpy_input, numpy_result, test_size=0.2)
# train_dataset, x_test, y_train, y_test = train_test_split(numpy_input, numpy_result, test_size=0.2)
dataset = dataset.reset_index(drop=True)

print(dataset)

train_dataset = dataset.sample(frac=0.7, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
# print("train_dataset:")
# print(train_dataset.to_string())
# print("test_dataset:")
# print(test_dataset.to_string())

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop("final_pos_gained")
test_labels = test_features.pop("final_pos_gained")

# print("debug")
# print(test_features.to_string())
# print("length of train_features:", len(train_features))
# print(train_features)

from tensorflow.keras.layers.experimental import preprocessing
normalizer = preprocessing.Normalization()
# print(train_features.dtypes)
normalizer.adapt(np.array(train_features))

# def build_and_compile_model(norm):
#     model = keras.Sequential([
#         norm,
#         layers.Dense(64, activation='relu'),
#         layers.Dense(64, activation='relu'),
#         layers.Dense(1)
#         ])

#     model.compile(loss='mean_absolute_error', optimizer=tf.keras.optimizers.Adam(0.001))
#     return model

from tensorflow.keras import regularizers

# model = build_and_compile_model(normalizer)
model = keras.Sequential([normalizer,
        layers.Dense(256, kernel_regularizer=regularizers.l2(0.001), activation='relu'),
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

# # F-score selection
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import f_classif

# selector = SelectKBest(f_classif, k='all')
# selected_features = selector.fit_transform(train_features, train_labels)

noOfEpochs = 1000

# model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=[soft_accuracy])
model.compile(loss='mean_squared_error', optimizer='rmsprop')
print(model.summary())
history = model.fit(train_features, train_labels, epochs=noOfEpochs, verbose=1, validation_split=0.2)

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
# plt.show()

# plt.subplot(1, 2, 2)
# plt.xlabel('Epoch Number')
# plt.ylabel("Accuracy")
# # plt.plot(range(500), history.history['loss'], label='loss')
# plt.plot(range(noOfEpochs), history.history['soft_accuracy'], label='accuracy')
# plt.plot(range(noOfEpochs), history.history['val_soft_accuracy'], label='test_accuracy')
# plt.legend(['train', 'test'], loc='upper right')
# plt.title('Training and Validation Loss')
plt.show()

print("now evaluating:")
results = model.evaluate(test_features, test_labels, batch_size=128, verbose=0)
print("test loss, test acc:", results)

# print("Generate predictions for 3 samples")
# predictions = model.predict(test_features[:3])
# print("predictions shape:", predictions.shape)

# test_results['model'] = model.evaluate(test_features, test_labels, verbose=0)

# model.add(layers.Dense(256, input_dim=11, activation='selu', name="layer1"))
# model.add(layers.Dense(128, activation='selu', name="layer2"))
# model.add(layers.Dense(64, activation='selu', name="layer3"))
# model.add(layers.Dense(64, activation='selu', name="layer4"))
# model.add(layers.Dense(32, activation='selu', name="layer5"))
# model.add(layers.Dense(16, activation='selu', name="layer6"))
# model.add(layers.Dense(12, activation='selu', name="layer7"))
# model.add(layers.Dense(1, activation='selu', name="layer8"))
# print(model.summary())

# model = keras.Sequential()
# model.add(layers.Dense(256, input_dim=11, activation='selu', name="layer1"))
# model.add(layers.Dense(128, activation='selu', name="layer2"))
# model.add(layers.Dense(64, activation='selu', name="layer3"))
# model.add(layers.Dense(64, activation='selu', name="layer4"))
# model.add(layers.Dense(32, activation='selu', name="layer5"))
# model.add(layers.Dense(16, activation='selu', name="layer6"))
# model.add(layers.Dense(12, activation='selu', name="layer7"))
# model.add(layers.Dense(1, activation='selu', name="layer8"))


# def soft_accuracy(y_true, y_pred):
#     return keras.backend.mean(keras.backend.equal(keras.backend.round(y_true), keras.backend.round(y_pred)))

# # model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1), metrics=[soft_accuracy])
# model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=[soft_accuracy])
# history = model.fit(x_train, y_train, epochs=1000, verbose=2, validation_split=0.2)

# save the model
model.save('saved_model/')
# model.save('complete_saved_model/')

# load the model, no need to train a model again
model = keras.models.load_model('saved_model', compile=False, custom_objects={'soft_accuracy': soft_accuracy})
# model = keras.models.load_model('complete_saved_model/')



print("Finished training the model")
# # combined_table = combined_table[["initial_pos", "no_of_pits", "tyre_grid", "tyre_1", "tyre_2", "tyre_grid_distance", "tyre_1_distance", "tyre_2_distance", "Temperature", "Humidity", "Altitude", "final_pos_gained"]]
# print("Model predicts that the condition specified by \"", "[2,1,1,4,3,3,23,35,0,78.61,0.47,2.6]", "\" will result in: {} position change".format(model.predict([[2,1,4,3,3,23,35,0,78.61,0.47,2.6]])))
# print("Model predicts that the condition specified by \"", "[2,1,4,3,3,23,35,0,1]", "\" will result in: {} position change".format(model.predict([[2,1,4,3,3,23,35,0,1]])))

# "abudhabi2019"
test_dataset = excel_unboxer("./data2019/abudhabi2019.xlsx") #pandas dataframe
test_result = test_dataset.pop("final_pos_gained")
print(test_dataset.values.tolist())
print("Model predicts the Abu Dhabi 2019 result be: ")
ct = 0
for i in test_dataset.values.tolist():
    prediction = int(np.round(model.predict([i]))[0])
    answer = int(test_result.values.tolist()[ct])
    print("Prediction is:", prediction, ", Answer is:", answer, ", Difference is:", answer - prediction)
    # print("For reference, the answer is: ", test_result.values.tolist()[ct])
    ct+=1



# import matplotlib.pyplot as plt
# # plt.figure(figsize=(8, 8))
# plt.subplot(1, 2, 1)
# plt.xlabel('Epoch Number')
# plt.ylabel("Loss Magnitude")
# plt.plot(range(1000), history.history['loss'], label='loss')
# plt.plot(range(1000), history.history['val_loss'], label='val_loss')
# # plt.plot(range(500), history.history['soft_accuracy'], label='accuracy')
# plt.legend(['train', 'test'], loc='upper right')
# plt.title('Training and Validation Loss')
# # plt.show()

# plt.subplot(1, 2, 2)
# plt.xlabel('Epoch Number')
# plt.ylabel("Accuracy")
# # plt.plot(range(500), history.history['loss'], label='loss')
# plt.plot(range(1000), history.history['soft_accuracy'], label='accuracy')
# plt.plot(range(1000), history.history['val_soft_accuracy'], label='test_accuracy')
# plt.legend(['train', 'test'], loc='upper right')
# plt.title('Training and Validation Loss')
# plt.show()


# # print("These are the l0 variables: {}".format(l0.get_weights()))
# # print("These are the l1 variables: {}".format(l1.get_weights()))
# # print("These are the l2 variables: {}".format(l2.get_weights()))

# # Evaluate the model by test data set
# # print("Now evaluating the model")
# # model.evaluate(x_test, y_test, batch_size = 32, verbose = 2)