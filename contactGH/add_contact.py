import json

#contact_name = input("Quel est le nom du contact ? : ")
#contact_number = input("Quel est le numéro de téléphone du contact ? : ")
#contact_mail = input("Quel est le l'adresse mail du contact ? : ")
#contact_location = input("Quel est l'adresse du contact ? : ")
#contact_birthday = input("Quand est l'anniversaire du contact ? : ")
#contact_notes = input("Quelle note voulez vous ajouter au contact ? : ")


def adding(contact_name,contact_number,contact_mail,contact_location,contact_birthday,contact_notes):
    dataTest = {
                "name": contact_name,
                "number" : contact_number,
                "mail" : contact_mail,
                "location" : contact_location,
                "birthday": contact_birthday,
                "notes": contact_notes
            }


    with open("contact.json","r+") as f:
        data=json.load(f)
        data.append(dataTest)
        f.seek(0)
        f.write(json.dumps(data, indent=4))







    
    