from flask import Flask, make_response, render_template, request, redirect, send_file, url_for
import json
from add_contact import adding
import zipfile

def shutdown_server():
    
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()   


def read_data():

    global options

    data = open("contact.json", "r")
    data=json.load(data)
    
    
    options=[]
    i=0
    print("DATA READED")
    for x in range(len(data)):
        informations = data[i]
        options.append(informations["name"])
        i+=1
    print(options)

def info(option):

    global name
    global number
    global mail
    global location
    global birthday
    global notes
        
    data = open("contact.json", "r")
    data=json.load(data)
    

    data = data[option]
    name = data['name']
    number = data['number']
    mail = data['mail']
    location = data['location']
    birthday = data['birthday']
    notes = data['notes']

def remove(iD):
    data = open("contact.json", "r")
    data=json.load(data)

    del data[iD]   
    with open("contact.json","w") as f:

        f.write(json.dumps(data, indent=4))
 




app = Flask(__name__)


@app.route("/")
def choose():
    read_data()
    return render_template("index.html",options=options)

@app.route("/<int:contactNumber>")

def contact_info(contactNumber):
    read_data()
    if contactNumber > len(options)-1:
        return render_template("404.html")
    
    info(contactNumber)


    read_data()
    return render_template('details.html', name=name, number=number, mail=mail,location=location,birthday=birthday,notes=notes, options=options)
    
    


#@app.route("/contact_info", methods=["POST", "GET"])
#def contact_info():
        #output = request.form["selection"]
        #print(output)
        #info(int(output))
        #read_data()
        #return render_template('details.html', name=name, number=number, mail=mail,location=location,birthday=birthday,notes=notes, options=options)
    
@app.route("/add_contact")
def add_contact():
        read_data()
        return render_template('newcontact.html',options=options)

@app.route("/added", methods=["POST", "GET"])
def added():
    contact_name = request.form["add_name"]
    contact_number = request.form["add_number"]
    contact_mail = request.form["add_mail"]
    contact_location = request.form["add_location"]
    contact_birthday = request.form["add_birthday"]
    contact_notes = request.form["add_notes"]
    adding(contact_name,contact_number,contact_mail,contact_location,contact_birthday,contact_notes)
    read_data()

    return redirect(url_for('choose'))

@app.route('/delete', methods=["POST", "GET"])
def delete():
    
    if request.method == 'POST':
        if request.form['removeButton'] == 'delete':
            Id=int(str(request.referrer).split("/")[-1])
            remove(Id)
            
    return redirect(url_for('choose'))

@app.route('/export')
def export():
    filenames = ["contact.json"]
    with zipfile.ZipFile("contacts.zip", mode="w") as archive:
        for filename in filenames:
            archive.write(filename)
    return send_file("contacts.zip")

@app.route("/shutdown")
def shutdown():
    shutdown_server()


@app.errorhandler(404)
def not_found(e):
  
  return render_template("404.html")

app.run("0.0.0.0")