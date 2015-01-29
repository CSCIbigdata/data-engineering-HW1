Requests: 

#Post a new recipe
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"shit","description":"garbage","stars":"3"}' http://localhost:5000/api/1.0/recipes