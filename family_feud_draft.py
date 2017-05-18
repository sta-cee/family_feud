
questions_list = [
    {
        'text' : 'What are the top 6 most successful food chains in the us?',

        'answers' : {
            'mcdonalds' : { 'dollars' : '35.4 billion', 'points' : 83},
            'starbucks' : { 'dollars' : '12.7 billion', 'points' : 30},
            'subway' : { 'dollars' : '11.9 billion', 'points' : 28},
            'burger king' : { 'dollars' : '8.6 billion', 'points' : 20},
            'wendys' : { 'dollars' : '8.5 billion', 'points' : 20},
            'taco bell' : { 'dollars' : '8.2 billion', 'points' : 19},
        },
        'source' : 'businessinsider.com -- Ranked by system wide sales in the United States in 2014.'
    },
    {
        'text' : 'Name the top 6 most popular websites (by unique visitors):',

        'answers' : {
            'google' : { 'unique visitors' : '155,542,763', 'points' : 48},
            'youtube' : { 'unique visitors' : '112,488,595', 'points' : 35},
            'amazon' : { 'unique visitors' : '100,698,302', 'points' : 30},
            'facebook' : { 'unique visitors' : '99,399,545', 'points' : 31},
            'yahoo' : { 'unique visitors' : '91,533,902', 'points' : 28},
            'twitter' : { 'unique visitors' : '90,674,864', 'points' : 28},
        },
        'source' : 'alexa.com -- ranked by '
    },
    {
        'text' : 'What are the top 6 largest california cities (by population)?',

        'answers' : {
            'los angeles' : { 'population' : '4,094,764', 'points' : 98},
            'san diego' : { 'population' : '1,376,173', 'points' : 33},
            'san jose' : { 'population' : '1,023,083', 'points' : 25},
            'san francisco' : { 'population' : '856,095', 'points' : 20},
            'fresno' : { 'population' : '502,303', 'points' : 12},
            'long beach' : { 'population' : '494,709', 'points' : 12},
        },
        'source' : 'seecalifornia.com'
    },
    {
        'text' : 'What are the top six us cities with the highest rent?',

        'answers' : {
            'san francisco' : { 'rent' : '$4,780', 'points' : 46},
            'new york' : { 'rent' : '$4,450', 'points' : 43},
            'jersey city' : { 'rent' : '$3,080', 'points' : 30},
            'washington dc' : { 'rent' : '$2,990', 'points' : 29},
            'boston' : { 'rent' : '$2,900', 'points' : 28},
            'san jose' : { 'rent' : '$2,640', 'points' : 24},

        },
        'source' : 'apartmentlist.com'
    },
    {
        'text' : 'What are the top four most popular pets in the us?',

        'answers' : {
            'fish' : { 'owned' : '139.3 million', 'points' : 81},
            'cat' : { 'owned' : '94.2 million', 'points' : 55},
            'dog' : { 'owned' : '89.7 million', 'points' : 52},
            'bird' : { 'owned' : '20.3 million', 'points' : 12},

        },
        'source' : 'americanpetproducts.org'
    },

]

user_points = 0
user_correct_answers = 0
round_counter = 0
user_total_guesses = 0

def welcome():
    print '\nWelcome to Family Feud! I\'m going to ask you a series of questions that have multiple answers. You get points for every answer that you guess correctly.'
    opt_in_reply = raw_input('\nDo you want to play Family Feud? Please enter yes or no: ').lower()
    if opt_in_reply in ('y', 'yes'):
        print '\nAwesome, let\'s play!\n'
        play_game()
    else:
        print '\nOkay, have a nice day -- bye!\n'
        return

def play_game():
    global questions_list, user_points, user_correct_answers, round_counter, user_total_guesses

    for question_dict in questions_list:
        round_counter += 1
        print '---'
        print '\nRound #%i: You have %i guesses.\n'% (round_counter, len(question_dict['answers']))
        print question_dict['text']
        print '\n---\n'
        for guess_count in range(len(question_dict['answers'])):
            user_total_guesses += 1
            print 'Guess #%i: ' % (guess_count + 1)
            user_answer = (raw_input('>>> ')).lower()
            if user_answer in question_dict['answers']:
                print 'yes'
                user_correct_answers += 1
                print user_correct_answers
                user_points += question_dict['answers'][user_answer]['points']
                print user_points
            else:
                print 'no'
        # for x in range(len(questions_list)):
        #     for correct_answers in questions_list[x]['answers']:
        #         print correct_answers.title
        if round_counter == len(questions_list):
            end_game()

def end_game():
    global questions_list, user_points, user_correct_answers, round_counter, user_total_guesses
    print 'You completed %i rounds, correctly guessed %i answers out of %i possible correct answers, and earned %i points.' % (round_counter, user_correct_answers, user_total_guesses, user_points)



welcome()
