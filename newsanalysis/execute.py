import os
os.system("python build/start_crawl.py")
print("sentiment-ner process")
os.system("python build/final_model_1.py")
print("done")
print("extracting json")
os.system("python build/extract_json.py")