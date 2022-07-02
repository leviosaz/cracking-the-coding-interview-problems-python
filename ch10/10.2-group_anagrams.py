from collections import defaultdict

def groupAnagrams(words):
    # Basically dictionary with values of lists.
    dd = defaultdict(list)
    
    for word in words:
        base_word = "".join(sorted(word.lower()))
        dd[base_word].append(word)
        
    sorted_words = []
    for anagrams in dd.values():
        sorted_words.extend(anagrams)
    
    return sorted_words
        
print(groupAnagrams(["badis", "hey", "yeh", "carlsbad", "carl", "isbad", "badis"]))