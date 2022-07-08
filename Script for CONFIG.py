
with open('CONFIG.jsn', 'r', encoding='utf-8') as file:
    reader = file.read()
    reader = reader.replace("'", '&')
    reader = reader.replace('&', '"')

with open('CONFIG.jsn', 'w', encoding='utf-8') as js_file:
      js_file.write(reader)

