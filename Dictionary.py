
person = {"name": "Dorota Dybas",
            "country": "Poland",
            "job": "Sale assistant",
            "hobby":["decorating", "dancing"],
            "age": 37}


                    
                
def add_hobby(person, new_hobby):
    person["hobby"].append(new_hobby)


add_hobby(person, "reading")
print(person["hobby"])



