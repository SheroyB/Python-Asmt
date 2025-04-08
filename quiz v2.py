#Create a quiz
from easygui import*

score = 0
name = str()
year = int()

qa = {'New Zealand' : 'wellington', 'Australia' : 'canberra', 'India' : 'new delhi', 'China' : 'beijing'}

play = enterbox('Do you wish to play the quiz? (yes or no) : ')

if play == 'yes':
    while True:
        try:
            name = enterbox('Enter your name: ')
            if name == '':
                msgbox('You must provide a name')
            else:
                break
        except ValueError:
            msgbox('Please enter a valid name')
    while True:
        try:
            year = int(enterbox('Enter your year level : '))
            break
        except ValueError:
            msgbox('Please enter an integer')
    if year >=9:
        for k, v in qa.items():
            user_ans = enterbox(f'What is the capital of {k} : ')
            if user_ans.lower() == v.lower():
                msgbox('correct')
                score+=1
            else:
                msgbox('incorrect')
            total_score = score
            percent = (score/len(qa))*100
        msgbox(f'Your final score is {total_score} points')
        msgbox(f'You got {percent}%')

    else:
        msgbox(f'Unfortunately {name}, you must be year 9 or above to play')
else:
    msgbox('Understood, feel free to come back later')
