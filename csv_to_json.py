


if __name__ == "__main__":
    make_json(csvFilePath, jsonFilePath)

import csv
import json
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No']
            data[key] = rows
 
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    # generate.js only reads jsons that are wrapped with [ ] brackets
    # appended the string value to include the brackets
    with open(jsonFilePath, 'w') as jsonf:
        print(type(json.dumps(data,indent=4)))
        jsonf.write("[" + json.dumps(data, indent=4) + "]")
