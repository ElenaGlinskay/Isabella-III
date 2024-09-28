class Document:
    def __init__(self, db):
        self.collection = db['documentos']  # Nombre de la colección en MongoDB

    def create_document(self, data):
        return self.collection.insert_one(data)

    def find_all_documents(self):
        return self.collection.find()

    def find_document_by_id(self, doc_id):
        return self.collection.find_one({"_id": doc_id})

    def update_document(self, doc_id, data):
        return self.collection.update_one({"_id": doc_id}, {"$set": data})

    def delete_document(self, doc_id):
        return self.collection.delete_one({"_id": doc_id})
