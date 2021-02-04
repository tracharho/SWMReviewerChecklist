import os, json, csv

    
def categorizeCsvs():
    path_to_csvs = '/app/static/csv'
    if os.path.exists(os.getcwd()+ path_to_csvs):
        csvdir = os.path.abspath(os.getcwd()+ path_to_csvs)
        folder = []
        for i in os.walk(csvdir,topdown=True):
            folder.append(i)
        catandsub = {}
        categories = folder[0][1]
        for subcategories in categories:
            path = csvdir + "/" + subcategories
            subcategory = os.listdir(path)
            catandsub[subcategories] = subcategory
    else:
        return "MISSION FAILURE ON {}".format(os.getcwd())
    

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
            path = os.getcwd() + path_to_csvs + "/{}/{}".format(cat,file) #open the spcific file from teh static folder 
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
            c.append(b)
        dummy[cat] = c
    data = [dummy]
    jsonFilePath = os.getcwd()+ path_to_csvs + ".json"
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
if __name__ == "__main__":
    categorizeCsvs()
    
