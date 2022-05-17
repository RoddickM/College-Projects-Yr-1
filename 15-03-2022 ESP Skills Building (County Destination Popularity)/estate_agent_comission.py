import pandas as pd


def get_estate_agent(menu_choice):
    estate_agencies = {
        1 : "McDonalds Mansions",
        2 : "Athar Estates",
        3 : "Jepsons Bungalows",
        4 : "Rand Real Estates",
        5 : "Lennas Lettings"
        }
    
    chosen_estate_agency = estate_agencies.get(menu_choice)
    
    return chosen_estate_agency


def display_estate_agent_total_comission(estate_agency):
    df = pd.read_csv("EstateAgents.csv")

    extract_comm = df.loc[(df["Estate Agent"] == estate_agency), df.columns != "Estate Agent"]
    extract_comm["Commission Earned"] = round(extract_comm["Consultation fees"] * (extract_comm["Commission (%)"] / 100), 2)

    comm_calculated = extract_comm.to_string(index=False)

    total_commission = round(extract_comm["Commission Earned"].sum(), 2)

    print(f"\nHere is a breakdown of the comission earned in for {estate_agency}")
    print("")
    print(comm_calculated)
    print("")
    print(f"The total comission earned in all year for {estate_agency} was £{total_commission}\n")
    

def commission_agency_text_display():
    def estate_comission_menu():
        menu_display = "Welcome to T-Level Agencies!!"
        menu_display += "\nWhich agency would you like to check?"
        menu_display += "\n[ 1 ] McDonalds Mansions"
        menu_display += "\n[ 2 ] Athar Estates"
        menu_display += "\n[ 3 ] Jepsons Bungalows"
        menu_display += "\n[ 4 ] Rand Real Estates"
        menu_display += "\n[ 5 ] Lennas Lettings"
        menu_display += "\n[ 6 ] Exit"
        print(menu_display)
    
    while True:
        estate_comission_menu()
        choose = int(input("\nType the number next to the agency you wish to analyse: "))
        if choose == 6:
            break
        
        estate_agency_of_choice = get_estate_agent(choose)
        display_estate_agent_total_comission(estate_agency_of_choice)
