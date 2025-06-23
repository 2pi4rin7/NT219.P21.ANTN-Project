from pymongo import MongoClient

# Kết nối đến MongoDB server (mặc định localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# Chọn database và collection
db = client["healthcare"]
collection = db["users"]

# Lấy toàn bộ dữ liệu
all_data = collection.find()

# Duyệt và in từng bản ghi
for doc in all_data:
    print(doc)
