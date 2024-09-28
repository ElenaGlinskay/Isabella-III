class Section:
    def __init__(self, db):
        self.collection = db['secciones']

    def create_section(self, data):
        return self.collection.insert_one(data)

    def find_all_sections(self):
        return self.collection.find()

    def find_section_by_id(self, section_id):
        return self.collection.find_one({"_id": section_id})

    def update_section(self, section_id, data):
        return self.collection.update_one({"_id": section_id}, {"$set": data})

    def delete_section(self, section_id):
        return self.collection.delete_one({"_id": section_id})
