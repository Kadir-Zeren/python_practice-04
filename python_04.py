fruit = 'Orange'
print( 'Word :', fruit)
print('First letter:', fruit[0])
print('Second letter:', fruit[1])
print("3rd to 5th letters:", fruit[2:5])
print("Letter all after 3rd:" , fruit[2:])

text = 'Clarusway'
text[3]
text[4:7]
text[6:]
text[0:6]
text[:6]

city = 'Phoenix'
print(city[1:])# starts from index 1 to the end
print (city [ :6])# starts from zero to 5th index
print (city[ : : 2]) # starts from zero to end by 2 step
print(city[1 :: 2])# starts from index 1 to the end by 2 step
print(city[-3:])# starts from index -3 to the end
print(city[ ::- 1]) # negative step starts from the end to zero

text = 'abcdefghi'
text[1:8]
text[1:8:2]
text[1::3]
text[: : 2]
text[5:1]
text[5:1:-1]
text[5:1:-2]
text[ ::- 1]

text= 'kayak'
text == text[ ::- 1] 
yeni_text = 'abcdef'
yeni_text == yeni_text[ ::- 1]
text = 'Clarusway'
text [8] == text[-1]

animal = "hippopotamus"
print(animal[1:])
print (animal [ :6])
print(animal[ :: 2])
print(animal[1:7:2])
print(animal[-3:])
print(animal[ ::- 1])

vegetable = "Tomato"
print( 'length of the word', vegetable, 'is : ', len(vegetable))

text[ :4] + text[-3:]
text[ :5] + "k" + text[-3:]
text[ : 5] + 'k' + text[6:]
text[0]+text[len(text)//2] + text[-1]
len(text)
len(text)/2
len(text)//2

ilk = text[0]
son = text[-1]
orta = text[len(text)//2]
ilk + orta + son

str_one = 'upper'
str_two = 'case'
str_comb = str_one + str_two
print ('upper' + 'case')
print(str_one + str_two)
print(str_comb)

str_one = 'upper'
str_two = 3 * 'upper'
str_comb = str_one * 3
print(str_two)
print(str_comb)
print(* str_one)

string_1 = 'I am angry ... '
string_2 = '1453'
'joseph@clarusway.com' # Do not use variable

string_1 = 'I am angry ... '
print(* string_1)
string_2 = '1453'
print(* string_2)
'joseph@clarusway . com' # Do not use variable
print(* 'joseph@clarusway.com')

str_one = 'upper'
str_one += 'case'
print(str_one)
str_one += 'letter'
print(str_one)
str_one += 'end'
print(str_one)

fruit = 'Orange'
vegetable = 'Tomato'
amount = 4
print('The amount of {} we bought is {} pounds' . format(fruit, amount))

name = 'Yasin'
age = 43
meslek = 'Content Creator'
print('Merhaba, ismin {} yasin {} meslegin ise {}'.format(name, age, meslek))

print('{state} is the most {adjective} state of the {country}' . format(state='California',country='USA' , adjective=' crowded' ))

print("{}-{}-{}".format("12", "Feb", "Feb"))
print("{no}-{month}-{month}" .format(no="12", month="Feb"))
print("{6} {5} {0} {1} {3} {4} {2}". format("a new", "job", "months", "in", 6, "have started", "I will"))

name = 'Ali'
age = 43
meslek = 'Content Creator'
print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}')

fruit = 'Orange'
vegetable = 'Tomato'
amount = 6
output = f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds"
print(output)

sample = f"{2 ** 3}"
print(sample)

name = "MARIAM"
print(F'My name is {name. capitalize()}')