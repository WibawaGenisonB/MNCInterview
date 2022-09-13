def isValid(String):
    paranthesesMap = {">":"<",
    "}":"{",
    "]":"["}
    stack = []
    
    if len(String) < 1 or len(String) > 4096: #panjang string adalah 1 – 4096
        return False
    
    for i in String: #iterate through every element
        if i in paranthesesMap: #if tutup kurung
            #jika stack kosong dan diberi tutup kurung atau stack terakhir bukan pair dengan yang dibaca, false
            if stack and stack[-1] == paranthesesMap[i]: 
                stack.pop()
            else:
                return False
        else: #if buka kurung
            stack.append(i)

    #True if and only if stack is empty
    return True if not stack else False
    

    #input = string hanya mengandung <>{}[] akan terdeteksi oleh kode diatas karena hashmap hanya 3 entry

print(isValid("{{[<>[{{}}]]}}")) #True
print(isValid("[[{[[<{{{{[[[<[{[[<{{{{[{[{[[[<<{<{[{<<<[[<[{[<{{[{[<[[<<[{<<[[[{<[{[[{{<<>[<<{{<<{[[[<{}{[{{{[[{{[[<[{}]>]]}}]]}}}]}>]]]}>>}}>>]>}}]]}]>}]]]>>}]>>]]>]}]}}>]}]>]]>>>}]}>}>>]]]}]}]}}}}>]]}]>]]]}}}}>]]}]]")) #True
print(isValid(">}}]}]}]>>>>>>]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}")) #False