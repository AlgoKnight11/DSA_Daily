def matchingStrings(stringList, queries):
    results=[]
    for i in queries:
        results.append(stringList.count(i))
    return results
print(matchingStrings(["abcde","sdaklfj","asdjf","na","basdn","sdaklfj","asdjf","na","asdjf","na","basdn","sdaklfj","asdjf"],["abcde","sdaklfj","asdjf","na","basdn"]))