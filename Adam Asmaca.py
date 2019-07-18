try:
    while True:

        word = "EMRAH"
        correct_guesses = []
        wrong_guesses = []
        attempts = 0
        figures= ["""
             |+---+
             | 
             |
             |
             |
             |
        --------""", """
           +---+
            |  |  
            |  O
            |
            |
        --------""", """
           +---+
           |   |
           |   O
           |   |
           |
           |
        --------""", """
           +---+
           |   |
           |   O
           |   |\
           |
           |
        --------""", """
           +---+
           |   |
           |   0
           |  /|\
           |
           |
        --------""", """
           +---+
           |   |
           |   O
           |  /|\
           |   |
           |
        --------""", """
           +---+
           |   |
           |  _O_
           |  /|\
           |   |
           |
        --------"""]
        # ATTEMPT SAYISI 6 DAN KUCUK OLDUKCA LOOP U DONDUR
        while attempts < 6 :
            #FIGURES DA 7 TANE  FIGUR VAR. ATTEMT SAYISISINA GORE FIGURE U PRINTLIYOR.
            # 3. ATTEMT DE 3. FIGURE U VERIYOR >>> figures[2] 3.figur
            print(figures[attempts])


            ####  shown_letters I OLUSTUR ###

            #shown letteri tanimliyoruz. empty string olarak
            shown_letters = ""

            # word deki herbir harf icin ayri loop yap
            for harf in word:
                # eger loop daki harf, dogru tahminlerde bulunuyorsa, harf i shown_letters a ekle, eger yoksa _
                if harf in correct_guesses:
                    shown_letters = shown_letters+harf
                else:
                    shown_letters = shown_letters + " _ "

            #shown_letters i ilk burada printliyoruz
            print("Guess a letter", shown_letters)
            # KALAN ATTEMPT SAYISINI PRINTLE
            print(6-attempts, " guesses left. ")




            guess = input(" Enter a capital letter : ")


            # eger guess , correct_guesses ya da wrong_guesses bulunuyorsa bu mesaji printle
            # bu demektir ki bu harf daha once tahmin olarak zaten bi kere girilmis
            if guess in correct_guesses or guess in wrong_guesses:
                print("{} this letter was used, try another letter ".format(guess))


            # eger guess kelimenin icinde bi harf se  burayi printle   dogru bildini
            # ve bu harfi correct_guesses e ekle   append et
            elif guess in word:
                print(" You found it ! ")
                correct_guesses.append(guess)

            # eger dogru tahmin degilse,  yanlis prinitini printle
            # ve bu yanlis tahmin i   wrong_guesses e ekle , append et
            # ve attemts i 1 arttir   NOTE  attemts sadece bu durumda artiyor, yukaridakiler icin arttirilmiyor
            else:
                print(" The word does not consist this letter!")
                wrong_guesses.append(guess)
                attempts = attempts+1


        print("You lost the game... ! \nKelime : ",word)
        break



except ValueError:
    print("Pls be careful about the instructions !")

except type:
    print("Pls be careful about the instructions  !")
