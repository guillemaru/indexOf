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
	print("haystack is " + haystack + "; needle is " + needle + "solution is " + solution.strStr(haystack, needle))
  	haystack = "aaalaaallaaaa"
  	print("haystack is " + haystack + "; needle is " + needle + "solution is " + solution.strStr(haystack, needle))
  	haystack = "aaaaaaaa"
  	print("haystack is " + haystack + "; needle is " + needle + "solution is " + solution.strStr(haystack, needle))
if __name__ == '__main__':
    	main()
