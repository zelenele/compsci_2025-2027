import csv

data = []

with open(".github/Group A/Scienceproject.csv", "r", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

print(data)

survey_data = [
    {
        "category": "Perception of Environmental Friendliness",
        "data": {
            "Probably yes": 39.5,
            "Probably no": 25.9,
            "I don't know": 18.5,
            "Definitely no": 8.6,
            "Definitely yes": None
        }
    },
    {
        "category": "Meat Consumption Frequency",
        "data": {
            "4–6 times a week": 38.3,
            "2–3 times a week": 27.2,
            "Every day": 18.5,
            "Once a week or less": None
        }
    },
    {
        "category": "Most Consumed Meat Type",
        "data": {
            "Poultry": 79.0,
            "Beef": 40.7,
            "Fish/Seafood": 32.1,
            "Pork": 22.2,
            "Do not eat meat": 6.2
        }
    },
    {
        "category": "Fruit and Vegetable Consumption",
        "data": {
            "Every day": 71.6,
            "4–6 times a week": 14.8,
            "Rarely": None
        }
    },
    {
        "category": "Dairy Consumption",
        "data": {
            "Every day": 49.4,
            "4–6 times a week": 33.3,
            "Rarely or never": None
        }
    },
    {
        "category": "Food Waste Frequency",
        "data": {
            "Rarely": 40.7,
            "Sometimes": 32.1,
            "Never or almost never": 17.3,
            "Often": 9.9
        }
    },
    {
        "category": "Type of Diet",
        "data": {
            "Traditional/mixed": 85.2,
            "Vegetarian": 9.9,
            "Vegan/Flexitarian/Other": None
        }
    }
]