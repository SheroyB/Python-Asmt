#Create a quiz

score = 0

qa = {'Nz' : 'WGTN', 'Aus' : 'Can', 'Ind' : 'NDL', 'China' : 'Bjing'}

year = int(input('Enter your year level : '))

if year >=9:
    for k, v in qa.items():
        user_ans = input(f'What is the capital of {k} : ')
        if user_ans == v:
            print('correct')
            score+=1
        else:
            print('incorrect')
        total_score = score
        percent = (score/4)*100
    print(f'Your final score is {total_score}')
    print(f'You got {percent}%')

else:
    print('Unfortunately, you must be year 9 or above to play')
