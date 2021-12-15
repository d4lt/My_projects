


class Ceasar:

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, ciph) -> None:
        self.ciph = ciph
    
    def sort(self):
        
        alph_ciph = []

        for i in self.alpha:

            i  = self.alpha[self.alpha.index(i)+ 2 : self.alpha.index(i)+ 3]

            if i == 'y':
                i = 'a'
            elif i == 'z':
                i = 'b'
            alph_ciph.append(i)

        return alph_ciph
            

my_enc = Ceasar(2)

print(tuple(my_enc.sort()))


