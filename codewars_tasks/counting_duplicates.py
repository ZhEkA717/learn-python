def duplicate_count(text):
    hash = {}
    for el in text.lower():
        if not el in hash:
            hash[el] = 1
        else: hash[el]+=1
    
    filter_hash = {}

    for el in hash:
        if hash[el] > 1:
            filter_hash[el] = hash[el]

    return len(filter_hash)
        

print(duplicate_count('aAbbcde') )
        