class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Make everything lowercase and remove spaces/symbols
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean = clean + ch.lower()

        # Step 2: Reverse the clean string using a simple loop
        rev = ""
        for ch in clean:
            rev = ch + rev

        # Step 3: Check if both are equal
        if clean == rev:
            return True
        else:
            return False
