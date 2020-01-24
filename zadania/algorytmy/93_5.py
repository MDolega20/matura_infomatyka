
def ciag_fibonnaciego(n,s):
    return 1 if n < 3 else ciag_fibonnaciego(n - 2, s+1)+ciag_fibonnaciego(n-1, s+1)

print(ciag_fibonnaciego(40,1))