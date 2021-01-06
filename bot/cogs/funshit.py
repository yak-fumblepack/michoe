def percent_isgay(args):
    gayletters = ["g","a","y","m","i","c","h","a","e","l","p","n","s","G","A","Y","M","I","C","H","A","E","L","P","N","S"]
    barelygayletters = ["x","u","r","w","z","j","k"]
    gayness = 0

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in gayletters:
            gayness += 5
        wordlen += 1

    wordlen = 0
    while wordlen < len(args):
        if args[wordlen] in barelygayletters:
            gayness += 0.4
        wordlen += 1

    return (args + " is " + str((gayness/len(args))*100) + "%% gay")


