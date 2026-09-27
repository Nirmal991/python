from _sqlite3 import connect

filename = 'user.sqlite'

class UserDatabaseManagment:
    def __init__(self, db_path):
        self.db_path = db_path

        sql_cmd = '''CREATE TABLE IF NOT EXISTS USERS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT UNIQUE NOT NULL,
        ADDRESS TEXT,
        MOBILE TEXT,
        EMAIL TEXT)'''

        with connect(db_path) as conn:
            curr = conn.cursor()
            curr.execute(sql_cmd)

        print(f'Table EMPS created successfully in the sqlite file `{filename}`')

    def find_user(self,username):
        sql_cmd = '''SELECT ID, USERNAME, ADDRESS, MOBILE, EMAIL 
        FROM USERS
        WHERE USERNAME = ?'''

        with connect(self.db_path) as conn:
            curr = conn.cursor()
            curr.execute(sql_cmd, (username,))
            row = curr.fetchone()

            if row:
                return {
                    "id": row[0],
                    "username": row[1],
                    "address": row[2],
                    "mobile": row[3],
                    "email": row[4]
                }
            return None

    def add_update_user(self, username, address, mobile, email):
        user = self.find_user(username)

        if user:
            sql_cmd = '''UPDATE USERS
            SET ADDRESS = ?, MOBILE = ?, EMAIL = ?
            WHERE USERNAME = ?'''

            with connect(self.db_path) as conn:
                curr = conn.cursor()
                curr.execute(sql_cmd, (address, mobile, email))
            return "UPDATED"
        else:
            sql_cmd = '''INSERT INTO USERS(USERNAME, ADDRESS, MOBILE, EMAIL)
            VALUES (?,?,?,?)'''

            with connect(self.db_path) as conn:
                curr = conn.cursor()
                curr.execute(sql_cmd, (username, address, mobile, email))
            return "INSERTED"

    def list_all_user(self):
        sql_cmd='''SELECT ID, USERNAME ADDRESS, MOBILE, EMAIL
        FROM USERS
        ORDER BY USERNAME'''

        with connect(self.db_path) as conn:
            curr = conn.cursor()
            curr.execute(sql_cmd)

            rows = curr.fetchall()

            users = []

            for row in rows:
                users.append({
                    "id": row[0],
                    "username": row[1],
                    "address": row[2],
                    "mobile": row[3],
                    "email": row[4]
                })


                return users