#!flask/bin/python
from flask import Flask,jsonify,request

app = Flask(__name__)

#Just to initialize our sample database
recipes = [
	
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

#this GET returns all of the recipes
@app.route('/api/1.0/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'recipes':recipes})

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


if __name__ == '__main__':
    app.run(debug=True)