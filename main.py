
from utils.clear import clear
from sources.lolcounter import find_counters as lolcounter
from sources.ugg import find_counters as ugg
from sources.rankedboost import find_counters as rankedboost

def interface():
    champ = input("Champion: >> ")
    clear()
    try:
        weakest = ugg(champ) # < change the source here
    except:
        print("The champion doesn't exist!")
        input()
        clear()
        interface() # repeat

    print(f"{champ.capitalize()}'s counters:\n")
    for i in weakest:
        print(i)
    
    input()
    clear()
    interface() # repeat

interface()