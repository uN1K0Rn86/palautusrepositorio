HINTA = 5


class Kassapaate:
    def __init__(self):
        self.__myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        kortti.lataa(summa)

    def osta_lounas(self, kortti):
        if kortti.saldo() >= HINTA:
            kortti.osta(HINTA)
        else:
            return
        self.__myytyja_lounaita = self.__myytyja_lounaita + 1
