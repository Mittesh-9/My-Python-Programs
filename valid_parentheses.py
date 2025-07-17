def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        chars = ['(', ')', '{', '}', '[', ']']
        
        # first solution to just simply check
        '''for i in range(len(s)):
                if s[0] == "(" and s[-1] == ")":
                        print(True)
                        break
        else:
                print(False)'''

        # second solution to check if the first and last characters are brackets
        found_chars = [char for char in chars if char in s]
        print("Found brackets:", found_chars)
        if found_chars[0] == '(' and found_chars[1] == ')':
                return True
        else:
                return False

        # leetcode accepted solution
        '''def isValid(self, s):
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0'''

# s = "()" # true
# s = "([])" # true
# s = "()[]{}" # true
# s = "(]" # false

is_valid = isValid("([)]")