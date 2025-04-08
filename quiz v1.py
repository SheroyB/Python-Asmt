#Create a quiz

score = 0 #Initialize score to zero

#Dictionary of country abbreviations and their capitals
qa = {'Nz' : 'Wellington', 'Aus' : 'Canberra', 'Ind' : 'New Delhi', 'China' : 'Beijing'}

#Ask user for their year level
year = int(input('Enter your year level : '))

#Only allow users Year 9 or above to play
if year >=9:
    for k, v in qa.items():
        #Ask the user the capital of each country
        user_ans = input(f'What is the capital of {k} : ')
        if user_ans == v:
            print('correct') #Correct answer
            score+=1
        else:
            print('incorrect') #Incorrect answer

        #Update total score and percentage after each question
        total_score = score
        percent = (score/4)*100

    #Display final results
    print(f'Your final score is {total_score}')
    print(f'You got {percent}%')

else:
    #If year level is below 9
    print('Unfortunately, you must be year 9 or above to play')
