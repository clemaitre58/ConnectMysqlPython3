#!/usr/bin/env python
from __future__ import print_function

import pymysql

conn = pymysql.connect(host='glapeira.freeboxos.fr', port=3306, user='cedric', passwd='cedb002', db='TempRPIZero01')

cur = conn.cursor()

cur.execute("SELECT * FROM Temp")

print(cur.description)

print()

for row in cur:
        print(row)

cur.close()
conn.close()
