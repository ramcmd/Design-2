# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:46:19 2022

@author: 91886
"""
#TC: O(1)
#SC: O(n)
class MyHashSet(object):

    def __init__(self):
        self.bucketlen = 1000
        self.bucket = [None] * self.bucketlen

    def h1(self, key):
        return key%len(self.bucket)
    
    def h2(self, key):
        return key//self.bucketlen
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.bucket[self.h1(key)] and self.h1(key) == 0:
            self.bucket[self.h1(key)] = [False] * (self.bucketlen+1)
        elif not self.bucket[self.h1(key)]:
            self.bucket[self.h1(key)] = [False] * self.bucketlen
                    
        self.bucket[self.h1(key)][self.h2(key)] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
         """  
        if self.bucket[self.h1(key)] :
            self.bucket[self.h1(key)][self.h2(key)] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if self.bucket[self.h1(key)]:
            return self.bucket[self.h1(key)][self.h2(key)]
        else:
            return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)