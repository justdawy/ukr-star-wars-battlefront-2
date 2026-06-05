import csv

# Назви файлів (змініть 'localization_pl.txt', якщо у вас інша назва польського файлу)
EN_FILE = 'localization_en.txt'
UK_FILE = 'localization_uk.txt'
PL_FILE = 'localization_pl.txt'
OUTPUT_CSV = 'result.csv'

with open(EN_FILE, 'r', encoding='utf-8') as f_en, \
     open(UK_FILE, 'r', encoding='utf-8') as f_uk, \
     open(PL_FILE, 'r', encoding='utf-8') as f_pl, \
     open(OUTPUT_CSV, 'w', encoding='utf-8', newline='') as f_csv:

    writer = csv.writer(f_csv, delimiter=',')
    
    writer.writerow(['id', 'source', 'target', 'context'])

    for index, (line_en, line_uk, line_pl) in enumerate(zip(f_en, f_uk, f_pl), start=1):
        
        source_text = line_en.strip()
        uk_text = line_uk.strip()
        context_text = line_pl.strip()

        if uk_text == source_text or not uk_text:
            target_text = ""
        else:
            target_text = uk_text

        writer.writerow([index, source_text, target_text, context_text])

print(f"Файл {OUTPUT_CSV} успішно створено!")