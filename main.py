import random
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS= 5
a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
b= random.randint(NOMBRE_MIN,NOMBRE_MAX)

def poser_une_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    z = random.randint(0,1)
    operateur_str ="+" or "-"
    if z == 1:
        operateur_str = "*"
    reponse_str = input(f"combien font : {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if z == 1:
        calcul = a*b
    if reponse_int==calcul:
         return True

    return False

nombre_pts = 0
for i in range(0,NB_QUESTIONS):
    print(f"Question n°{i+1} /{NB_QUESTIONS} ")
    if poser_une_question():
        print("Réponse CORRECTE")
        nombre_pts += 1
    else :
        print("Réponse INCORRECTE")
    print()

print(f"Votre note est de {nombre_pts}/{NB_QUESTIONS} ")
moyenne= int(NB_QUESTIONS/2)
if nombre_pts == NB_QUESTIONS:
    print("Excellent travail ! C'est un sans faute.")
elif nombre_pts == 0:
    print("Pire score possible... C'est catastrophique")
elif 0<nombre_pts < moyenne:
    print("Vous n'avez même pas la moyenne... Révisez !")
elif nombre_pts == moyenne:
    print("Vous avez tout juste la moyenne...")
elif moyenne < nombre_pts < NB_QUESTIONS:
    print("Cela reste correcte, persévérez !")
