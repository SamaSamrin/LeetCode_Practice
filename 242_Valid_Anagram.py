def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>=len(t):
            for i in s:
                if s.count(i)!=t.count(i):
                    return False
            return True
        else:
            for i in t:
                if t.count(i)!=s.count(i):
                    return False
            return True
          
 """
 Runtime: 7247 ms	
 Memory: 14.1 MB
 """
