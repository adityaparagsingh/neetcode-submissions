class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "||".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("||")
        return decoded_strs
