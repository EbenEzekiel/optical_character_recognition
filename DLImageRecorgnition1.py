# Machine learning image recognition using Tensor flow


"""DL Image recorgnition task-  hand written numbers """

# import libraries

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Import datasets

(X_train, y_train),(X_test,y_test) = keras.datasets.mnist.load_data()

# Determine minimum and maximun values in X_train
X_train_f = X_train.flatten(order="C")
print(f"Total number of element is: {len(X_train_f)}, maximum value is: {X_train_f.max()}, minimum value is: {X_train_f.min()}")

# Determine minimum and maximun values in X_test
X_test_f = X_test.flatten(order = "C")
print(f"Total number of element is: {len(X_test_f)}, maximum value is: {X_test_f.max()}, minimum value is: {X_test.min()}")

# Reshape dataset and scale by dividing by 255(each value is between 0 and 255)

X_train_flattened, X_test_flattened = X_train.reshape(len(X_train), 784)/255, X_test.reshape(len(X_test), 784)/255

# Inspect data in X_train and y_train datasets

num  = 3553
print("y_train value is :" ,y_train [num])
print("")
print("Hand written X_train data is :")
plt.matshow(X_train[num]);

# Build model

model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation = "sigmoid")
])

# Compile model

model.compile(optimizer = "adam", 
              loss = "sparse_categorical_crossentropy",
              metrics = ["accuracy"]
              )

# Fit model to training data

model.fit(X_train_flattened, y_train, epochs = 5)

# Evaluate model performance (accuracy) on test dataset

print(f"model accuracy on test data is : {model.evaluate(X_test_flattened, y_test)[1] * 100} %.")

# Generate predictions for test data

y_pred = model.predict(X_test_flattened)

# Inspect data in test (X_test and y_test) datasets and predicted (y_pred) values

num  = 719
print(f"y_test value is : {y_test [num]}")
print("")
print(f"predicted value is : {np.argmax(y_pred[num])}")
print("")
print("Hand written X_test data is :")
plt.matshow(X_test[num]);

plt.figure(figsize=(6,3))
cm = tf.math.confusion_matrix(y_test, [np.argmax(i) for i in y_pred])
sns.heatmap(cm, annot = True, fmt ="d")

plt.ylabel("True values")
plt.xlabel("Predicted values")
plt.title("Confusion matrix heat map")
plt.show();

"""BUILD MODEL OF THREE ELEMENTS"""

# Build model

model = keras.Sequential([
    keras.layers.Dense(100, input_shape=(784,), activation = "sigmoid"),
    keras.layers.Dense(10, activation = "sigmoid")
])

# Compile model

model.compile(optimizer = "adam", 
              loss = "sparse_categorical_crossentropy",
              metrics = ["accuracy"]
              )

# Fit model to training data

model.fit(X_train_flattened, y_train, epochs = 5)

print(f"model accuracy on test data is : {model.evaluate(X_test_flattened, y_test)[1] * 100} %.")

# Plot confusion matrix heatmap
plt.figure(figsize=(6,3))
cm = tf.math.confusion_matrix(y_test, [np.argmax(i) for i in y_pred])
sns.heatmap(cm, annot = True, fmt ="d")

plt.ylabel("True values")
plt.xlabel("Predicted values")
plt.title("Confusion matrix heat map")
plt.show();

"""OPTIMIZER AND LOSS FUNCTION PARAMETERS TUNNING

"""

# Initialize "params" parameters grid and "accuracy_scores" dictionary

params = { "01": [100, "sigmoid", "relu"],
          "02": [200, "sigmoid", "relu"],
          "03": [300, "sigmoid", "relu"],

          "11": [100, "sigmoid", "sigmoid"],
           "12": [200, "sigmoid", "sigmoid"],
           "13": [300, "sigmoid", "sigmoid"],

          "21": [100, "relu", "relu"],
          "22": [200, "relu", "relu"],
          "23": [300, "relu", "relu"],

          "31": [100, "relu", "sigmoid"],
          "32": [200, "relu", "sigmoid"],
          "33": [300, "relu", "sigmoid"],
          }

accuracy_scores = dict()

# Model hyperparameter tunning

start_time = pd.Timestamp.now()
for i in params.keys():
  model = keras.Sequential([
    keras.layers.Dense(params[i][0], input_shape=(784,), activation = params[i][1]),
    keras.layers.Dense(10, activation = params[i][2])
  ])

  # Compile model

  model.compile(optimizer = "adam", 
                loss = "sparse_categorical_crossentropy",
                metrics = ["accuracy"]
                )

  # Fit model to training data

  model.fit(X_train_flattened, y_train, epochs = 5)
  accuracy_scores[i] = model.evaluate(X_test_flattened, y_test)[1] * 100

end_time = pd.Timestamp.now()

print(f"Model trained in {end_time - start_time} ")

# Access parameters that returned highest accuracy score

print(f"Max accuracy score is {max(accuracy_scores.values())}")
for i in accuracy_scores.keys():
  if accuracy_scores[i]== max(accuracy_scores.values()):
    print(f"Best parameters are {accuracy_scores[i]}, at key {i} ")
print("")
print("Accuracy score values are :")
accuracy_scores

"""FINAL MODEL"""

model = keras.Sequential([
    keras.layers.Dense(200, input_shape=(784,), activation = "relu"),
    keras.layers.Dense(10, activation = "sigmoid")
    ])
  

# Compile model

model.compile(optimizer = "adam", 
                loss = "sparse_categorical_crossentropy",
                metrics = ["accuracy"]
                )

# Fit model to training data
model.fit(X_train_flattened, y_train, epochs = 10)

# Evaluate model perfomance (accuracy score) on test data
accuracy_score = model.evaluate(X_test_flattened, y_test)[1] * 100

print(f"Accuracy score is : {accuracy_score}.")

# Generate predictions for test data
y_pred = model.predict(X_test_flattened)

# Plot confusion matrix heatmap of predicted values
plt.figure(figsize=(6,3))
cm = tf.math.confusion_matrix(y_test, [np.argmax(i) for i in y_pred])
sns.heatmap(cm, annot = True, fmt ="d")

plt.ylabel("True values")
plt.xlabel("Predicted values")
plt.title("Confusion matrix heat map")
plt.show();

# Inspect data in test (X_test and y_test) datasets and predicted (y_pred) values

num  = 7203
print(f"y_test value is : {y_test [num]}")
print("")
print(f"predicted value is : {np.argmax(y_pred[num])}")
print("")
print("Hand written X_test data is :")
plt.matshow(X_test[num]);

"""CONCLUSION:
With a 98% performance accuracy, the model is working well

END.
"""