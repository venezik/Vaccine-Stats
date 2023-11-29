import csv
def dic_list_gen(lsts, array):
    a = []
    for x in array:
        dit = {}
        idx = 0
        for l in x:
            dit[lsts[idx]] = l
            idx = idx + 1
        a.append(dit)
    return a    

def read_values(filename):
    final = []
    with open(filename) as f:
        read = csv.reader(f)
        count = 0
        for ln in read:
            if count != 0:
                arr = []
                for y in ln:
                    arr.append(y)
                final.append(arr)
            count = count+1
        return final

def make_lists(dic,dic1):
    res = []
    for i in dic1:
        arr = []
        for num in dic:
            arr.append(i[num])
        res.append(arr)
    return res

def write_values(filename, l1st):
    with open(filename, "a+") as f:
        wr = csv.writer(f)
        for i in l1st:
            arr= []
            for y in i:
                arr.append(y)
            wr.writerow(arr)


import json
import urllib.request

def json_loader(url):
    converted = urllib.request.urlopen(url)
    string = converted.read().decode()
    convertedString = json.loads(string)
    return convertedString

def make_values_numeric(lst,dict1):
    for i in lst:
        if i in dict1:
            val = dict1[i]
            val = float(val)
            dict1[i] = val
    return dict1

def save_data(lstStr,lstDict,filename) :
    with open(filename, "w") as f:
        write = csv.writer(f)
        var = make_lists(lstStr, lstDict)
        write.writerow(lstStr)
        for i in var:
            write.writerow(i)


def load_data(filename):
    lst =[]
    with open(filename) as f:
        read = csv.reader(f)
        header = next(read) 
        for i in read:
            lst.append(i)
        
        x = dic_list_gen(header,lst)
        return x
