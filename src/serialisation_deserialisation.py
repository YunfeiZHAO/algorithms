""" Serialisation and deserialisation related questions """

class EncodeDecodeStr:
    """ https://neetcode.io/problems/string-encode-and-decode
        encode a list of string to a string and decode it back from the str
    """
    def encode(self, strs: list[str]) -> str:
        """ use str length and a end character """
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s
        return encoded

    def decode(self, s: str) -> list[str]:
        """ get str length first and then get the string """
        decoded = []
        prefix = ""
        n = len(s)
        i = 0
        while i < n:
            if s[i] == "#":
                # get the length of current word
                word_len = int(prefix)
                decoded.append(s[i + 1: i + 1 + word_len])
                i = i + 1 + word_len
                prefix = ""
            else:
                prefix += s[i]
                i += 1
        return decoded

        

        
