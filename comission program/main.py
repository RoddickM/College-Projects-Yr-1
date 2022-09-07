from estate_agent_comission import *
from graph_for_all_estate_agency import *

def main_menu():
    menu_display = "Welcome to T-Level Agencies!!"
    menu_display += "\nWhat action would you like to choose"
    menu_display += "\n[ 1 ] View each agency's total comission as a table"
    menu_display += "\n[ 2 ] View graph comparisson of all estate agency"
    menu_display += "\n[ 3 ] Exit"
    print(menu_display)
    
main_menu()
choose = int(input("\nType the number next to the agency you wish to analyse: "))

if choose == 1:
    commission_agency_text_display()
elif choose == 2:
    view_all_agency_graph()

    