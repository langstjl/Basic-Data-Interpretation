#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:52:30 2023

@author: Jeff
"""

import pandas as pd

melbourne_file_path = ('file_path')

melbourne_data = pd.read_csv(melbourne_file_path)

melb_data_descript = (melbourne_data.describe())
print (melb_data_descript)

melb_columns = melbourne_data.columns
print (melb_columns)

melb_price = melbourne_data.Price
print ('The average home price in Melbourne is', round((sum(melb_price) / len(melb_price)), 2), 'dollars.')


y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x = melbourne_data [melbourne_features]
print (x.describe())
print (x.head())

from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor(random_state=(1))

print (melbourne_model.fit(x,y))
print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are:")
print(melbourne_model.predict(x.head()))

from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(x)
print ('The mean absolute error of our data is:', mean_absolute_error(y, predicted_home_prices))

from sklearn.model_selection import train_test_split

train_x, val_x, train_y, val_y = train_test_split(x, y, random_state = 0)

# Define model.
melbourne_model = DecisionTreeRegressor()

# Fit model.
melbourne_model.fit(train_x, train_y)

# Get predicted prices on validation data.
val_predictions = melbourne_model.predict(val_x)
print (mean_absolute_error(val_y, val_predictions)) 


def get_mae (max_leaf_nodes, train_x, val_x, train_y, val_y) :
    model = DecisionTreeRegressor(max_leaf_nodes=(max_leaf_nodes) , random_state=(0) )
    model.fit(train_x, train_y)
    preds_val = model.predict(val_x)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)

for max_leaf_nodes in [5, 50, 500, 505, 510, 5000, 50000] :
    my_mae = get_mae(max_leaf_nodes, train_x, val_x, train_y, val_y)
    print ('Max leaf nodes %d \t\t Mean Absolute Error: %d' %(max_leaf_nodes, my_mae))
    
best_tree_size = 505
    
final_model = DecisionTreeRegressor(max_leaf_nodes = best_tree_size, random_state = 0)
print (final_model.fit(x, y))

from sklearn.ensemble import RandomForestRegressor

forest_model = RandomForestRegressor(random_state = 1)
forest_model.fit(train_x, train_y)
melb_preds = forest_model.predict(val_x)
print (mean_absolute_error(val_y, melb_preds))