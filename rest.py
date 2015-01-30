#!flask/bin/python
from flask import Flask,jsonify,request, make_response
from pymongolab import Connection

app = Flask(__name__)

#This makes the connection to Mongolabs
connection = Connection("15bcI8yedImO3qWvB6bZncbz_v3VONO3")
#This is the connection to our DB called "hw1"
db = connection.hw1

#calculate count, this is a one time cost
count = db.recipes.find()[db.recipes.count() -1]['id']

#this GET returns all of the recipes
@app.route('/api/1.0/recipes', methods=['GET'])
def get_recipes():
	recipelist = []
	for recipe in db.recipes.find():
		recipelist.append ({
				'id': recipe[u'id'],
				'title': recipe[u'title'],
				'description' : recipe[u'description'],
				'stars' : recipe[u'stars']
		})
	return jsonify({'recipe':recipelist})

#this GET returns a specific recipe based on the ID 
@app.route('/api/1.0/recipes/<int:recipe_id>',methods=['GET'])
def get_recipe(recipe_id):
	try:
		col = db.recipes.find_one({'id' : recipe_id})
	
		recipe = {
				'id': col[u'id'],
				'title': col[u'title'],
				'description' : col[u'description'],
				'stars' : col[u'stars']
		}
	except TypeError:
		return not_found("Out of Range")
	return jsonify(**recipe)

#this is a POST request used to create a recipe see the curl_tests to see how to make a new object
@app.route('/api/1.0/recipes',methods=['POST'])
def create_recipe():
	if not request.json or not 'title' in request.json:
		return "BAD POST"
	global count
	count = count + 1
	recipe = {
		'id': count,
		'title': request.json['title'],
		'description' : request.json.get('description'),
		'stars' : request.json.get('stars')
	}

	db.recipes.insert(recipe)
	return jsonify({'recipe': recipe}),201

# This is PUT request to modify an object 
@app.route('/api/1.0/recipes/<int:recipe_id>',methods=['PUT'])
def modify_recipe(recipe_id):
	try:
		col = db.recipes.find_one({'id' : recipe_id})
	
		recipe = {
				'id': col[u'id'],
				'title': col[u'title'],
				'description' : col[u'description'],
				'stars' : col[u'stars']
		}
	except TypeError:
		return not_found("Out of Range")

	recipe['title'] = request.json.get('title', recipe['title'])
	recipe['description'] = request.json.get('description')
	recipe['stars'] = request.json.get('stars') 

	if(recipe['title'] != None):
		db.recipes.update({'id': recipe['id']}, {'$set' : {'title' : recipe['title']}})

	if(recipe['description'] != None):
		db.recipes.update({'id': recipe['id']}, {'$set' : {'description' : recipe['description']}})	

	if(recipe['stars'] != None):
		db.recipes.update({'id': recipe['id']}, {'$set' : {'stars' : recipe['stars']}})
	
	return jsonify({'recipe': recipe})

# This is DELETE request to delete a recipe based on the ID
@app.route('/api/1.0/recipes/<int:recipe_id>',methods=['DELETE'])
def delete_recipe(recipe_id):
	db.recipes.remove({'id' : recipe_id})
	return jsonify({'result':True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)	


if __name__ == '__main__':
    app.run(debug=True)
