class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack
        '''
        use a stack to save the indices of (
            if ) is greater than ( -> remove )
        if the number of ( is greater
            - remove from the indices from stack
        '''
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        # (((
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)