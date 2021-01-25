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
    j = 1
    l = [] #row list
    m = [] #subcat list
    n= [] #cat list
    row_num = [] #row number list
    #cat : categories, sub : subcategories
    for cat, sub in catandsub.items():
        for file in sub: #for each .csv in the folder
            # checks out - print(file)
            filename= file.replace('.csv',"") #use new var as a subcat string
            #data[cat] = {filename:{}} #initialize a deeper nested empty dict
            path = os.getcwd() + "/static/csv/{}/{}".format(cat,file) #open the spcific file from teh static folder
            with open(path, 'r') as f: 
                csvReader = csv.DictReader(f)     
                for row in csvReader:
                    m.append(filename) 
                    n.append(cat) 
                    l.append(row)  
                    row_num.append("row"+str(j))
                    j += 1

    for x in range(len(row_num)):
        data.append({n[x]:{m[x] :  {"Row_number":row_num[x], "Problem":l[x]['Problem'], "Comment":l[x]['Comment'], "Reference":l[x]['Reference']}}})
        

    jsonFilePath = os.getcwd()+"/static/checklist.json"

    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    categorize_csvs()
    
