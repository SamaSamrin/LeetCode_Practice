def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in s:
            if s.count(i)==1 and s.find(i)!=-1:
                return s.find(i)
        return -1
      
  """
  Runtime: 9544 ms	
  Memory: 13.8 MB
  """
