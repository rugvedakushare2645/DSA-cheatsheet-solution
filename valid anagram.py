
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return sorted(s)==sorted(t)

        #using pure logic

        if len(s)!=len(t):
            return False

        count = [0]*26
        for i in range(len(s)):
            s_index = (ord(s[i]) - ord('a'))
            t_index = (ord(t[i]) - ord('a'))

            count[s_index]+=1
            count[t_index]-=1

        for value in count:
            if value !=0:
                return False

        return True
        
