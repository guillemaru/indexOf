class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        else:
            hl = len(haystack)
            nl = len(needle)
            for x in range(hl):
                    if needle[0]==haystack[x]:
                        if nl==1:
                            return x
                        else:
                            #check starts
                            check=True
                            for y in range(nl-1):
                            	check = (needle[y+1]==haystack[x+1])
                            if check:
                                return x
            return -1
                                    
                    
                
def main():
    haystack = "hello"
    needle = "ll"
    solution = Solution()
    print("haystack is " + str(haystack) + "; needle is " + str(needle) + "; solution is " + str(solution.strStr(haystack, needle)))
    haystack = "aaaasfafnjllaaa"
    print("haystack is " + str(haystack) + "; needle is " + str(needle) + "; solution is " + str(solution.strStr(haystack, needle)))
    haystack = "aaaaaaaaaaa"
    print("haystack is " + str(haystack) + "; needle is " + str(needle) + "; solution is " + str(solution.strStr(haystack, needle)))
    
    
if __name__ == '__main__':
    	main()
	
	
'''
Output is

haystack is hello; needle is ll; solution is 2
haystack is aaaasfafnjllaaa; needle is ll; solution is 10
haystack is aaaaaaaaaaa; needle is ll; solution is -1

'''
