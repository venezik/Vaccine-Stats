import bottle
import json
import data
import processing
import os.path


def load_data( ):
    csv_file = 'saved_data.csv'
    if not os.path.isfile(csv_file):
        url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
        info = data.json_loader(url)
        heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer',\
                   'administered_unk_manuf','series_complete_pop_pct']
        data.save_data(heads, info, 'saved_data.csv')

load_data()
@bottle.route("/")

def index() :
    return bottle.static_file("index.html", root = ".")
    
@bottle.route("/styles.css")
def styles():
    return bottle.static_file("styles.css", root = ".")
    
@bottle.route("/one.js")

def one():
    return bottle.static_file("one.js", root = '.')
#ld = data.load_data("saved_data.csv")
#maxDate = processing.max_value(ld,"date")
#lstmaxDate = processing.copy_matching(ld,"date",maxDate)
#print(maxDate)
#print(lstmaxDate)
#newDict = {"x":[],"y" :[], "type": "bar"}
#for dic in lstmaxDate:
#    location = dic["location"]
#    value = dic["series_complete_pop_pct"]
#    newDict["x"].append(location)
#    newDict["y"].append(value)
#data_var = [newDict]
#print(data_var)

@bottle.route("/bar")

def bar():
    ld = data.load_data("saved_data.csv")
    maxDate = processing.max_value(ld,"date")
    lstmaxDate = processing.copy_matching(ld,"date",maxDate)
    newDict = {"x":[],"y" :[], "type": "bar"}
    for dic in lstmaxDate:
        location = dic["location"]
        value = dic["series_complete_pop_pct"]
        newDict["x"].append(location)
        newDict["y"].append(value)
    data_var = [newDict]
    return json.dumps(data_var)
#A route to serve up the bar chart data as a JSON blob
#A route to serve up the line graph data as a JSON blob
@bottle.route("/pie")
#A route to serve up the pie chart data a JSON blob
def pie():
    ld = data.load_data("saved_data.csv")
    maxDate = processing.max_value(ld,"date")
    lstmaxDate = processing.copy_matching(ld,"date",maxDate)
    emptylst = []
    for t in lstmaxDate:
        numerical = data.make_values_numeric(['administered_janssen', 'administered_moderna', 'administered_pfizer','administered_unk_manuf'], t)
        emptylst.append(numerical)
    pie1 = processing.sum_matches(emptylst,"date",maxDate,'administered_janssen')
    pie2 = processing.sum_matches(emptylst,"date",maxDate,'administered_moderna')
    pie3 = processing.sum_matches(emptylst,"date",maxDate,'administered_pfizer')
    pie4 = processing.sum_matches(emptylst,"date",maxDate,'administered_unk_manuf')
    emptydata = {}
    labels = ['Janssen', 'Moderna', 'Pfizer','Unknown']
    values = [pie1,pie2,pie3,pie4]
    emptydata["values"] = values
    emptydata["labels"] = labels
    emptydata["type"] = "pie"
    return json.dumps([emptydata])

@bottle.post("/line")
def line():
    blob = bottle.request.body.read().decode()
    var = json.loads(blob)
    ld = data.load_data("saved_data.csv")
    lstofLocation = processing.copy_matching(ld,"location",var)
    lstofLocation.sort(key = compare)
    formatedDict = {"x":[],"y": [],"type": "scatter" }

    for i in lstofLocation:
        dats = i["date"] 
        datz = float(i["series_complete_pop_pct"])
        formatedDict["x"].append(dats)
        formatedDict["y"].append(datz)
    return json.dumps([formatedDict])

def compare(dict):
    return dict["date"]


    return None
bottle.run(host="0.0.0.0",post=8080)