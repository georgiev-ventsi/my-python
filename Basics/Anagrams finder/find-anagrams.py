def find_anagrams(str1, str2):
    sorted_lower_str1 = sorted(str1.lower())
    sorted_lower_str2 = sorted(str2.lower())
    print(sorted_lower_str1, sorted_lower_str2)

    if len(sorted_lower_str1) == len(sorted_lower_str2):
        if sorted_lower_str1 == sorted_lower_str2:
            print('These two strings are anagrams')
        else:
            print('These two strings are not anagrams')
    else:
        print('These two strings are not anagrams')

find_anagrams('HIVes', 'Menhit')
find_anagrams('HIVes', 'Eshiv')
find_anagrams('HIVes', 'Eshivs')