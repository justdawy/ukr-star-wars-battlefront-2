import csv

with open('temp.csv', encoding="utf-8") as csv_file, \
     open('localization_uk.txt', mode="w", encoding="utf-8") as txt_file, \
     open('localization_en.txt', mode="r", encoding="utf-8") as eng_file:

    csv_reader = csv.DictReader(csv_file, delimiter=",")
    
        if csv_reader.fieldnames:
        print(f"Column names are {', '.join(csv_reader.fieldnames)}")

    for row in csv_reader:
        eng_line = eng_file.readline()
        
        target_text = row.get("target")
        
        
        if target_text and target_text.strip():
            txt_file.write(target_text.strip() + "\n")
        else:
            txt_file.write(eng_line)

print("Ready")