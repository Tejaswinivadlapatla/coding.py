class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if (flag==False) and ((a>=0 and b<0) or (a<0 and b>=0)):
            return True
        elif (flag == True) and (a<0 and b<0):
            return True
        else:
            return False