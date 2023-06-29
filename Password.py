import random
import sqlite3

# Connect to the database
conn = sqlite3.connect('/Users/sakhile/Documents/Projects/Pass/DB/passwords.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (platform text, username text, password text)''')

char = 'abcdefghijklmnopqrsABCDEFGHIJKLMNOPQRS!@#$%^&.(),'
number = int(input('The number of passwords to generate: '))
length = int(input('Length of password: '))

for i in range(number):
    platform = input('Enter the platform for the password: ')
    username = input('Enter the username for the password: ')
    password = ''
    for j in range(length):
        password += random.choice(char)

    # Insert the password into the database
    c.execute("INSERT INTO passwords (platform, username, password) VALUES (?, ?, ?)", (platform, username, password))
    conn.commit()

print('Passwords stored successfully.')

# Retrieve and display the most recently stored password
c.execute("SELECT * FROM passwords ORDER BY ROWID DESC LIMIT 1")
result = c.fetchone()

if result:
    platform, username, password = result
    print('Most recently stored password:')
    print('Platform:', platform)
    print('Username:', username)
    print('Password:', password)
else:
    print('No passwords found in the database.')

# Close the database connection
conn.close()
