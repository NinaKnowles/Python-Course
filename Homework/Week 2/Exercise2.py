def letter_count():
    output=0
    word=str(input('Enter a word').lower())
    letter=str(input('Enter a letter').lower())
    for val in word:
        if val==letter:
            output=output+1
        else:
            continue
    print(f'The entered letter appears in the word {output} times')

letter_count()


