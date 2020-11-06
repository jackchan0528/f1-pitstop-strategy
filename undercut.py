import pandas as pd
import numpy as np

def undercut_excel_unboxer(file_location):
    undercut = pd.read_excel(
        file_location, sheet_name="lapsundercut",
        dtype={"No.": str, "laps_undercut_overcut": str, "delta_position": str},
        index_col = 0
    )
    undercut = undercut[["laps_undercut_overcut", "delta_position"]]

    for i in undercut.index:
        # to drop NaN records
        if (pd.isna(undercut["laps_undercut_overcut"][i]) or pd.isna(undercut["delta_position"][i]) ):
            undercut = undercut.drop([i])

    # change data from pandas object to numpy object
    undercut_numpy = undercut.to_numpy()
    # change data type from string to integer
    undercut_numpy = undercut_numpy.astype(int)

    undercut_numpy_lip, undercut_numpy_pc = np.hsplit(undercut_numpy, 2)
    return undercut_numpy_lip, undercut_numpy_pc

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
# print(undercut_numpy_lip, undercut_numpy_pc)

# apply tensorflow logics
import tensorflow as tf
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

lap_in_pit    = undercut_numpy_lip
position_change = undercut_numpy_pc

l0 = tf.keras.layers.Dense(units=4, input_shape=[1])
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=1)

model = tf.keras.Sequential([l0, l1, l2])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(lap_in_pit, position_change, epochs=500, verbose=False)
print("Finished training the model")
print("Model predicts that 25 th lap in pit will result in: {} position change".format(model.predict([25])))