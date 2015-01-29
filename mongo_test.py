from pymongolab import Connection

#This is makes the connection to Mongolabs
connection = Connection("15bcI8yedImO3qWvB6bZncbz_v3VONO3")

#This is the connection to our DB called "hw1"
db = connection.hw1

#This is the actual collection/table called recipes
collection = db.recipes

#This is a test valye
test_1 ={
		'id' : 1,
		'title' : u'lasagna',
		'description' : u'a yummy italian dish!',
		'stars' : 3
	}

test_2 = {
		'id' : 2,
		'title' : u'sausage',
		'description' : u'a bad german dish! meat is murder',
		'stars' : 4
	}


collection.insert(test_1)
collection.insert(test_2)

col = collection.find_one()
print(col)