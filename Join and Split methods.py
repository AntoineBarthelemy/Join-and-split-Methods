def raccourci (Numbers : float ) -> str:
    """Fonction permettant de conserver la partie entière et la partie décimal au millième près"""

    if isinstance(Numbers, int):
        print("Votre valeur est un entier, un flottant est demandé")
        # Ici, return permet de dire Ok c'est fini, on arrete là, car il est utilisé seule, donc il ne renvoie RIEN, il sert juste à sortir
        return 

    # Conversion en chaine de caractères 
    Numbers = str(Numbers)

    # Conversion en list
    Numbers = Numbers.split(".")

    # Tuple Unpacking (étalement des deux objects de la liste dans les deux variables)
    partie_entiere, partie_decimal = Numbers
    
    # partie_entiere, partie_decimal étant devenu des str on les repasse en tant que List pour pouvoir mettre plusieurs arguments dans la fonction join
    return ",".join([partie_entiere, partie_decimal[0:3]])
    
    
   
  
print(raccourci(1))

