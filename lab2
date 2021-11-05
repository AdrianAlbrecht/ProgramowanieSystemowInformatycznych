import string
from file_manager import FileManager

def zad1(a_list, b_list):
    lista = []
    for i in a_list:
        if ((a_list.index(i)) % 2 == 0):
            lista.append(i)
    for i in b_list:
        if ((b_list.index(i)) % 2 == 1):
            lista.append(i)
    print(lista)
    return lista


# a_list = ["kappa", "kappa1", "kappa2", "kappa3", "kappa4"]
# b_list = ["kappa5", "kappa6", "kappa7", "kappa8", "kappa9"]
#
# zad1(a_list, b_list)

def zad2(data_text):
    word_dict = {}
    word_len = len(data_text)
    letters = []
    letters[:0] = data_text
    word_upper = data_text.upper()
    word_smaller = data_text.lower()

    word_dict['lenght'] = word_len
    word_dict['letters'] = letters
    word_dict['big_letters'] = word_upper
    word_dict['smaller_letters'] = word_smaller
    print(word_dict)
    return dict


# data_text="Kot"
# zad2(data_text)

def zad3(text, letter):
    replaced_text = text.replace(letter, "")
    print(replaced_text)
    return replaced_text


# zad3("Wyrewolwerowany rewolwerowiec",'r')

def zad4():
    print("Wybierz jednostkę którą chcesz otrzymać:")
    x = input("1:Kelwin, 2:Rankine, 3:Fahrenheit ")
    lista = ["1", "2", "3"]
    if (x not in lista):
        print("podałeś złą wartość")
    else:
        y = input("Podaj stopnie: ")
        if str(x) == "1":
            stopnie_K = int(y) + 273.15
            print("Kelwina " + str(stopnie_K))
        elif str(x) == "2":
            stopnie_R = (int(y) + 273.15) * 1.8
            print("Rankine " + str(stopnie_R))
        elif str(x) == "3":
            stopnie_F = ((int(y) * 2) + 32) * 0.9
            print("Fahrenheita " + str(stopnie_F))


# zad4()

class calculator:
    def add(x, y):
        result=x+y
        return result
    def difference(x, y):
        result=x-y
        return result
    def multiply(x, y):
        result=x*y
        return result
    def divide(x, y):
        result=x/y
        return result

class ScienceCalculator(calculator):
    def pow(x,y):
        result=pow(x,y)
        return result

def zad7(x):
    print((x[::-1]))

# zad7("kappa")
FileManager.update_file("test.txt")
FileManager.read_file("test.txt")