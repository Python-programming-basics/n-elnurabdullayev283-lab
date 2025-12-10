#! 1
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

print(min(my_dict.keys()) + max(my_dict.keys()))

# ! 2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]


names_end_with_8 = []
for d in users:
    for key, val in d.items():
        if key == "phone":
            if val[len(val) - 1] == "8": #int(val) % 10 == 8
                names_end_with_8.append(d['name'])

print(" ".join(sorted(names_end_with_8)))

# ! 3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

row_of_empty_email = []

for d in users:
    if d.get('email') == '':
        row_of_empty_email.append(d['name'])
    if d.get('email') == None:
        row_of_empty_email.append(d['name'])
print(" ".join(sorted(row_of_empty_email)))

# ! 4
dict_of_str_in_int = {
    "0" : 'zero',
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

number = int(input("ÐÐ²ÐµÐ´Ð¸ÑÐµ ÑÐ¸ÑÐ»Ð¾: "))
print(' '.join([dict_of_str_in_int[i] for i in str(number)]))

# ! 5
courses = {
    'CS101': {
        'ÐÐ¾Ð¼ÐµÑ Ð°ÑÐ´Ð¸ÑÐ¾ÑÐ¸Ð¸': 3004,
        'ÐÑÐµÐ¿Ð¾Ð´Ð°Ð²Ð°ÑÐµÐ»Ñ': 'Ð¥Ð°Ð¹Ð½Ñ',
        'ÐÑÐµÐ¼Ñ': '8:00'
    },
    'CS102': {
        'ÐÐ¾Ð¼ÐµÑ Ð°ÑÐ´Ð¸ÑÐ¾ÑÐ¸Ð¸': 4501,
        'ÐÑÐµÐ¿Ð¾Ð´Ð°Ð²Ð°ÑÐµÐ»Ñ': 'ÐÐ»ÑÐ²Ð°ÑÐ°Ð´Ð¾',
        'ÐÑÐµÐ¼Ñ': '9:00'
    },
    'CS103': {
        'ÐÐ¾Ð¼ÐµÑ Ð°ÑÐ´Ð¸ÑÐ¾ÑÐ¸Ð¸': 6755,
        'ÐÑÐµÐ¿Ð¾Ð´Ð°Ð²Ð°ÑÐµÐ»Ñ': 'Ð Ð¸Ñ',
        'ÐÑÐµÐ¼Ñ': '10:00'
    },
    'NT110': {
        'ÐÐ¾Ð¼ÐµÑ Ð°ÑÐ´Ð¸ÑÐ¾ÑÐ¸Ð¸': 1244,
        'ÐÑÐµÐ¿Ð¾Ð´Ð°Ð²Ð°ÑÐµÐ»Ñ': 'ÐÐµÑÐº',
        'ÐÑÐµÐ¼Ñ': '11:00'
    },
    'CM241': {
        'ÐÐ¾Ð¼ÐµÑ Ð°ÑÐ´Ð¸ÑÐ¾ÑÐ¸Ð¸': 1411,
        'ÐÑÐµÐ¿Ð¾Ð´Ð°Ð²Ð°ÑÐµÐ»Ñ': 'ÐÐ¸',
        'ÐÑÐµÐ¼Ñ': '13:00'
    }
}

course_key = input()

for keys in courses[course_key]:
    row = f"{course_key}: {courses[course_key]['ÐÐ¾Ð¼ÐµÑ Ð°ÑÐ´Ð¸ÑÐ¾ÑÐ¸Ð¸']}, {courses[course_key]["ÐÑÐµÐ¿Ð¾Ð´Ð°Ð²Ð°ÑÐµÐ»Ñ"]}, {courses[course_key]["ÐÑÐµÐ¼Ñ"]}"
print(row)

# ! 6
multi_tap_keyboard = {

    '.': '1',
    ',': '11',
    '?': '111',
    '!': '1111',
    ':': '11111',
    

    'A': '2',
    'B': '22',
    'C': '222',
    
  
    'D': '3',
    'E': '33',
    'F': '333',
    

    'G': '4',
    'H': '44',
    'I': '444',
    

    'J': '5',
    'K': '55',
    'L': '555',
    

    'M': '6',
    'N': '66',
    'O': '666',
    
   
    'P': '7',
    'Q': '77',
    'R': '777',
    'S': '7777',
    

    'T': '8',
    'U': '88',
    'V': '888',
    
   
    'W': '9',
    'X': '99',
    'Y': '999',
    'Z': '9999',
    
  
    ' ': '0'
}

row = input("ÐÐ²ÐµÐ´Ð¸ÑÐµ Ð¿ÑÐµÐ´Ð»Ð¾Ð¶ÐµÐ½Ð¸Ðµ: ")
new_row_of_numbers = []
for i in row.upper():
    if multi_tap_keyboard.get(i) != None:
        new_row_of_numbers.append(multi_tap_keyboard[i])
print("".join(new_row_of_numbers))

# ! 7
encoding_dictionary = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

row = input("ÐÐ²ÐµÐ´Ð¸ÑÐµ Ð¿ÑÐµÐ´Ð»Ð¾Ð¶ÐµÐ½Ð¸Ðµ: ")
new_row = []
for el in row.upper():
    new_row.append(encoding_dictionary[el])
print("".join(new_row))

# ! 8 
result = {x: x**2 for x in range(11,16)}

# ! 9
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230} 

dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666} 

 
result = {}
result.update(dict1)

for key, value in dict2.items():
    if key in result:
        result[key] += value

# ! 10
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff' 

result = {}

for char in text:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

# ! 11
def seen_words(s):
    dict_of_words = {}
    
    for i in sorted(s.split()):
        if i in dict_of_words:
            dict_of_words[i] += 1
        else:
            dict_of_words[i] = 1
    return max(dict_of_words.items(), key = lambda x: x[1])
        



s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley' 

# ! 12
pets = [('Hatiko', 'Parker', 'Wilson', 50), 

        ('Rusty', 'Josh', 'King', 25), 

        ('Fido', 'John', 'Smith', 28), 

        ('Butch', 'Jake', 'Smirnoff', 18), 

        ('Odi', 'Emma', 'Wright', 18), 

        ('Balto', 'Josh', 'King', 25), 

        ('Barry', 'Josh', 'King', 25), 

        ('Snape', 'Hannah', 'Taylor', 40), 

        ('Horry', 'Martha', 'Robinson', 73), 

        ('Giro', 'Alex', 'Martinez', 65), 

        ('Zooma', 'Simon', 'Nevel', 32), 

        ('Lassie', 'Josh', 'King', 25), 

        ('Chase', 'Martha', 'Robinson', 73), 

        ('Ace', 'Martha', 'Williams', 38), 

        ('Rocky', 'Simon', 'Nevel', 32)] 

 

result = {}
for tup in pets:
    key = (tup[1], tup[2], tup[3])
    value_to_add = tup[0]

    if key in result:
        result[key].append(value_to_add)
    else:
        result[key] = [value_to_add]

# ! 13
from collections import Counter

sen = input()
c = Counter(sorted(sen.lower().split()))
most_rare_word = min(c.items(), key = lambda x: x[1] )
print(most_rare_word)

# ! 14 
def fix_identifiers(input_string):
    identifiers = input_string.split()
    seen = {}
    result = []

    for ident in identifiers:
        if ident not in seen:
            seen[ident] = 0
            result.append(ident)
        else:
            seen[ident] += 1
            result.append(f"{ident}_{seen[ident]}")

    return ' '.join(result)
