#The script remove unneccesary lines (spaces, chars, etc.) and leaves countries only

#Load raw data file to be clean
with open("countries_raw.txt", "r") as file:
  content = file.readlines()

#Data cleaner parameters
content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]

print(content)

#Export/create new file cleaned
with open("countries_clean.txt", "w") as file:
  for i in content:
    file.write(i+"\n")
print("Completed.")

#Data Checker
checklist = ["Portugal", "Germany", "Munster", "Spain"]

'''
One of the items is not a country. Please use Python and the file containing the list of countries (attached) as the data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.
'''
with open("countries_clean.txt", "r") as file:
    content = file.readlines()
 
content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]
 
print(checked)

'''
We're opening our file data source and loading it in Python as a list in content. Then we clean out that list of break lines in line 6. Then, in line 7, we check if the items of content  are in checklist and if they are, we leave them on the list; otherwise, we remove them. So, we end up with only three matches.
'''