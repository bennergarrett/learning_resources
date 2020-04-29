
##s is input
##t is what s is tested against for anagram
def anagram(s, t):
    s=s.tolower().strip().replace(" ", "")
    print(s)





if __name__ == '__main__':

    anagram('dog', 'god')
