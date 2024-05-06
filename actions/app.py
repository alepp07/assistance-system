from flask import Flask, jsonify

app = Flask(__name__)

# Sample data structure for offers
offers_data = [
    {"id": 1, "name": "Erasmus Information", "description": "Information about the Erasmus Program"},
    {"id": 2, "name": "Language Support", "description": "Language courses and resources for language support"},
    {"id": 3, "name": "Network Opportunities", "description": "Opportunities for networking with Erasmus alumni and participants"},
    {"id": 4, "name": "Events", "description": "Information about Erasmus events"},
    {"id": 5, "name": "Requirement for Application", "description": "Requirements and procedures for applying to Erasmus"},
    {"id": 6, "name": "Academic Assist Guidance", "description": "Academic guidance and support for Erasmus participants"}
]

# List of countries with funding rates
countries_data = [
    {"name": "Denmark", "rate": 750},
    {"name": "Finland", "rate": 750},
    {"name": "Ireland", "rate": 750},
    {"name": "Iceland", "rate": 750},
    {"name": "Liechtenstein", "rate": 750},
    {"name": "Luxembourg", "rate": 750},
    {"name": "Norway", "rate": 750},
    {"name": "Sweden", "rate": 750},
    {"name": "Austria", "rate": 690},
    {"name": "Belgium", "rate": 690},
    {"name": "Cyprus", "rate": 690},
    {"name": "France", "rate": 690},
    {"name": "Greece", "rate": 690},
    {"name": "Italy", "rate": 690},
    {"name": "Malta", "rate": 690},
    {"name": "Netherlands", "rate": 690},
    {"name": "Portugal", "rate": 690},
    {"name": "Spain", "rate": 690},
    {"name": "Bulgaria", "rate": 630},
    {"name": "Croatia", "rate": 630},
    {"name": "Czech Republic", "rate": 630},
    {"name": "Estonia", "rate": 630},
    {"name": "Hungary", "rate": 630},
    {"name": "Latvia", "rate": 630},
    {"name": "Lithuania", "rate": 630},
    {"name": "North Macedonia", "rate": 630},
    {"name": "Poland", "rate": 630},
    {"name": "Romania", "rate": 630},
    {"name": "Serbia", "rate": 630},
    {"name": "Slovakia", "rate": 630},
    {"name": "Slovenia", "rate": 630},
    {"name": "Turkey", "rate": 630}
]

# GET request to get list of Countries with fund rates
@app.route('/api/funding', methods=['GET'])
def get_funding():
    return jsonify(countries_data)

# GET request to get info of the offer list
@app.route('/api/offers', methods=['GET'])
def get_offers():
    return jsonify(offers_data)

# POST request to add a new offer
@app.route('/api/offers', methods=['POST'])
def add_offer():
    new_offer = {
        "id": max(offers_data, key=lambda x: x['id'])['id'] + 1,
        "name": "New Offer",
        "description": "Description for the new offer"
    }
    offers_data.append(new_offer)
    return jsonify(new_offer), 201

if __name__ == '__main__':
    app.run(debug=True)


#/api/offers for list of offers
#/api/funding for list of funding rates of countries