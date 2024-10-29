class Question():
    def __init__(self, statement="", list_propositions=[], correct_answer=0):
        self.setStatement(statement)
        self.setListPropositions(list_propositions)
        self.setCorrectAnswer(correct_answer)

    def setStatement(self, statement):
        if issubclass(type(statement), str): # Vérifie que le paramètre statement soit bien de type string
            self.statement = statement
        else:
            print("Erreur : le paramètre attentdu pour la méthode addStatement est de type string")

    def setListPropositions(self, list_propositions):
        if type(list_propositions) is list:
            error = False
            for proposition in list_propositions:
                # Vérifie que chaque élément de la liste est de type string
                if issubclass(type(proposition), str) == False :
                    print("Erreur : le paramètre attendu pour la méthode setListPropositions est une liste d'élements de type string")
                    error = True
                    break
            if error == False:
                self.list_propositions = list_propositions
        else:
            print("Erreur : le paramètre attendu pour la méthode setListPropositions doit être une liste de string")
            
    
    def addProposition(self, proposition):
        if issubclass(type(proposition), 'str') == False :
            print("Erreur : le paramètre attendu pour la méthode addProposition doit être de type string")
        else:
            self.list_propositions.append(proposition)

    def setCorrectAnswer(self, correct_answer):
        if isinstance(correct_answer, int) == False:
            print("Erreur : le paramètre attendu pour la méthode setCorrectAnswer doit être de type int")
        elif correct_answer < 0:
            print(f"Erreur : le paramètre attendu pour la méthode setCorrectAnswer doit être un entier positif")
        elif len(self.list_propositions) > 0 and correct_answer < 1 and correct_answer > len(self.list_propositions):
            print(f"Erreur : Pour cette question, la réponse correcte doit être un entier compris entre 1 et {len(self.list_propositions)}")
        elif len(self.list_propositions) == 0 and correct_answer > 0:
            print(f"Erreur : Il faut d'abord renseigner la liste de propositions pour la question avant de paramétrer la réponse correcte")
        else:
            self.correct_answer = correct_answer
                 

    def ask(self, remaining_chances):
        print(f"{self.statement}")
        for index, proposition in enumerate(self.list_propositions, start=1):
            print(f"{index} : {proposition}")

        while remaining_chances > 0:
            user_answer = input("Ta réponse (numéro) : ")
            if self.checkAnswerFormat(user_answer) == True:
                old_remaining_chances = remaining_chances
                remaining_chances = self.checkCorrectAnswer(user_answer, old_remaining_chances)
                if remaining_chances == old_remaining_chances: # == le user a donné la bonne réponse
                    break
        
        return remaining_chances

    def checkAnswerFormat(self, user_answer):
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Erreur : Tu dois saisir le numéro de ta réponse")
            valid_format = False
        else:
            if user_answer < 0 or user_answer > len(self.list_propositions):
                print(f"Erreur : Tu dois saisir un numéro entre 1 et {len(self.list_propositions)}")
                valid_format = False
            else:
                valid_format = True
        
        return valid_format
    
    def checkCorrectAnswer(self, user_answer, remaining_chances):
        if int(user_answer) == self.correct_answer:
            print("Bonne réponse !\n")
        else:
            remaining_chances -= 1
            if remaining_chances == 1:
                print("Mauvaise réponse :( - ATTENTION : il ne te reste plus qu'1 seule erreur possible !")
            else:
                print(f"Mauvaise réponse :( - Il te reste {remaining_chances} erreurs possibles !")
        
        return remaining_chances

class Quiz():
    def __init__(self, list_questions=[]):
        self.list_questions = list_questions

    def setListQuestions(self, list_questions):
        if type(list_questions) is list:
            error = False
            for question in list_questions:
                # Vérifie que chaque élément de la liste est de type string
                if isinstance(question, Question) == False :
                    print("Erreur : le paramètre attendu pour la méthode setListQuestions est une liste d'objets Question")
                    error = True
                    break
            if error == False:
                self.list_questions = list_questions
        else:
            print("Erreur : le paramètre attendu pour la méthode setListQuestions doit être une liste d'objets Question")

    def play(self, remaining_chances):
        print("QUIZ TIME!\n")

        for num, question in enumerate(self.list_questions):
            print(f"Question n°{num+1}")
            remaining_chances = question.ask(remaining_chances)
            if remaining_chances == 0:
                print("Tu as perdu :(")
                break
        
        if remaining_chances > 0:
            print("Bravo champion.ne ! Tu as terminé le quiz\n\n")

#########

question1 = Question(
    statement = "En quelle année est sortie l'album Nevermind, de Nirvana ?",
    list_propositions = ["1979", "1987", "1991", "1995"],
    correct_answer = 3
)

question2 = Question(
    statement = "Quelle est la capitale de l'Italie ?",
    list_propositions = ["Rome", "Florence", "Naples", "Venise"],
    correct_answer = 1
)

question3 = Question(
    statement = "De quelle couleur est le cheval blanc d'Henry IV ?",
    list_propositions = ["Rouge", "Blanc", "Vert", "Noir"],
    correct_answer = 2
)

remaining_chances = 3

quiz = Quiz(list_questions = [question1, question2, question3])
quiz.play(remaining_chances)