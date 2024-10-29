class Imputer(list):
    def __init__(self, list):
        self.list = list

    def avg(self):
        # Vérification des valeurs dans la liste
        nb_none_values = 0

        for number in self.list:
            try:
                if number != None:
                    number = float(number)
                else:
                    nb_none_values += 1
            except ValueError:
                print("Erreur : La liste fournie en paramètre de la méthode avg() contient une valeur non numérique et différente de None")
                return []
        
        if nb_none_values == len(self.list):
            meanValue = 0
        else:
            meanValue = sum(number for number in self.list if number is not None) / sum(1 for number in self.list if number is not None)

        self.list = [meanValue if number is None else number for number in self.list]

        return self.list
    
    def median(self):
        # Vérification des valeurs dans la liste
        for number in self.list:
            try:
                if number != None:
                    number = float(number)
            except ValueError:
                print("Erreur : La liste fournie en paramètre de la méthode median() contient une valeur non numérique et différente de None")
                return []
            
        filledValues = sorted([number for number in self.list if number is not None])

        nbFilledValues = len(filledValues)

        if nbFilledValues % 2 == 1:
            medianValue = filledValues[nbFilledValues // 2]
        else:
            medianValue = (filledValues[nbFilledValues // 2] + filledValues[nbFilledValues // 2 - 1]) / 2

        self.list = [medianValue if number == None else number for number in self.list]

        return self.list

#######
 
myList = [None, 2, 3, 12, 5, 6, None]
print(myList)

myImputer = Imputer(myList)
newList = myImputer.avg()
print(newList)
print('----------')

print(myList)
myImputer2 = Imputer(myList)
newList2 = myImputer2.median()
print(newList2)