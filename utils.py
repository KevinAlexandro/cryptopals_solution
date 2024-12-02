import base64
import codecs
import string


class Utils:
    @staticmethod
    def hex_to_base64(hex_str:str):
        # from hex to string
        # print(codecs.decode(hex_str, 'hex').decode())
        return base64.b64encode(bytes.fromhex(hex_str)).decode()

    @staticmethod
    def xor_hex_operation(hex_str_1:str, hex_str_2:str):
        assert len(hex_str_1) == len(hex_str_2), "The length of both strings should be equal"
        return format(int(hex_str_1, base=16) ^ int(hex_str_2, base=16), 'x')

    @staticmethod
    def generate_hex_str_by_size(hex_char:str, size:int):
        hex_word = ''
        # hex_char = f'{hex_char:02}'
        while len(hex_word)!=size:
            hex_word = f'{hex_word}{hex_char}'
        return hex_word

    def challenge_3(self, hex_str:str):

        size = len(hex_str)
        for i in range(0, 256):
            hex_char = format(i, 'x')
            print(hex_str)
            reverse_xor_result = self.xor_hex_operation(hex_str, self.generate_hex_str_by_size(hex_char, size))
            print(reverse_xor_result)
            try:
                print(codecs.decode(reverse_xor_result, 'hex'))
            except:
                pass
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        return None