import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(__file__), 'screener.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            filename TEXT,
            text TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score REAL,
            justification TEXT,
            resume_text TEXT,
            job_description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_resume(name, filename, text):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('INSERT INTO resumes (name, filename, text) VALUES (?, ?, ?)', (name, filename, text))
    conn.commit()
    rid = cur.lastrowid
    conn.close()
    return rid

def get_resume_text(resume_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT text FROM resumes WHERE id=?', (resume_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

def save_result(score, justification, resume_text, job_description):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('INSERT INTO results (score, justification, resume_text, job_description) VALUES (?, ?, ?, ?)',
                (score, justification, resume_text, job_description))
    conn.commit()
    rid = cur.lastrowid
    conn.close()
    return rid
