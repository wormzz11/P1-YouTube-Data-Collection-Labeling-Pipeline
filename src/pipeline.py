from  src.fetch import  title_fetcher
from  src.processor import processing
from src.database import db_creator, insert_videos, quick_inspection
def run_pipeline():
    db_creator()
    data = title_fetcher("Python", 20)
    processed_data = processing(data)
    insert_videos(processed_data)
    quick_inspection()
if  __name__ == "__main__":
    run_pipeline()




