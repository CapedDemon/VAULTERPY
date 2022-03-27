from cryptography.fernet import Fernet
import sqlite3


"""
The main functions are -
1. making a new password vault
2. generating key
3. inputing passwords in the vault and securing with any of your keys
4. retriving passwords using the key
"""

class passvault:
    
    def __init__(self):
        print("Initialised password vault .... ")

    def starters(self):
        print("1. Work with previous vault (P)\n2. Create new password vault (N)\n")
        mainChoice = input(":- ").upper()
        return mainChoice

    def menu(self):
        print("1. Generate a secret key (K)\n2. Insert password inside the vault and securing with key (I)\n3. Retrive passwords with decoding using the key (R)\n4. Load your secret key (L)\n5. Quit (Q)\n\n")
        menuChoice = input(": ")
        return menuChoice

    def p_vault(self):
        name = input("Enter the name of your vault (ex - vault.db, mongo.db) - ")
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()

        # making the table inside the database
        # just in case 😂😂
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS content (password TEXT, work TEXT)
            """)
        self.conn.commit()

    def c_vault(self):
        name = input("Enter the name of your vault - ")
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()

        # making the table inside the database
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS content (password TEXT, work TEXT)
            """)
        self.conn.commit()


    def l_vault(self):
        path = input("Enter the path of your secret key (Ex- secret.key) - ")
        self.secretKey = open(path, "rb").read()

    def i_vault(self):       
        entry = True
        while entry:

            # the key or the password is for what
            key = input("In which name you want to store the password - ")
            password = input("Give the password - ")
            encoded_message = password.encode()
            f = Fernet(self.secretKey)
            encrypted_message = f.encrypt(encoded_message)

            self.cur.execute("""
            INSERT INTO content (password, work) VALUES (?, ?)""", ((encrypted_message), key))
            self.conn.commit()

            # asking for more
            stop = input("Do you want to continue inserting password (y/n) - ")
            if stop=='n':
                entry = False

    def k_vault(self):
        key = Fernet.generate_key()
        path = input("Enter the filename to store your key (ex - secret.key) - ")
        with open(path, 'wb') as f:
            f.write(key)
        f.close()


    def r_vault(self):
        
        # seeing choice
        see = input("Do you want to see your passwords encrypted (e) or decoded (d) - ")

        recData = self.cur.execute("""
            SELECT * FROM content
            """)
        if see=='e':
            f = Fernet(self.secretKey)
            print("Your passwords in encrypted form are as follows - ")
            
            for x in recData:
                print(x[1] + " <-> " + str(x[0]))

        else:
            print("Your passwords in decrypted form are as follows - ")
            f = Fernet(self.secretKey)
            for x in recData:
                print(x[1] + ' -> ', end="")
                decrypted_message = f.decrypt(x[0])
                print(decrypted_message.decode())  