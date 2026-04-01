import pandas as pd
import sqlite3
DB_PATH = "data/database.db"

def export(theme, mode, file_format):
    with sqlite3.connect(DB_PATH) as con:
        if mode  == "labeled":
            query = "SELECT * FROM yt_rel WHERE THEME = ? AND RELEVANT IS NOT NULL"
            
        elif mode  == "unlabeled": 
            query =  "SELECT * FROM yt_rel WHERE THEME = ? AND RELEVANT IS NULL"

        elif mode == "all":
            query = "SELECT * FROM yt_rel WHERE THEME = ?"
    
        else:
            raise ValueError("Invalid mode")
        
        df = pd.read_sql_query(query , con, params=(theme,))
        df.drop(columns=["updated_at", "id"], errors="ignore")

        if file_format == "csv":
            df.to_csv(f"data/exports/{theme}_{mode}.csv", index=False)

        elif  file_format  =="xlsx":
            df.to_excel(f"data/exports/{theme}_{mode}.xlsx", index=False)


export("meow", "labeled", "xslx")

    


