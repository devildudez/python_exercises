""""
Упражнение 118. Словесные палиндромы
(34 строки)

В упражнениях 75 и 76 мы уже имели дело со словами, являющимися палиндромами.
Тогда мы анализировали буквы в слове с начала и конца, игнорируя пробелы
и знаки препинания, чтобы понять, совпадает ли его
написание в прямом и обратном направлениях.

И хотя палиндромами обычно называют слова, это понятие вполне можно расширить.
Например, английская фраза
«Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?»
является словесным палиндромом, поскольку если читать ее по словам,
игнорируя при этом знаки препинания и заглавные буквы, в обоих направлениях
она будет звучать одинаково.

Еще примеры английских словесных палиндромов:
«Herb the sage eats sage, the herb»
и
«Information school graduate seeks graduate school information».

Напишите программу, которая будет запрашивать строку у пользователя
и оповещать его о том, является ли она словесным палиндромом. Не
забывайте игнорировать знаки препинания при выявлении результата.
"""

def is_palendrome(stroka: str) -> bool:

    x=stroka.lower()
    x = x.replace(',', '')
    x = x.replace('?', '')
    x = x.replace('!', '')
    x = x.replace('.', '')
    x = x.replace('\n', ' ')

    print(x)
    x = x.split()
    print(x)

    if len(x) in (0 ,1):
        print("Its a palindrome")
        return True

    middle = len(x) // 2
    print(middle)

    print(x[0:middle])
    if len(x) % 2 == 0:
        second_delimiter = middle - 1
    else:
        second_delimiter = middle

    print(x[-1:second_delimiter:-1])

    if x[:middle] == x[-1:second_delimiter:-1]:
        print("Its a palindrome")
        return True
    else:
        print("It is not a palindrome")
        return False


if __name__ == '__main__':

    # s = input()
    # s = 'Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?'
    # is_palendrome(s)
    #
    # s = 'Herb the sage eats sage, the herb»'
    # is_palendrome(s)
    #
    # s = 'Information school graduate seeks graduate school information'
    # is_palendrome(s)
    #
    # s = 'mom'
    # is_palendrome(s)

    s = 'mom mom'
    is_palendrome(s)
