from flask import Flask, jsonify, request

app = Flask(__name__)
accounts = [{'name' : 'billy', 'balance' : 450}, {'name' : 'kelly', 'balance' : 250}]

@app.route("/accounts", methods = ["GET"])
def getAccounts():
	return  jsonify(accounts)

@app.route("/accounts/<id>", methods = ["GET"])
def getAccount(id):
	id = int(id) - 1
	return  jsonify(accounts[id])

@app.route("/accounts", methods = ["POST"])
def postAccounts():
	name = request.json['name']
	balance = request.json['balance']
	data = {'name' : name, 'balance' : balance}
	accounts.append(data)
	return  jsonify(data)
