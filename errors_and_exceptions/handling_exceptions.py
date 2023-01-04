'''

It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whatever the operating system supports); 
note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.
'''

while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
