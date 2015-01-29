Requests: 

#Get a recipe 
curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/1.0/recipes


#Post a new recipe
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"fish and chips","description":"garbage","stars":"3"}' http://localhost:5000/api/1.0/recipes

#Modify a recipe with a put:

curl -i -H "Content-Type: application/json" -X PUT -d '{"stars":10}' http://localhost:5000/api/1.0/recipes/1

#Delete a recipe with a DELETE
curl -i -H "Content-Type: application/json" -X DELETE -d '{"done":true}' http://localhost:5000/api/1.0/recipes/
