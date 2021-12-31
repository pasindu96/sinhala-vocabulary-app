# Compare the answer with given word
def CompareWord(word, answer):
    if word == answer:
        # Store in DB -> userid, score, time taken
        return
    else:
        # Check the mismatching letter
        CheckLetters(word, answer)
        # Check the letter is mahaprana, sanghaka or moordhaja etc
        # Store in DB -> userid, score, time taken, weaken area
        return


characterList = []


def CheckLetters(word, answer):
    for i in range(0, len(answer)):
        if word[i] != answer[i]:
            characterList.append(word[i])


# Check the Type of the incorrect answer letter
def questionType(category):
    return {
        'ණ': 'Moordhaja',
        'ළ': 'Moordhaja',
        'ෂ': 'Moordhaja',

        'ඟ': 'Sanghaka',
        'ඦ': 'Sanghaka',
        'ඬ': 'Sanghaka',
        'ඳ': 'Sanghaka',
        'ඹ': 'Sanghaka',

        'ඵ': 'Mahaprana',
        'භ': 'Mahaprana',
        'ධ': 'Mahaprana',
        'ථ': 'Mahaprana',
        'ඨ': 'Mahaprana',
        'ඡ': 'Mahaprana',
        'ඪ': 'Mahaprana',
        'ඝ': 'Mahaprana',
        'ඛ': 'Mahaprana',
        'ඣ': 'Mahaprana'

    }[category]


# Check output
print(CompareWord("එළවළු", "එළවලු"))

for i in characterList:
    print(questionType(i))

print(characterList)


# Recommendations -> To be collected from interview

# Problem with the String SQL
# ======================================Start of DB Connection=============================================
# Database Connection -> MongoDB
def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb url in python to mongodb using pymongo ->If clustered, us Atlas
    CONNECTION_STRING = "mongodb://localhost:27017"
    # "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example
    return client['research_db']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()

collection_name = dbname["student_answers"]
item_1 = {
    "id": "ST001",
    "question": "අඹ",
    "answer": "අබ",
    "type": "MCQ",
    "result": "Incorrect",
    "weaken_letter_types": "සඤ්ඤක",
    "time_taken": "6000ms"
}

item_2 = {
    "id": "ST001",
    "question": "ඖෂධ",
    "answer": "ඖෂධ",
    "type": "Choose letters",
    "result": "Correct",
    "weaken_letter_types": "",
    "time_taken": "8500ms"
}
# collection_name.insert_many([item_1, item_2])

# ======================================End of DB Connection===============================================

# Response expected by the front end
sample_response = {
    "id": "ST001",
    "question": "ඖෂධ",
    "answer": "ඖෂධ",
    "type": "Image based MCQ",
    "time_taken": "5500ms"
}
