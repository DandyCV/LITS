import re

match = 'Lorem123'
string = '''Both patterns and strings to be searched \ can be Unicode strings (str) as well as 8-bit strings (bytes). (x64)
However, Unicode strings and 8-bit strings cannot be mixed: that is, you \ cannot match a Unicode string with a byte pattern or vice-versa;
 similarly, when asking for a substitution, the (x86 or x64) replacement string must be of the same type as both the pattern and the search string.'''

# result = re.match(r'.+', string) #Повертає об'єкт. Виконує пошук на початку рядка.
# result =  re.search(r's{2}', string)   #Шукає перше співпадіння у тексті
# result = re.findall(r'^[bB]', string)  #повертає усі співпадіння
# result = re.split(r'\\', string)    #розбиває по символу(спеціальні символи треба екранувати)
# result = re.sub(r'\s', '!', string)  #замінює патерн1 патерн2
pattern = re.compile(r'\(x\d{2}\s?(or)?\s(x\d{2})?\)')  #компілює шаблон для патерна
# print(result).group(), result.start(), result.end()
result = pattern.findall(string)
print(result)

number1 = '+380666603616'
number2 = '0666603516'

pattern = re.compile(r'(\+38)*[0][0-9]{9}')
print(
    pattern.match(number1).group(),
    pattern.match(number2).group()
)