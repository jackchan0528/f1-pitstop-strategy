import pandas as pd

test = pd.read_csv(
    "aus2019_pitstop.csv",
    # dtype={"1": str,"2": str,"3": str,"4": str,"5": str,"6": str,"7": str,"8": str,"9": str,"10": str,"11": str,"12": str,"13": str,"14": str,"15": str,"16": str,"17": str,"18": str,"19": str,"20": str},
    dtype={"No.": str, "Driver": str, "Team": str, "Lap": int, "Stop": int, "Time": float, "Total Time": float},
    index_col = False
)

standing = pd.read_csv(
    "aus2019.csv",
    dtype={"1": str,"2": str,"3": str,"4": str,"5": str,"6": str,"7": str,"8": str,"9": str,"10": str,"11": str,"12": str,"13": str,"14": str,"15": str,"16": str,"17": str,"18": str,"19": str,"20": str},
    # dtype={"No.": str, "Driver": str, "Team": str, "Lap": int, "Stop": int, "Time": float, "Total Time": float},
    index_col = 0
)


# trial: lap boxed VS position gained
# to know how many positions has one gained/lost
position_delta = {}
for i in range(len(standing.columns)):
    for j in range(len(standing.columns)):
        if standing.loc["Lap 58"][i] == standing.loc["Grid"][j]:
            position_delta[str(standing.loc["Lap 58"][i])] = j-i
            break

df_position_delta = pd.DataFrame(position_delta.items(), columns=["No.", "Position_Delta"])
df_position_delta = df_position_delta.merge(test, on = "No.", how = "left")

# df_position_delta = df_position_delta.groupby(["No.", "Position_Delta",], sort=False, as_index=False).max()

# df_position_delta = df_position_delta[["No.","Position_Delta", "Stop"]]
# print(df_position_delta.dtypes)


print(df_position_delta)

# to implement ML from tensorflow
import tensorflow as tf

import numpy as np
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
# fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

lap_in_pit    = np.array([23,15,25,14,28,14,13,12,27,26,37,15,13,14,27,26,1],  dtype=int)
position_change = np.array([1,-1,1,-1,0,1,4,1,7,5,6,-4,-3,-1,-1,3,3],  dtype=int)

# for i,c in enumerate(lap_in_pit):
#   print("{} th lap in pit = {} position change".format(c, position_change[i]))

# l0 = tf.keras.layers.Dense(units=1, input_shape=[1])

# model = tf.keras.Sequential([l0])


# import matplotlib.pyplot as plt
# plt.xlabel('Epoch Number')
# plt.ylabel("Loss Magnitude")
# plt.plot(history.history['loss'])


l0 = tf.keras.layers.Dense(units=4, input_shape=[1])
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([l0, l1, l2])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
model.fit(lap_in_pit, position_change, epochs=500, verbose=False)
print("Finished training the model")
print("Model predicts that 25 th lap in pit will result in: {} position change".format(model.predict([25])))
# print("These are the l0 variables: {}".format(l0.get_weights()))
# print("These are the l1 variables: {}".format(l1.get_weights()))
# print("These are the l2 variables: {}".format(l2.get_weights()))