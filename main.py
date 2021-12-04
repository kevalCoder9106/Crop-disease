import pandas

data = pandas.read_csv("data.csv")

def find_disease(season,p_name):
    index = 0
    while True:
        try:
            if data.iloc[index]['season'] == season and data.iloc[index]['plant_name'] == p_name:
                return [data.iloc[index]['disease'],data.iloc[index]['decription']]
            
            index = index + 1
        except:
            break
    
    return 0

if __name__ == "__main__":
    season = input("Enter season: ")
    p_name = input("Enter plant name: ")

    itr_data = find_disease(season,p_name)
    
    if itr_data != 0:
        print("----------------------------------------------------------------------------------")
        print(f"\n\nPlant name: {p_name}\nDisease: {itr_data[0]}\nDescription: {itr_data[1]}\n")
        print("----------------------------------------------------------------------------------")
    else:
        print("Invalid input")
