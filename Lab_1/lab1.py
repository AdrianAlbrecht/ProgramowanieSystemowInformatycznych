zad1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
       "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud " \
       "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure " \
       "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. " \
       "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit " \
       "anim id est laborum."

def zad2 (text, char1, char2):
    return text.count(char1), text.count(char2)

def zad3(text_1: str, text_2: float, text_3: int):
    print('{0} {2} {1}'.format(text_1, text_2, text_3))
    print('{:^40}'.format(text_1))
    print('{:1}'.format(text_1))
    print('{:4d}'.format(text_3))
    print('{:02.2f}'.format(text_2))

#Zad 4
# print(dir(zad1))
# help(zad1.center(10,"a"))

#Zad 5
letters = "Wojciechowski Bartosz"
letters.lower()
# print(letters[::-1].title())


# print(zad2(zad1,"a","b"))
# zad3("Ala",3.3333333,5)

#zad 6
lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[]
for i in range(5):
    lista2.append(lista1.pop(5))
# print(lista2)
# print(lista1)

#zad7
lista3=lista1+lista2
lista3.insert(0,0)
lista3kopia=lista3
lista3kopia.sort(reverse=True)
# print(lista3kopia)

#zad8
zad8=[["15555", "Ala Au"],["134323", "Olwk Krak"]]


#zad9
dic={}
for l2 in zad8:
    dic[l2[0]] = l2[1:]
# print(dic)

dic["134323"].append("123123123")
dic["134323"].append("a@email")
dic["134323"].append(20)

dic["15555"].append("122123123")
dic["15555"].append("ab@email")
dic["15555"].append(21)
# print(dic)

#zad10
numbers=[213,321,123,123,321,123,222,232,231,123]
# print(set(numbers))

#zad11
for i in range(1,11):
    print(i)

#zad12
for i in range(100,19,-5):
    print(i)

#zad13
ls = [dic, dic]
text = ""
for i in ls:
    text += str(i)
print(text)
