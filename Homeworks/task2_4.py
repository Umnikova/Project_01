# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


def remove_exclamation_marks(s):
    s_result = ""
    for i in range(0, len(s)):
        
        if s[i] != '!':
         s_result = s_result + s[i]
    print(f'{s} --> "{s_result}"')

remove_exclamation_marks('За!да!ние! вы!пол!не!но!')

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    n = len(s)
    s_result = ""
    for i in range(0, n):
        if s[-1] == '!':
            s_result = s[: n-1]
        elif s[-1] != '!':
            s_result = s[::]
    print(f'{s} --> "{s_result}"')

remove_last_em("Hi! Hello!!!")

#Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
    
def remove_word_with_one_em(s):
    s_list = s.split()
    s_list_clean = []
    for i in range(len(s_list)):
        count = 1
        if count != s_list[i].count('!'):
            s_list_clean.append(s_list[i])
    print(f'"{s}" --> "{" ".join(s_list_clean)}"')

remove_word_with_one_em("Hi! !Hi! Hi!")



