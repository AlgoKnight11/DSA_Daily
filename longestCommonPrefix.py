def longestCommonPrefix( strs):
    output=strs[0]
    for i in range(1,len(strs)):
        while strs[i].startswith(output)==False:
            output=output[:len(output)-1]
            if output=="":
                break
    return output
print(longestCommonPrefix(["flower","flow","flight"]))