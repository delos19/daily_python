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
    'z' : '--..'
    }

dot = 0
dash = 0

word_list = open('list.txt')

for row in word_list:
    for letter in row:
        morse_eq = dictionary.get(letter)
        dash += str(morse_eq).count('-')
        dot += str(morse_eq).count('.')

print('There are {} dashes'.format(dash))
print('There are {} dots'.format(dot))

