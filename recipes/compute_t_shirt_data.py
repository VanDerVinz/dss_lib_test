# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
orders = dataiku.Dataset("orders")
orders_df = orders.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

t_shirt_data_df = orders_df # For this sample code, simply copy input to output


# Write recipe outputs
t_shirt_data = dataiku.Dataset("t_shirt_data")
t_shirt_data.write_with_schema(t_shirt_data_df)
