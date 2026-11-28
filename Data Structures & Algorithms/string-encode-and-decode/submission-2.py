class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        What is to stop me from putting them in a
        csv string? Probably nothing but that isn't very 'clever'.

        Ahhh. The comma (',') is a valid ASCII character.

        Hint 1: Use a non-ASCII character as a delimter. Apparently
        there is a better way. Hahaha I was too clueless to realise that the comma
        is an ASCII character - I will skip this one.

        Hint 2: Encode and decode the strings using a smart approach based
        on the lengths of each string. How to differentiate between the
        lengths and any numbers that might be present in the strings?

            When thinking of encoding and decoding I think of the python
            hashlib. But is this too much? hashlib can't decode anyway.
            Abandoning this idea.

            Okay I've spent too long. Going for Hint 3 and if I can't 
            figure it out I will watch the video.
        
        Hint 3: f"{len(string)}{string}#" But # is an ASCII character.

        Video: I had the Hint 3 wrong. It is f"{len(string)}#{string}"
        """
        encoded_str: str = ""
        
        # # First attempt:
        # for string in strs[:-1]:
        #     encoded_str += f"{string},"

        # # Make sure there is no comma after the last string
        # encoded_str += strs[-1]

        # # Second attempt - after Hint 3 (the solution)
        # for s in strs:
        #     encoded_str += f"{len(s)}{s}#"

        # Third attempt
        for s in strs:
            encoded_str += f"{len(s)}#{s}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        """
        Attempt 1: Now we just need to split the strings into a list.

        Attempt 2: The string starts off with a number n. We then get the next 
        n chars and append that to the list.

        Attempt 3: After watching half of the solution video
        """
        # # First attempt
        # return s.split(",")

        decoded_list: List[str] = []

        # Second Attempt
        # # First word
        # i = 0
        # len_i_word = int(s[i])
        # len_word_sep = s[i:i+len_i_word+2]
        # decoded_list.append(len_word_sep[1:-1])

        # # Second Word
        # i += len(len_word_sep)
        # len_i_word = int(s[i])
        # len_word_sep = s[i:i+len_i_word+2]
        # decoded_list.append(len_word_sep[1:-1])

        # i = 0
        # while i < len(s):
        #     len_i_word = int(s[i])
        #     enc_word = s[i:i+len_i_word+2]
        #     decoded_list.append(enc_word[1:-1])
        #     i += len(enc_word)

        # Third attempt
        i = 0
        while i < len(s):
            delim_i = s.find('#', i)
            len_word = int(s[i:delim_i])
            len_enc = len(s[i:delim_i+1]) # Include the '#'
            len_enc_word = len_enc + len_word
            enc_word = s[i+len_enc:i+len_enc_word]
            decoded_list.append(enc_word)
            i += len_enc_word

        return decoded_list





