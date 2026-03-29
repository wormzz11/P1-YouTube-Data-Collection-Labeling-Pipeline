import sqlite3


videos = [{'title': 'A bad day to use python', 'videoId': 'mx3g7XoPVNQ'}, {'title': '25 Tips &amp; Tricks in Python', 'videoId': 's_oXtdhqXR8'}, {'title': 'Python Full Course for Beginners', 'videoId': 'K5KVEU3aaeQ'}, {'title': 'you need to learn Python RIGHT NOW!! // EP 1', 'videoId': 'mRMmlo_Uqcs'}, {'title': 'Python in 100 Seconds', 'videoId': 'x7X9w_GIm1s'}]
evaluated = [
    ("mx3g7XoPVNQ", 1),
    ("s_oXtdhqXR8", 0),
    ("K5KVEU3aaeQ", 1),
    ("mRMmlo_Uqcs", 0),
    ("x7X9w_GIm1s", 1)
]
def db_creator():
    con = sqlite3.connect("data/database.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS yt_rel(
            id INTEGER PRIMARY KEY,
            videoId TEXT UNIQUE,
            title TEXT,
            relevant INTEGER
        )  
    """)
    con.close()



def insert_videos(videos):
    con = sqlite3.connect("data/database.db")
    cur = con.cursor()
    for video in videos:
        videoId = video.get("videoId")
        title = video.get("title")

        cur.execute("""
            INSERT OR IGNORE INTO yt_rel(videoId, title, relevant) VALUES(
                ?, ?,?
                )     
            """, (videoId,title, None))
    con.commit()
    con.close()

    

def insert_evaluation(evaluated_videos):
    con = sqlite3.connect("data/database.db")
    cur = con.cursor()
    for evaluation in evaluated_videos:
        cur.execute("""
                    UPDATE yt_rel
                    set relevant = ?
                    WHERE videoId = ?
                    """, (evaluation[1], evaluation[0])) 
        
    con.commit()
    res = cur.execute("Select * FROM yt_rel WHERE relevant = 1")
    print(res.fetchall())
    con.close()
db_creator()
insert_videos(videos)
insert_evaluation(evaluated)
    