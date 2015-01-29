Requests: 

#Post a new recipe
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"fish and chips","description":"garbage","stars":"3"}' http://localhost:5000/api/1.0/recipes

#Modify a recipe with a put:

curl -i -H "Content-Type: application/json" -X PUT -d '{"stars":10}' http://127.0.0.1:5000/api/1.0/recipes/1