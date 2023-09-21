class Solution:
    def rotate(self, N, D):
        # code here
        bin_st=str(bin(N))[2:]
        bin_st="0"*(16-len(bin_st))+bin_st
        # print(bin_st)
        bin_st1=["0"]*16
        bin_st2=["0"]*16
        for i in range(16):
            bin_st1[(i+D)%16]=bin_st[i]
            bin_st2[(i+(16-D))%16]=bin_st[i]
            # bin_st1=bin_st[:(i+D)%16]+bin_st[i]+bin_st[((i+D)%16)+1:]
            # bin_st2=bin_st[:(i+D)%16]+bin_st[i]+bin_st[((i+D)%16)+1:]
        bin_right="".join(bin_st1)
        bin_left="".join(bin_st2)
        return [int(bin_left,base=2),int(bin_right,base=2)]