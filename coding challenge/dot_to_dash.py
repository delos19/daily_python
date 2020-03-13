dictionary = {
    'a' : '.-',
    'b' : '-..',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
    }

# Converts the letters to morse to be printed
test_word = input('Word to convert: \n')
morse_eq = ''

for letter in test_word:
    morse_eq += dictionary.get(letter)
print(morse_eq)

# Imports the list of words and totals the dots and dashes
dot = 0
dash = 0
word_list = open('list.txt')

for row in word_list:
    for letter in row:
        morse_eq = dictionary.get(letter) 
        dash += str(morse_eq).count('-')
        dot += str(morse_eq).count('.')
        count = str(morse_eq).count('-')
        if count > 15:
            print(row)
        

print('There are {} dashes'.format(dash))
print('There are {} dots'.format(dot))

