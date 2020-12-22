from numpy.core.fromnumeric import transpose
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

def undercut_excel_unboxer(file_location):
    undercut = pd.read_excel(
        file_location, sheet_name="lapsundercut",
        dtype={"No.": str, "laps_undercut_overcut": str, "delta_position": str},
        index_col = 0
    )

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

    # print(temperature["Temperature"].values)
    # print(humidity["Humidity"].values)
    

    combined_table = undercut[["laps_undercut_overcut", "delta_position"]]
    combined_table["Temperature"] = ""
    combined_table["Humidity"] = ""
    for i in combined_table.index:
        combined_table["Temperature"][i] = float(temperature.values)
        combined_table["Humidity"][i] = float(humidity.values)

    # reorder the columns
    combined_table = combined_table[["laps_undercut_overcut", "Temperature", "Humidity", "delta_position"]]

    for i in combined_table.index:
        # to drop NaN records
        if (pd.isna(combined_table["laps_undercut_overcut"][i]) or pd.isna(combined_table["delta_position"][i]) ):
            combined_table = combined_table.drop([i])


    # print(combined_table)

    # change data from pandas object to numpy object
    combined_table_numpy = combined_table.to_numpy()
    # change data type from string to integer
    combined_table_numpy = combined_table_numpy.astype(float)

    # print(combined_table_numpy)
    # print(np.shape(combined_table_numpy)[1])

    # np.array_split(combined_table_numpy_lip, split_idx, axis=0)

    # combined_table_numpy_lip, combined_table_numpy_pc = np.array_split(combined_table_numpy, 3, axis=1)
    combined_table_numpy_lip = combined_table_numpy[:,:3].astype(float)
    combined_table_numpy_pc = combined_table_numpy[:,-1].astype(int)

    # print(combined_table_numpy_lip)
    # print(combined_table_numpy_pc)
    return combined_table_numpy_lip, combined_table_numpy_pc

# calling all data2019.xlsx files
file_names = ["abudhabi2019", "austrian2019", "azerbaijan2019", "bahrain2019", "belgian2019", 
"brazilian2019", "british2019", "canada2019", "chinese2019", "french2019", "german2019", 
"hungarian2019", "italian2019", "japanese2019", "mexican2019", "monaco2019", "russian2019", 
"singapore2019", "spanish2019", "unitedstates2019"]
# make australian 2019 as the first one to be read in, so to make the numpy array not null when concatenating
undercut_numpy_lip, undercut_numpy_pc = undercut_excel_unboxer("./data2019/australian2019.xlsx")
for i in file_names:
    tp_undercut_numpy_lip, tp_undercut_numpy_pc = undercut_excel_unboxer("./data2019/"+i+".xlsx")
    undercut_numpy_lip = np.concatenate((undercut_numpy_lip, tp_undercut_numpy_lip), axis = 0)
    undercut_numpy_pc = np.concatenate((undercut_numpy_pc, tp_undercut_numpy_pc), axis = 0)

print(undercut_numpy_lip)
print(undercut_numpy_pc)

# # concatenate other factors
# undercut_numpy_lip = undercut_numpy_lip.tolist()
# for i in undercut_numpy_lip:
#     i.append(300)
# undercut_numpy_lip = np.array(undercut_numpy_lip)
# print(undercut_numpy_lip)
# print(undercut_numpy_lip, undercut_numpy_pc)

# apply tensorflow logics
import tensorflow as tf
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

lap_in_pit    = undercut_numpy_lip
position_change = undercut_numpy_pc

# input shape means how many input is taken
l0 = tf.keras.layers.Dense(units=4, input_shape=[3])
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=1)

model = tf.keras.Sequential([l0, l1, l2])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(lap_in_pit, position_change, epochs=500, verbose=False)
print("Finished training the model")
print("Model predicts that 25 th lap in pit will result in: {} position change".format(model.predict([[25,79,0.55]])))