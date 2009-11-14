fh = open('cipher1.txt', 'r')
values = map(lambda x: int(x), fh.read().split(','))

# key is 3 letters from a-z
key_length = 3
valid_chars = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]
clue_words = [' the ', ' and ', ' or ', ' but ', ' in ']

def guess_password(password='', key_length=3):
    if key_length > 0:
        for char in valid_chars:
            guess_password(password + char, key_length - 1)
    else:
        xored = []
        for i in xrange(len(values)):
            xored.append(chr(values[i] ^ ord(password[i % 3])))
        xored_text = ''.join(xored)
        matches = 0
        for clue_word in clue_words:
            if clue_word in xored_text:
                matches += 1
        if matches > 3:
            print password
            print xored_text[:100]
            print sum(map(lambda x: ord(x), xored))
            return

guess_password()
