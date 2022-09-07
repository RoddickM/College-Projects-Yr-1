import pandas as pd
import matplotlib.pyplot as plt


def view_all_agency_graph():
    df = pd.read_csv("EstateAgents.csv")
    
    count = df["Estate Agent"].value_counts()
    estate_agency = []
    total_comission_axis = []
    
    for i in count.index:
        estate_agency.append(i)
        
    for agency in estate_agency:
        extract_comm = df.loc[(df["Estate Agent"] == agency), df.columns != "Estate Agent"]
        extract_comm["Commission Earned"] = round(extract_comm["Consultation fees"] * (extract_comm["Commission (%)"] / 100), 2)
        
        total_commission = round(extract_comm["Commission Earned"].sum(), 2)
        total_comission_axis.append(float(total_commission))
    
    plt.bar(estate_agency, total_comission_axis)
    plt.xticks(rotation=90)
    plt.show()
    

