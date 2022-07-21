import sys #ogout of the application
def main():
    login()
    
def login():
    username="ADMIN"
    password="12345"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("Welcome - Access Granted")
        menu()

def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
                      A: Hangman
                      B: Madlibbs
                      C: Ping-Pong
                      D: Tetris
                      E: Tic Tac Toe
                      F: Number Game 
                      G: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        import hang2
    elif choice == "B" or choice =="b":
        import window
    elif choice == "C" or choice =="c":
        import pong
    elif choice == "D" or choice =="d":
        import tetris
        tetris.main() 
    elif choice == "E" or choice =="e":
        import trial 
    elif choice == "F" or choice =="f":
        import NUMgame
    elif choice=="G" or choice=="g":
        sys.exit
    else:
        print("You must only select either A,B,C,D or E.")
        print("Please try again")
        menu() 
#the program is initiated, so to speak, here
main()
