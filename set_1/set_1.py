from utils import Utils

class Set1:
    def __init__(self):
        self.__utils = Utils()
        self.__run()

    def __challenge_1(self):
        print('===== Set 1 - Challenge 1 =====')
        phrase_1_1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        print(self.__utils.hex_to_base64(phrase_1_1))

    def __challenge_2(self):
        print('===== Set 1 - Challenge 2 =====')
        hex_str_1 = "1c0111001f010100061a024b53535009181c"
        hex_str_2 = "686974207468652062756c6c277320657965"
        print(self.__utils.xor_hex_operation(hex_str_1, hex_str_2))

    def __challenge_3(self):
        print('===== Set 1 - Challenge 3 =====')
        word_challenge_3 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        word_scores = {}
        # all extended ascii characters
        for hex_number in range(0, 256):
            # key must be the same size as word_challenge_3
            key = self.__utils.fill_hex_key_by_size(f'{hex_number:02d}', len(word_challenge_3))
            xor_result = self.__utils.xor_hex_operation(word_challenge_3, key)
            plain_text = self.__utils.hex_to_plain_text(xor_result)
            word_scores[plain_text] = self.__utils.english_word_score(plain_text)

        print(max(word_scores, key=word_scores.get))

    def __run(self):
        self.__challenge_1()
        self.__challenge_2()
        self.__challenge_3()

