import sqlite3

def db_creator():
    with sqlite3.connect("data/database.db") as con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS yt_rel(
                id INTEGER PRIMARY KEY,
                videoId TEXT UNIQUE,
                title TEXT,
                thumbnail TEXT,
                relevant INTEGER
            )  
        """)
  


def insert_videos(videos):
    with sqlite3.connect("data/database.db") as con:
        cur = con.cursor()
        for video in videos:
            videoId = video.get("videoId")
            title = video.get("title")
            thumbnail = video.get("thumbnail")
            cur.execute("""
                INSERT OR IGNORE INTO yt_rel(videoId, title, thumbnail, relevant) VALUES(
                    ?, ?,?, ?
                    )     
                """, (videoId,title, thumbnail, None))
   


def insert_evaluation(evaluation):
    with sqlite3.connect("data/database.db") as  con:
        cur = con.cursor()
        cur.execute("""
            UPDATE yt_rel
            set relevant = ?
            WHERE videoId = ?
            """, (evaluation[1], evaluation[0])) 
        
 
    

def quick_inspection():
    with sqlite3.connect("data/database.db") as con:
        cur = con.cursor()
        res = cur.execute("Select COUNT(*) FROM yt_rel WHERE relevant IS NULL ")
        print(res.fetchone())
       

def load_next_video():
    with sqlite3.connect("data/database.db") as con:
        con.row_factory =  sqlite3.Row
        cur = con.cursor()
    
        cur.execute("""SELECT id, videoId, title, thumbnail 
        FROM yt_rel
        WHERE relevant IS NULL
        ORDER BY id ASC
        LIMIT 1
        """)    
        return cur.fetchone()
    
import sqlite3

def reset_database():
    with sqlite3.connect("data/database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE yt_rel SET relevant = NULL")
        con.commit()