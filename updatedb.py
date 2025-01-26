# Файл updatedb.py: обновляет объект класса Person в базе данных

import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.11)
db['Sue Jones'] = sue

db.close()