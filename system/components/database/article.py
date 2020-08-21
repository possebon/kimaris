# Python Standard Libraries
import sqlite3
# External Libraries
import pandas as pd



def get_article(name):
    conn = sqlite3.connect("./db/results.db")
    df = pd.read_sql_query(f"""
    SELECT * from nodes
    WHERE name = "{name}";
    """, conn)
    
    # Changing order of columns for layout
    df = df[["id", "name", "info", "cited_by", "depth", "link"]]
    return df