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
    return catandsub

def read_csvs(catandsub):
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
                    l = {}
                    l["id"] = j
                    l["Problem"] = row['Problem']
                    l["Comment"] = row['Comment']
                    l["Reference"] = row['Reference']
                    data[cat][filename] = l
                    j += 1
    return data

#Function extracts data from /static/csv and 
#formats into categorical form. 
    # # Open a csv reader called DictReader
    # with open(csvFilePath) as csvf:
    #     csvReader = csv.DictReader(csvf)       
    #     # Convert each row into a dictionary 
    #     # and add it to data
    #     for rows in csvReader:           
    #         # Assuming a column named 'No' to
    #         # be the primary key
    #         key = rows['No']
    #         data[key] = rows
    # # Open a json writer, and use the json.dumps() 
    # # function to dump data
    # # generate.js only reads jsons that are wrapped with [ ] brackets
    # # appended the string value to include the brackets
    # with open(jsonFilePath, 'w') as jsonf:
    #     print(type(json.dumps(data,indent=4)))
    #     jsonf.write("[" + json.dumps(data, indent=4) + "]")

if __name__ == "__main__":
    categories = categorize_csvs()
    data = read_csvs(categories)
    for k,v in data.items():
        print(k,"+++++", v)
