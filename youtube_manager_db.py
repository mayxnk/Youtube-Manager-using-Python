import sqlite3

con = sqlite3.connect('youtube_manager.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL       
     )
''')


def list_all_videos():
    cursor.execute('''SELECT * FROM videos''')
    for row in cursor.fetchall():
        print(row)

def add_video():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name,time))
    con.commit()

def update_video(id):
    new_name = input("Enter video name: ")
    new_time = input("Enter video time: ")
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id = ?",(new_name,new_time,id))
    con.commit()


def delete_video(id):
    cursor.execute("DELETE FROM videos where id = ?",(id,))
    con.commit()


def main():
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all videos ")
        print("2. Add a youtube video ")
        print("3. Update the youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter the choice: ")

        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                list_all_videos()
                id = input("Enter video index to update: ")
                update_video(id)
            case  "4":
                list_all_videos()
                id = input("Enter video index to delete: ")
                delete_video(id)
            case "5":
                break
            case _:
                print("Invalid Choice !")
    con.close()


if __name__ == "__main__":
    main()