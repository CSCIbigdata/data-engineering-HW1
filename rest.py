#!flask/bin/python
from flask import Flask,jsonify,request

app = Flask(__name__)

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


@app.route('/api/1.0/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'recipes':recipes})

@app.route('/api/1.0/recipes/<int:recipe_id>',methods=['GET'])
def get_recipe(recipe_id):
	recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
	return jsonify({'recipe':recipe[0]}

@app.route('/api/1.0/recipes',methods=['POST'])
def create_recipe():
	if not request.json or not title in request.json:
		return "BAD POST"

	recipe = {
		'id': recipes[-1]['id'] + 1,
		'title': request.json['title'],
		'description' : request.json.get('description'),
		'stars' : request.json.get('stars')
	}

	recipes.append(recipe)
	return jsonify({'recipe': recipe}),201


if __name__ == '__main__':
    app.run(debug=True)