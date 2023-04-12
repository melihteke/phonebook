from pymongo import MongoClient
from bson.objectid import ObjectId


class Phonebook:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client.get_database(db_name)
        self.collection = self.db.get_collection(collection_name)

    def add_record(self, record):
        self.collection.insert_one(record)

    def remove_record(self, record_id):
        self.collection.delete_one({'_id': ObjectId(record_id)})

    def update_record(self, record_id, updates):
        self.collection.update_one({'_id': ObjectId(record_id)}, {'$set': updates})

    def view_all_records(self):
        return [record for record in self.collection.find()]

    def view_specific_record(self, filters):
        return [record for record in self.collection.find(filters)]

# Example usage:
phonebook = Phonebook(
    uri="mongodb+srv://dbausr_melih:XXXXXXXXXX@cluster0.yblsda7fog.mongodb.net/test?retryWrites=true&w=majority",
    db_name="test",
    collection_name="phonebook"
)

# Adding a new record
new_record = {'name': 'John Smith', 'phone_number': '555-1234'}
phonebook.add_record(new_record)

# Updating an existing record
record_id_to_update = 'some_id'
updates = {'name': 'Jane Doe', 'phone_number': '555-5678'}
phonebook.update_record(record_id_to_update, updates)

# Removing a record
record_id_to_remove = 'some_id'
phonebook.remove_record(record_id_to_remove)

# Viewing all records
all_records = phonebook.view_all_records()

# Viewing specific records
filters = {'name': 'John Smith'}
specific_records = phonebook.view_specific_record(filters)