def findFirstIdenticalElements(Input):

    answer_string = ""
    answer_array = []

    for i, i_string in enumerate(Input): #iterate through every element
        j = i+1
        while(j < len(Input)): #compare with every element after it
            if(i_string.lower() == Input[j].lower()): 
                answer_string = i_string #if found an identical element, set that element as answer
                break
            j += 1
    if answer_string: #if answer is found, find everything identical to answer
        for i, i_string in enumerate(Input):
            if(answer_string.lower() == i_string.lower()):
                #di soal dikatakan tidak boleh menggunakan function komputasi array
                #tapi sy menggunakan fungsi append hanya utk menyimpan jawaban utk direturn
                #I assume this is allowed
                answer_array.append(i) 
        return(answer_array)
    else:
        return False

print(findFirstIdenticalElements(["4", "abcd", "acbd", "aaab", "acbd"]))
