import os, json, csv

    
def categorize_csvs():
    csvdir = os.path.abspath(os.getcwd()+ '/static/csv')
    folder = []
    for i in os.walk(csvdir,topdown=True):
        folder.append(i)

    catandsub = {}
    categories = folder[0][1]
    for subcategories in categories:
        path = csvdir + "/" + subcategories
        subcategory = os.listdir(path)
        catandsub[subcategories] = subcategory
    

    data = []
    dummy = {}
    j = 1
    l = [] #row list
    m = [] #subcat list
    n= [] #cat list
    
    row_num = [] #row number list
    #cat : categories which happen be the folders
    #sub : list of subcategories
    #print(catandsub.items())
    for cat, sub in catandsub.items(): #looping through each folder is correct
        #print(dummy)
        c = []
        for file in sub: #for each .csv in the folder
            b = {}
            filename= file.replace('.csv',"") #use new var as a subcat string
            path = os.getcwd() + "/static/csv/{}/{}".format(cat,file) #open the spcific file from teh static folder 
            al = []
            with open(path, 'r') as f: 
                csvReader = csv.DictReader(f)     
                for row in csvReader:
                    a = {}
                    for k, v in row.items():
                        a[k] = v
                    a["rownum"] = ("row"+str(j))
                    row_num.append("row"+str(j))
                    al.append(a)
                    j += 1
                b[filename] = al
                print('----')
                print(b)
                print('----')
            c.append(b)
        dummy[cat] = c
        print('***')
        print(dummy[cat])
        print('***')
    data = [dummy]
    jsonFilePath = os.getcwd()+"/static/checklist.json"
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    print(data)
if __name__ == "__main__":
    categorize_csvs()
    
