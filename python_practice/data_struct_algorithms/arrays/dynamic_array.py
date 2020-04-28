import ctypes
import sys
class dynamic_array(object):

    def __init__(self):

        ##count
        ##
        self.n = 0
        ##one element by default
        ##
        self.capacity = 1
        ##makes makes array
        ##
        self.A = self.make_array(self.capacity)

    ##returns number of elements in array
    ##
    def __len__(self):
        return self.n

    ##return elements in index k
    ##
    def __getitem__(self, k):
        ##if k isn't in between 0 and count return error
        ##
        if not 0 <= k < self.n:
            return IndexError('K is out of Bounds!')
        return self.A[k]

    ##add element to end of array
    ##
    def append(self, ele):

        if self.n == self.capacity:
            ##2x if capcity isn't enough
            ##
            self._resize(2*self.capacity)
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):

        ##make new array size of new_cap
        ##
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capcity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()
