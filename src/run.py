from helpers import *
from cryptography.fernet import Fernet

password_vault = passvault()

mainChoice = password_vault.starters()
if mainChoice == 'P':
    password_vault.p_vault()
elif mainChoice == 'N':
    password_vault.c_vault()


choice = password_vault.menu().upper()
while choice != 'Q':
    if choice == 'K':
        password_vault.k_vault()

    elif choice == 'I':
        password_vault.i_vault()

    elif choice == 'R':
        password_vault.r_vault()

    elif choice == 'L':
        password_vault.l_vault()
    else:
        print("Provide correct choice\n")
    choice = password_vault.menu().upper()