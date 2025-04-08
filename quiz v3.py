#Create a quiz
from easygui import*
import pandas as pd
import matplotlib.pyplot as plt

score = 0
name = str()
year = int()

#Dictionary containing countries and their capitals
qa = {'New Zealand' : 'wellington', 'Australia' : 'canberra', 'India' : 'new delhi', 'China' : 'beijing'}

#Ask the user if they want to play
play = enterbox('Do you wish to play the quiz? (yes or no) : ')

if play == 'yes':
    #Get the user's name
    while True:
        try:
            name = enterbox('Enter your name: ')
            if name == '': #If user leaves name blank
                msgbox('You must provide a name')
            elif name.isdigit(): #If user enters numbers as their name
                msgbox('Please enter a valid name')
            else:
                break
        except ValueError:
            msgbox('Please enter a valid name')

    #Get the user's year level
    while True:
        try:
            year = int(enterbox('Enter your year level : '))
            break
        except ValueError:
            msgbox('Please enter an integer')

    #Check if user is eligible (Year 9 or above)
    if year >=9:
        for k, v in qa.items():
            #Ask the capital of each country
            user_ans = enterbox(f'What is the capital of {k} : ')
            if user_ans.lower() == v.lower():
                msgbox('correct \n +1 point')
                score+=1
            else:
                msgbox('incorrect')
        
        #Calculate final score and percentage
        total_score = score
        percent = (score/len(qa))*100
        msgbox(f'Your final score is {total_score} points')
        msgbox(f'You got {percent}%')

        #Save score to file
        with open("mock_scores.txt","a") as mock_scores_file:
                mock_scores_file.write(f"\n{name},{total_score}")
        
        #Read the file and create a bar chart
        df = pd.read_csv('mock_scores.txt')
        colors = ["red", "green", "yellow", "purple", "orange"]
        df.plot(x = 'name', y = 'score', kind = 'bar', color = colors)
        plt.show()

    else:
        #If user is not in Year 9 or above
        msgbox(f'Unfortunately {name}, you must be year 9 or above to play')
else:
    #If user doesn't want to play
    msgbox('Understood, feel free to come back later')
