import os
from flask import Flask, jsonify
import random


app = Flask(__name__)

person1 = {
	"id": 1,
	"first_name": "Billy Bob",
	"last_name": "Doe",
	"age": 73,
	"gender": "male",
	"lucky_numbers": [3,7,9,10]
	
}

person2 = {
	"id": 2,
	"first_name": "Wilbur",
	"last_name": "Doe",
	"age": 37,
	"gender": "undecided",
	"lucky_numbers": [2,4,6,8]
	
}

person3 = {
	"id": 3,
	"first_name": "Veronica",
	"last_name": "Doe",
	"age": 46,
	"gender": "female",
	"lucky_numbers": [3,5,7,8]
	
}

family = {
	"last_name": "Doe",
	"members": [person1, person2, person3]
}


  
@app.route('/', methods=['GET'])
def hello():
	lucky = []
	for m in family["members"]:
		lucky = lucky + m["lucky_numbers"]
  
	addAll = 0
	for l in lucky:
		addAll += l
	return jsonify(family)
	

  
@app.route('/member/<int:id>')
def get_member(id):
	if id > 0:
		for m in family["members"]:
			if m["id"] == id:
				lucky = []
				for x in range(4):
					list = random.randint(1,10)
				lucky.append(list)
				return jsonify({"status_code": 200, "data": m})
			else:
				response = jsonify({"error": 400, "message":"no member found" })
				response.status_code = 400
				return response
  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))