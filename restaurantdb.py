import pg

db = pg.DB(dbname='restaurant_db')
query = db.query('select * from restaurant')
db.debug = True

name =  'Antico'# raw_input('Enter the name of the restaurant: ')
distance =  3.5 #float(raw_input('distance from ATV : '))
stars = 4.5    #float(raw_input('Stars : '))
category = 'Italian' #raw_input('category : ')
favourite_dish = 'Pizza' #raw_input('What is your favourite dish: ')
takeout =  'Y'#raw_input('Takeout? (Y or N) : ')

query = db.query("insert into restaurant (id,name,distance,stars,category,favourite_dish,takeout) values (default,'%s',%f,%f,'%s','%s','%s')" % (name, distance,stars,category,favourite_dish,takeout))



print query
