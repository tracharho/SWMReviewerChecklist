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
    

    data = {}
    j = 1
    for cat, sub in catandsub.items():
        for file in sub:
            filename= file.replace('.csv',"")
            data[cat] = {filename:{}}
            path = os.getcwd() + "/static/csv/{}/{}".format(cat,file)
            with open(path, 'r') as f:
                
                csvReader = csv.DictReader(f)  
                for row in csvReader:
                    data[cat][filename]["row"+str(j)] = row
                    j += 1
    
    jsonFilePath = os.getcwd()+"/static/checklist.json"

    with open(jsonFilePath, 'w') as jsonf:
        print('hit')
        jsonf.write("[" + json.dumps(data, indent=4) + "]")

if __name__ == "__main__":
    categorize_csvs()
    
