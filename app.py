from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Подключение к локальному блокчейну (например, Hardhat или Ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
if not w3.isConnected():
    print("Failed to connect to blockchain")

# Данные контракта
contract_address = Web3.to_checksum_address("0xYourContractAddressHere")  # Замените адрес
contract_abi = [  # ABI из контракта DiplomaRegistry
    # Вставьте здесь ABI контракта DiplomaRegistry
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Укажите аккаунт для транзакций
account = w3.eth.accounts[0]

# API для добавления диплома
@app.route('/addDiploma', methods=['POST'])
def add_diploma():
    try:
        data = request.json
        diploma_id = data['diplomaId']
        owner_name = data['ownerName']
        university = data['university']
        degree = data['degree']
        date = data['date']

        tx_hash = contract.functions.addDiploma(
            diploma_id, owner_name, university, degree, date
        ).transact({'from': account})
        w3.eth.wait_for_transaction_receipt(tx_hash)

        return jsonify({"message": "Diploma added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API для получения диплома
@app.route('/getDiploma/<diplomaId>', methods=['GET'])
def get_diploma(diplomaId):
    try:
        diploma = contract.functions.getDiploma(diplomaId).call()
        return jsonify({
            "ownerName": diploma[0],
            "university": diploma[1],
            "degree": diploma[2],
            "date": diploma[3]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# API для авторизации университета
@app.route('/authorizeUniversity', methods=['POST'])
def authorize_university():
    try:
        data = request.json
        university_address = Web3.to_checksum_address(data['universityAddress'])

        tx_hash = contract.functions.authorizeUniversity(university_address).transact({'from': account})
        w3.eth.wait_for_transaction_receipt(tx_hash)

        return jsonify({"message": "University authorized successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
