#!flask/bin/python
from flask import Flask,jsonify,request
from pymongolab import Connection

#pip install Flask-PyMongo
from flask.ext.pymongo import PyMongo


app = Flask(__name__)

#This is makes the connection to Mongolabs
connection = Connection("15bcI8yedImO3qWvB6bZncbz_v3VONO3")

#This is the connection to our DB called "hw1"
db = connection.hw1

#This is the actual collection/table called recipes
collection = db.recipes

#Just to initialize our sample database
test_recipes = [
	
	{
		'id' : 1,
		'title' : u'lasagna',
		'description' : u'a yummy italian dish!',
		'stars' : 3
	},
	{
		'id' : 2,
		'title' : u'sausage',
		'description' : u'a bad german dish! meat is murder',
		'stars' : 4
	}
]

try: 
	collection.insert(recipes)
except: 
	print("already initialized the DB")


# To figure out how to interact wit the DB check out: http://api.mongodb.org/python/current/tutorial.html
col = collection.find_one()
print(col)

# #this GET returns all of the recipes
# @app.route('/api/1.0/recipes', methods=['GET'])
# def get_recipes():
#     return jsonify({'recipes':test_recipes})


#this GET returns all of the recipes
@app.route('/api/1.0/recipes', methods=['GET'])
def get_recipes():
    total = []
    for recipe in collection.find():
    	total.append(recipe)
    
 	return total  

#this GET returns a specific recipe based on the ID 
@app.route('/api/1.0/recipes/<int:recipe_id>',methods=['GET'])
def get_recipe(recipe_id):
	recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
	return jsonify({'recipe':recipe[0]})

#this is a POST request used to create a recipe see the curl_tests to see how to make a new object
@app.route('/api/1.0/recipes',methods=['POST'])
def create_recipe():
	if not request.json or not 'title' in request.json:
		return "BAD POST"

	recipe = {
		'id': recipes[-1]['id'] + 1,
		'title': request.json['title'],
		'description' : request.json.get('description'),
		'stars' : request.json.get('stars')
	}

	recipes.append(recipe)
	return jsonify({'recipe': recipe}),201

# This is PUT request to modify an object 
@app.route('/api/1.0/recipes/<int:recipe_id>',methods=['PUT'])
def modify_recipe(recipe_id):
	recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
	recipe[0]['title'] = request.json.get('title', recipe[0]['title'])
	recipe[0]['description'] = request.json.get('description', recipe[0]['description'])
	recipe[0]['stars'] = request.json.get('stars', recipe[0]['stars'])
	return jsonify({'recip': recipe[0]})

# This is DELETE request to delete a recipe based on the ID
@app.route('/api/1.0/recipies/<int:recipe_id>',methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
    recipies.remove(recipe[0])
    return jsonify({'result':True})


if __name__ == '__main__':
    app.run(debug=True)