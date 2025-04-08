#Create a quiz using easygui
from easygui import*

score = 0
name = str()
year = int()

#Dictionary of countries and their capitals
qa = {'New Zealand' : 'wellington', 'Australia' : 'canberra', 'India' : 'new delhi', 'China' : 'beijing'}

#Ask user if they want to play the quiz
play = enterbox('Do you wish to play the quiz? (yes or no) : ')

if play == 'yes':
    #Ask for user's name
    while True:
        try:
            name = enterbox('Enter your name: ')
            if name == '':
                msgbox('You must provide a name')
            else:
                break
        except ValueError:
            msgbox('Please enter a valid name')

    #Ask for user's year level
    while True:
        try:
            year = int(enterbox('Enter your year level : '))
            break
        except ValueError:
            msgbox('Please enter an integer')

    #Check if user is eligible to play
    if year >=9:
        for k, v in qa.items():
            #Ask the capital of each country
            user_ans = enterbox(f'What is the capital of {k} : ')
            if user_ans.lower() == v.lower():
                msgbox('correct')     #Correct answer message
                score+=1
            else:
                msgbox('incorrect')   #Incorrect answer message

            #Update total score and calculate percentage after each question
            total_score = score
            percent = (score/len(qa))*100

        #Show final score and percentage
        msgbox(f'Your final score is {total_score} points')
        msgbox(f'You got {percent}%')

    else:
        #If year level is too low to play
        msgbox(f'Unfortunately {name}, you must be year 9 or above to play')
else:
    #User chose not to play
    msgbox('Understood, feel free to come back later')
