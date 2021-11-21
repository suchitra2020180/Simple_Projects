##Project23_ adding to nested_dictionaries

tour_list=[
    {"country": "France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {"country": "Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    }
]

## To add a new dictionary to existing we will create a function and a new dictionary inside a function
def add_item (given_country,given_visits,given_cities):
    new_dict={}
    new_dict["country"]=given_country,
    new_dict["visits"]=given_visits,
    new_dict["cities"]=given_cities
    tour_list.append(new_dict)



add_item("Russia",2,["Moscow"," saint Lille"," trw_Dijon"])
print(tour_list)