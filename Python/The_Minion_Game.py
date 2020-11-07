def minion_game(string):
    # your code goes here
    vowels=['A','E','I','O','U']
    words_vow=0
    words_cons=0
    for i in range(len(string)):
        if string[i] in vowels:
            words_vow+= len(string)-i
        else:
            words_cons+= len(string)-i
    if words_cons>words_vow:
        print('Stuart '+str(words_cons))
    elif words_cons==words_vow:
        print('Draw')
    else:
        print('Kevin '+str(words_vow))
            
