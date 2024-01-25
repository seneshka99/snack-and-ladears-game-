import random
#add the snack and ladears key values
snack_and_ladears = {27:5,40 :3 ,43:18,54:31,66:45,76:58,89:53,99:41,
                 4:25,13:46,33:49,50:69,42:63,62:81,74:92}
def rool():
    return random.randint(1,6)
def first(first_playear):
    Firat_new_poaiahion = 0
    first_playear = rool()
    Firat_new_poaiahion += first_playear
    if Firat_new_poaiahion == 100:
        print("first playear is a win")
      
      #firt playear new bord latear nombear
    if Firat_new_poaiahion in snack_and_ladears:
        print(" firat playear latter :",Firat_new_poaiahion)
        print("opps firat playear new posishion :",snack_and_ladears[Firat_new_poaiahion])
        
    else:
        print("first playear letter",first_playear)
    
def Second(second_playear):
    Second_new_posishion = 0
    second_playear = rool()
    Second_new_posishion += second_playear
    if Second_new_posishion == 100:
            print("second playear is a win")
    #second playear new bord latear nomber
    if Second_new_posishion in snack_and_ladears:
        print("second playear latter :",Second_new_posishion)
        print("oops Seconnd playear new poaiahion :",snack_and_ladears[Second_new_posishion])
        
    else:
        print("second playear latter",second_playear)
        
#board rooling 
def board():
    x= ""
    for _ in range(100):
        input("press the enter butten rooling")
        print(first(x))
        print(Second(x))
       
        
result = board()
print(result)
