import sqlite3
import pandas as pd
import shutil
from datetime import datetime


# setting paths to datafile and db
data_file = "ose_monsters.csv"
db_path = "../../db.sqlite3"

# create a back up before importing
now = datetime.now()
shutil.copyfile(db_path, f"../back_up_{now}_db.sqlite3")

# setting the name of the table and the query
table = "ose_monster"

# creating a connection
con = sqlite3.connect(db_path)

# reading data from the csv file
new_data = pd.read_csv(data_file, dtype="str")
# add source column
new_data["source"] = "Classic Fantasy"

# Write the new DataFrame to a the SQLite table
new_data.to_sql(table, con, if_exists="append", index=False)


# close the connection to the db
con.close()

print(f"Succès ! {len(new_data)} monstres ont été importés")
