from datetime import date
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


def writeToDatabase(result):
    # Store to database
    dbname = get_database()
    collection_name = dbname["student_answers"]
    collection_item = {
        "student_id": result.student_id,
        "question_type": result.question_type,
        "question": result.question,
        "given_answer": result.answer,
        "letter_count": result.letter_count,
        "result": result.result,
        "similarity": result.similarity,
        "weaken_letter_types": result.weaken_letter_types,
        "time_taken": result.time_taken,
        "time_stamp": date.today().strftime("%d/%m/%Y")
    }
    print(collection_item)
    collection_name.insert(collection_item)


