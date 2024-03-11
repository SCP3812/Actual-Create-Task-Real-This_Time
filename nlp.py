import random 
     
#markov = input("Give your prompt here: ")

markov = "But beyond Wisu by the Sea of Darkness there lies a land known by the name of Yura. In summers the days are very long there, so that the Sun does not set for forty days, as the merchants say; but in winters the nights are equally long. The merchants report that Darkness is not far (from them), and that the people of Yura go there and enter it with torches, and find a huge tree there which is like a big village. But on top of the tree there sits a large creature, they say it is a bird. And they bring merchandise along, and each merchant sets down his goods apart from those of the others; and he makes a mark on them and leaves, but when he comes back, he finds commodities there, necessary for his own country"

def Markovian(markov): 
    markov_chain = {}
    markov_list = markov.split(" ")

    n=0
    while n < len(markov_list)-1:
        word = markov_list[n].lower().replace('\W+', "")
        if not word in markov_chain.keys():
            markov_chain[word] = []
        if markov_list[n+1]:
            markov_chain[word].append(markov_list[n+1])
        n = n + 1 
    words = list(markov_chain.keys())
    word = words[random.randint(0, len(words)-1)]
    result = ""

    for i in words:
        result = result + word + " "
        newWord = markov_chain[word][random.randint(0, len(markov_chain[word])-1)]
        word = newWord

        if not word or not word in markov_chain:
            word = words[random.randint(0, len(words)-1)]
    return result


print(Markovian(markov)) 
