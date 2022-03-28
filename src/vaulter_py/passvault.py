from cryptography.fernet import Fernet
import sqlite3


"""
The main functions are -
1. making a new password vault
2. generating key
3. inputing passwords in the vault and securing with any of your keys
4. retriving passwords using the key
"""

class Passvault:
    
    def __init__(self):
        self.secretKey = None
        print("Initialised password vault .... ")
        print('''
                    .---.                 |"""""|
                    '   '--------"""    ." -----".
                    '    --------[()]   |         |
                    '---'         ||     ---------
            
        ''')
        print("\n\n")

    def starters(self):
        print("1. Work with previous vault (P)\n2. Create new password vault (N)")
        mainChoice = input(":- ").upper()
        return mainChoice

    def menu(self):
        print("1. Generate a secret key (K)\n2. Insert password inside the vault and securing with key (I)\n3. Retrive passwords with decoding using the key (R)\n4. Load your secret key (L)\n5. Help (H)\n6. Quit (Q)\n\n")
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
        if (self.secretKey == None):
            entry = False
            print("First, load your key to continue\n")
        while (entry==True):

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
        
        if (self.secretKey != None):

            # seeing choice
            see = input("Do you want to see your passwords encrypted (e) or decoded (d) - ")

            recData = self.cur.execute("""
                SELECT * FROM content
                """)
            i=1;
            if see=='e':
                f = Fernet(self.secretKey)
                print("\nYour passwords in encrypted form are as follows - ")
                
                
                for x in recData:
                    print(str(i) + ". " + x[1] + " -> " + str(x[0]))
                    i=i+1

                print("\n\n")

            else:
                print("\nYour passwords in decrypted form are as follows - ")
                f = Fernet(self.secretKey)
                for x in recData:
                    print(str(i) + ". " + x[1] + ' -> ', end="")
                    decrypted_message = f.decrypt(x[0])
                    print(decrypted_message.decode())
                    i=i+1
                print("\n\n")
        
        else:
            print("First, load your secret key \n")

        
    def h_vault(self):
        print("""
                            Working with VAULTERPY is pretty easy.

                    1. When starting the vaulterpy, you need to select two things
                        - P -> To work with already created vaults, or database
                        - N -> To create a new vault/database
                        You need to first click any one of these, else you will be not able to do others.
                    
                    2. K -> This will generate a secret key, in the file .key extension which
                        will be specified by you.

                    3. L -> Loading the key is very important. From, initialisation, the default key is None.
                        So, to insert passwords and encrypt them secret key need to be loaded.
                        As well as for retriving passwords.

                    4. I -> This will allow you to insert passwords in the vault.
                        You need to give the password and the key of password, 
                        means for which thing you are keeping the password.

                    5. H -> This will show you the help guide, in which you are in now.

                    6. Q -> This will Quit the program.
                    
    """)
    print ("\n")


def main():
    pv = Passvault()
    mainChoice = pv.starters()

    if mainChoice == 'P':
        pv.p_vault()

    elif mainChoice == 'N':
        pv.c_vault()
            

    print("\n")
    choice = pv.menu().upper()
    while choice != 'Q':
        if choice == 'K':
            pv.k_vault()

        elif choice == 'I':
            pv.i_vault()

        elif choice == 'R':
            pv.r_vault()

        elif choice == 'L':
            pv.l_vault()

        elif choice == 'H':
            pv.h_vault()

        else:
            print("Provide correct choice\n")
        choice = pv.menu().upper()