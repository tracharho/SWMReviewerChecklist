import os, json, csv
from app.models import OriginalRow
from app import db

# TO DO
# - Decide if the JSON writing should stay or go. 
# - Refractor and stuff.
def createChecklistJSON():
    path_to_csvs = '/app/static/csv'
    if os.path.exists(os.getcwd()+ path_to_csvs):
        csvdir = os.path.abspath(os.getcwd()+ path_to_csvs)
        folder = [i for i in os.walk(csvdir,topdown=True)]
        catandsub = {}
        categories = folder[0][1]
        for subcategories in categories:
            path = csvdir + "/" + subcategories
            subcategory = os.listdir(path)
            catandsub[subcategories] = subcategory
    else:
        return "MISSION FAILURE ON {}".format(os.getcwd())
    
    """ 
    Sample Directory Tree inside the csv folder
    
    .
    ├── Erosion and Sediment Control (Category)
    │   └── Silt Fence.csv (Subcategory)
    ├── General (Category)
    │   └── Site Plan - General Requirements.csv (Subcategory)
    └── Stormwater (Category)
        ├── Permeable Pavement.csv (Subcategory)
        └── Stormwater - General Requirements.csv (Subcategory)
    
    Each subcateory has its own number of rows
    -subcat : Subcatchment
    -cat : list of categories which is also the names of the Category folders
    -sub : list of subcategories which is the name of the Subcategory file names
    -filename : the subcategory string stripped of '.csv'
    """
    
    dummy = {} # a temporary container dictionary
    j = 1 # int iterator
    
    row_num = [] #row number list
    #sub : list of subcategories
    #filename : String name of the subcategory
    for cat, sub in catandsub.items():
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
                    rowdb = OriginalRow()
                    # row is an ordered dictionary, use dictionary indexsing for looping
                    for k, v in row.items(): # k : column name & v : column value
                        a[k] = v      
                    
                    a["row_number"] = ("row"+str(j))
                    a['subcategory'] = filename
                    a['category'] = cat
                    for k, v in a.items():
                        setattr(rowdb, k, v)
                    rowdb.checked = False
                    db.session.add(rowdb)
                    al.append(a)
                    j += 1
    db.session.commit()
    data = [dummy] # the end resulting list that will contain dummy inside a list.
    jsonFilePath = os.getcwd()+ path_to_csvs + ".json"
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        print('hit')

if __name__ == "__main__":
    createChecklistJSON()
    
