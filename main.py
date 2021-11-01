from random import choice
from typing import List, NamedTuple, Tuple


class Question1(NamedTuple): #cat 1 of questions
    question: str
    answers: List[str]
    correct: str
    amount: int


questions1 = [
    Question1(
        "QUESTION: What is the biggest currency in Europe?",
        ["A) Crown", "B) Peso", "C) Dolar", "D) Euro"],
        "D", 25
    ),
    Question1(
        "QUESTION: What is the biggest mountain in the world?",
        ["A) Everest", "B) Montblanc", "C) Popocatepepl", "D) K2"],
        "A", 25
    ),
    Question1(
        "QUESTION: What is the capital of Brasil?",
        ["A) Rio de Janeiro", "B) Brasilia", "C) Sao Paolo", "D) Recife"],
        "B", 25
    ),
    Question1(
        "QUESTION: Who discovered America?",
        ["A) Cristopher Columbus", "B) The Vikings", "C) Sir Ranulph Fiennes", "D) Darwin"],
        "A", 25
    ),
    Question1(
        "QUESTION: Who won the last FIFA World Cup?",
        ["A) Croatia", "B) France", "C) Argentina", "D) Germany"],
        "B", 25
    ),
]
class Question2(NamedTuple): #cat 2 of questions
    question: str
    answers: List[str]
    correct: str
    amount: int

questions2 = [
    Question2(
        "QUESTION: How many colors are in the Rainbow?",
        ["A) Two", "B) Four", "C) Three", "D) Seven"],
        "D", 75
    ),
    Question2(
        "QUESTION: What is the currency of UK?",
        ["A) Pound", "B) Crown", "C) Euro", "D) Dollar"],
        "A", 75
    ),
    Question2(
        "QUESTION: Jon Snow is a popular character of which television series?",
        ["A) HIMYM", "B) GOT", "C) Friends", "D) Rampage"],
        "B", 75
    ),
    Question2(
        "QUESTION: Which is the most popular social media network?",
        ["A) Twitter", "B) Tik Tok", "C) Instagram", "D) Facebook"],
        "C", 75
    ),
    Question2(
        "QUESTION: Avengers Infinity War was released in the US in which month of 2018?",
        ["A) April", "B) November", "C) December", "D) January"],
        "A", 75
    ),
]
class Question3(NamedTuple): #cat 3 of questions
    question: str
    answers: List[str]
    correct: str
    amount: int

questions3 = [
    
    Question3(
        "QUESTION: Saudi Arabia is the biggest producer of?",
        ["A) Coffee", "B) Leather", "C) Coal", "D) Oil"],
        "D", 125
    ),
    Question3(
        "QUESTION: Which of these countries did NOT fight in WWII?",
        ["A) Switzerland", "B) Italy", "C) Germany", "D) Ireland"],
        "A", 125
    ),
    Question3(
        "QUESTION: QUESTION: What is the main difference between a supercharger and a turbocharger?",
        ["A) Drive Mechanisms", "B) Name", "C) Supercharger is American", "D) Sound"],
        "A", 125
    ),
    Question3(
        "QUESTION: What country was tennis player Novak Djokovic born in?",
        ["A) Bosnia", "B) Slovenia", "C) Ukraine", "D) Poland"],
        "A", 125
    ),
    Question3(
        "QUESTION: In pool, what color is the 6-ball?",
        ["A) Red", "B) Green", "C) Blue", "D) Black"],
        "B", 125
    ),
]
class Question4(NamedTuple): #cat 3 of questions
    question: str
    answers: List[str]
    correct: str
    amount: int

questions4 = [
    Question4(
        "QUESTION: What US city is associated with Alcatraz?",
        ["A) New York", "B) Washington", "C) Los Angeles", "D) San Francisco"],
        "D", 175
    ),
    Question4(
        "QUESTION: What is the capital of Senegal?",
        ["A) Kampala", "B) Dakar", "C) Nairobi", "D) Rabat"],
        "B", 175
    ),
    Question4(
        "QUESTION: Which country hosted the 1982 FIFA World Cup?",
        ["A) Spain", "B) Mexico", "C) Brasil", "D) France"],
        "A", 175
    ),
    Question4(
        "QUESTION: Which country has the most time zones?",
        ["A) United States", "B) China", "C) Russia", "D) Australia"],
        "C", 175
    ),
    Question4(
        "QUESTION: Which colour is used as a term to describe an illegal market for rare goods?",
        ["A) Blue", "B) Brown", "C) Black", "D) Yellow"],
        "C", 175
    ),
]
class Question5(NamedTuple): #cat 3 of questions
    question: str
    answers: List[str]
    correct: str
    amount: int

questions5 = [
    Question5(
        "QUESTION: Who created the game Space Invaders?",
        ["A) Konami", "B) Kiichiro Toyoda", "C) Tomohiro Nishikado", "D) Shigeru Miyamoto"],
        "D", 350
    ),
    Question5(
        "QUESTION: Who led over 900 followers in a mass suicide in 1978?",
        ["A) Jim Jones", "B) Abimael Guzmán", "C) Larry Phillips Jr", "D) Shoko Asahara"],
        "A", 350
    ),
    Question5(
        "QUESTION: How many days is the Olympic decathlon held over?",
         ["A) Two", "B) One", "C) Three", "D) Four"],
        "A", 350
    ),
    Question5(
        "Suva is the capital of?",
        ["A) Fiji", "B) Indonesia", "C) Bangladesh", "D) Taiwan"],
        "A", 350
    ),
    Question5(
        "QUESTION: What does IPA stand for related to food?",
        ["A) India Pale Ale", "B) International Phonetic Alphabet", "C) International Psychoanalytical Association", "D) International Police Association"],
        "A", 350
    ),
]



def questionnaire(q: Question1) -> Tuple[int, bool]:
    """Randomizes question and evaluates answer"""
    print(q.question)
    for answer in q.answers:
        print(answer)
    usr_input_answer = input(
        " What's your answer? "
        "Please select between A, B, C, D or R for Retirement. "
    ).upper()
    if usr_input_answer == q.correct:
        return q.amount, True
    elif usr_input_answer == "R":
        print("You decided to retire, you have: " + str(money) + " points")
    else:
        print("Game over!")
    return 0, False


money = 0 #Prize in points
keep_playing = True #Allows the game to be closed in case Retirement or incorrect answer, condition to be met in order to play is True.
while keep_playing == True and money < 50:
    winnings, keep_playing = questionnaire(choice(questions1))
    money += winnings
while keep_playing == True and money >= 50 and money < 200:
    winnings, keep_playing = questionnaire(choice(questions2))
    money += winnings
while keep_playing == True and money >= 200 and money < 450:
    winnings, keep_playing = questionnaire(choice(questions3))
    money += winnings
while keep_playing == True and money >= 450 and money < 800:
    winnings, keep_playing = questionnaire(choice(questions4))
    money += winnings
while keep_playing == True and money >= 800:
    winnings, keep_playing = questionnaire(choice(questions5))
    money += winnings
    if money == 1500:
      print("Congratulations, You've won! A total of 1500 points were earned")
      break
#First round ends when user reaches 50 points as each question is 25. Second round ends when user reaches 200 since each question for the second round takes 75 points. Third round goes from 200 to 450. Fourth round goes from 450 to 800. Fifth and last is from 800 to 1500 points.
