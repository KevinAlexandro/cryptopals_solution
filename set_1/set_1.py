from utils import Utils

class Set1:
    def __init__(self):
        self.__utils = Utils()
        self.__run()

    def __challenge_1(self):
        # Set 1 - Challenge 1
        print('===== Set 1 - Challenge 1 =====')
        phrase_1_1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        print(self.__utils.hex_to_base64(phrase_1_1))

    def __challenge_2(self):
        # Set 1 - Challenge 2
        print('===== Set 1 - Challenge 2 =====')
        hex_str_1 = "1c0111001f010100061a024b53535009181c"
        hex_str_2 = "686974207468652062756c6c277320657965"
        print(self.__utils.xor_hex_operation(hex_str_1, hex_str_2))

    def __challenge_3(self):
        # Set 1 - Challenge 3
        print('===== Set 1 - Challenge 3 =====')
        word_challenge_3 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        self.__utils.challenge_3(word_challenge_3)

    def __run(self):
        self.__challenge_1()
        self.__challenge_2()
        self.__challenge_3()

