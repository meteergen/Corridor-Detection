"""
Created: 19/10/2020
@author: AtahanCelebi
"""
import psycopg2
import numpy as np
import csv


try:
    conn = psycopg2.connect(database="Your Data Base",
                            user="postgres",
                            password="Your Password",
                            host="127.0.0.1",
                            port="5432")

    print("Successfully Connected")
except:
    print("Connection failed")


cur = conn.cursor()
###This query finds anormal-segments which are x10 times higher than the average
cur.execute(""" select c1.segmentid, c1.time,c1.travel_time
from combination_table c1
where c1.travel_time > (select avg(c2.travel_time)*10
                        from combination_table c2)
                        order by c1.time asc""")
rows =  cur.fetchall()

    # Extract the column names
anormal_segments = []
anormal_time = []

for row in  rows:
    anormal_segments.append(row[0])
    anormal_time.append(row[1])
dct=dict()
for i,j in zip(anormal_segments,anormal_time):
    dct.setdefault(i,[]).append(j)
print(dct)


csv_columns = ['segmentid','ObservationTime']
csv_file = "AnormalSegments.csv"
#print(len(dct)) #Thanks to Mete
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for key in dct.keys():
        csvfile.write("%s,%s"%(key,""))
        for i in range(len(dct[key])):
            csvfile.write("%s,%s"%(dct[key][i],""))
        csvfile.write("\n")