import base64
import codecs
import string


class Utils:
    @staticmethod
    def hex_to_base64(hex_str:str):
        return base64.b64encode(bytes.fromhex(hex_str)).decode()

    @staticmethod
    def fill_hex_key_by_size(hex_key: str, size: int):
        hex_key = hex_key * (size // len(hex_key) + 1)
        return hex_key[:size]

    @staticmethod
    def hex_to_plain_text(hex_str: str):
        try:
            plaint_text = bytes.fromhex(hex_str).decode('utf-8')
        except UnicodeDecodeError:
            try:
                plaint_text = bytes.fromhex(hex_str).decode('utf-16')
            except UnicodeDecodeError:
                print(f"Decoding hex into str -> {hex_str} failed for both UTF-8 and UTF-16")
                plaint_text = None

        return plaint_text

    def xor_hex_operation(self, hex_str_1:str, hex_str_2:str):
        if len(hex_str_1) != len(hex_str_2):
            print("The length of both strings should be equal. Updated automatically")
            hex_str_2 = self.fill_hex_key_by_size(hex_str_2, len(hex_str_1))

        return bytes([a ^ b for a, b in zip(bytes.fromhex(hex_str_1), bytes.fromhex(hex_str_2))]).hex()

    def challenge_3(self, hex_str:str):
        for hex_number in range(0,256):
            key = self.fill_hex_key_by_size(f'{hex_number:02d}', len(hex_str))
            xor_result = self.xor_hex_operation(hex_str, key)
            print(xor_result)
            print(self.hex_to_plain_text(xor_result))
            print(f"--------------------- DONE {hex_number} ---------------------")

        return None