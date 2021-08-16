import sqlite3


CREATE_NOTES_TABLE = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY, 
    title text,
    dateCreate timestamp, 
    dateUpdate timestamp, 
    body text
);
"""

INSERT_NOTE         = "INSERT INTO notes (title, dateCreate, dateUpdate, body) VALUES (?,?,?,?)"

GET_ALL_NOTES       = "SELECT * FROM notes"

GET_ALL_NOTESBYTEXT = """SELECT * FROM notes 
WHERE 
title LIKE ? or body LIKE ? 
or strftime('%d', dateCreate) LIKE ? 
or strftime('%d', dateCreate) LIKE ?
or strftime('%m', dateCreate) LIKE ? 
or strftime('%m', dateCreate) LIKE ?
or strftime('%Y', dateCreate) LIKE ? 
or strftime('%Y', dateCreate) LIKE ?"""

GET_ALL_NOTESBYID   = "SELECT * FROM notes WHERE id = ?"

DELETE_NOTES        = "DELETE FROM notes WHERE id = ?"

UPDATE_NOTE         = "UPDATE notes SET title = ?, body = ?, dateUpdate = ? WHERE id = ?"


def connect():
    return sqlite3.connect("notes.db")

def create_tables(connection):
    with connection:
         connection.execute(CREATE_NOTES_TABLE)

def add_note(connection, title, dateCreate, dateUpdate, body):
    with connection:
        connection.execute(INSERT_NOTE, (title, dateCreate, dateUpdate, body))

def get_all_notes(connection):
    with connection:
        return connection.execute(GET_ALL_NOTES).fetchall()

def get_all_notesByText(connection, text1, text2, text3, text4, text5, text6, text7, text8):
    with connection:
        return connection.execute(GET_ALL_NOTESBYTEXT, (text1, text2, text3, text4, text5, text6, text7, text8)).fetchall()

def get_all_notesById(connection, id):
    with connection:
        return connection.execute(GET_ALL_NOTESBYID, (id,)).fetchone()        

def delete_notes(connection, id):
    with connection:
        connection.execute(DELETE_NOTES, (id,))

def update_note(connection, title, body, dateUpdate, id):
    with connection:
        return connection.execute(UPDATE_NOTE, (title, body, dateUpdate,id))

