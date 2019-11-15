import csv

with open('UNdata_Export_20191115_224402618.csv', mode='r') as csv_file:
    raw_data = csv.reader(csv_file) #reads data of births from UN

    country_list = []
    data = []

    for row in raw_data:
        if row[0] not in country_list: #creates dictionary for each country
            country_dic = {"Country": row[0]}
            data.append(country_dic)
            country_list.append(row[0])

        if row[3] == "999999" and row[1] == "2001":
            data[country_list.index(row[0])]["TotalBirths2001"] = int(row[4]) # adds total births of 2001 to ditcionary
        elif row[3] == "999999" and row[1] == "2000":
            data[country_list.index(row[0])]["TotalBirths2000"] = int(row[4]) # adds total births of 2000 to ditcionary
        elif row[3] == "011011" and row[1] == "2001":
            data[country_list.index(row[0])]["BirthsNovember2001"] = int(row[4]) # adds births of november 2001 to ditcionary

with open('DiscoverEU_data.csv', mode='r') as csv_file:
    raw_data = csv.reader(csv_file) # reads data of DiscoverEU_data participation
    for row in raw_data:
        data[country_list.index(row[0])]["Participants2000"] = int(row[1]) # adds nº of participants in last year's edition to dictionary

CountriesMissingData = []
NovemberPeople = 0

for country in data:
    try:
        country["PopulationParticipation"] = country["Participants2000"]/country["TotalBirths2000"] # calculates fraction of eledgible population that participated
        country["NovemberFraction"] = country["BirthsNovember2001"]/country["TotalBirths2001"] # calculates fraction of november born people
        country["Participants2001"] = country["TotalBirths2001"] * country["PopulationParticipation"] # predicts number of participants for this year's edition
        country["NovemberParticipants"] = country["Participants2001"] * country["NovemberFraction"] # predicts number of participants born in november
        NovemberPeople += country["NovemberParticipants"] 
    except:
        CountriesMissingData.append(country["Country"]) # if something is missing let us know

print(data)
print(CountriesMissingData)
print(NovemberPeople)


