for i in range(0,3):

    print('Enter 1 for hangman\n')

    print('Enter 2 for Madlibs \n')

    print('Enter 3 for Ping Pong\n')

    choice = int(input('Enter your choice:'))

    if (choice == 1):
        import hang2
    elif(choice ==2):
        import window
    elif(choice ==3):
        import pong
    else:
        print('Invalid choice')