# Python Standard Libraries
import sqlite3
# External Libraries
import pandas as pd


def get_table_data():
    conn = sqlite3.connect("./db/results.db")

    df = pd.read_sql_query("SELECT * from nodes", conn)
    
    # Changing order of columns for layout
    df = df[["id", "name", "info", "cited_by", "depth", "link"]]
   
    return df

