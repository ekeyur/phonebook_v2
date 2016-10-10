import pg

db = pg.DB(dbname='phonebook_db')
#query = db.query('select * from restaurant')

db.debug = True

user_input = 0
while user_input != 5:
    print "\n"
    print "Electronic Phone Book"
    print "====================="
    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Quit"
    #print "6\. Quit"

    user_input = int(raw_input("What do you want to do (1 - 5) >> "))

    if (user_input == 1):
        name = raw_input("Name : ")
        query = db.query("select * from phonebook where name = '%s'" % (name))
        print query

    if (user_input == 2):
        name = raw_input("Name : ")
        number = raw_input("Number (xxx-xxx-xxxx): ")
        email = raw_input("Email : ")
        query = db.query("insert into phonebook (id,name,phone_number,email) values(default,'%s','%s','%s')" % (name,number,email))
        print query

    if (user_input == 3):
        name = raw_input("Name : ")
        query = db.query("Delete from phonebook where name = '%s'" % (name))

    if (user_input == 4):
        query = db.query('Select * from phonebook')
        print query

    if (user_input == 5):
        print "Bye"
        break
