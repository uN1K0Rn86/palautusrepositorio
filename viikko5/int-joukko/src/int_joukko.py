KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                kopio = self.ljono
                self.kopioi_lista(self.ljono, kopio)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(kopio, self.ljono)

            return True

        return False

    def poista(self, n):
        if n not in self.ljono:
            return False
        
        indeksi = self.ljono.index(n)
        self.ljono[indeksi] = 0

        for i in range(indeksi, self.alkioiden_lkm - 1):
            temp = self.ljono[i]
            self.ljono[i] = self.ljono[i + 1]
            self.ljono[i + 1] = temp

        self.alkioiden_lkm -= 1
        
        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()

        for i in range(0, a.alkioiden_lkm):
            x.lisaa(a.ljono[i])

        for i in range(0, b.alkioiden_lkm):
            x.lisaa(b.ljono[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()

        for i in range(0, a.alkioiden_lkm):
            for j in range(0, b.alkioiden_lkm):
                if a.ljono[i] == b.ljono[j]:
                    y.lisaa(b.ljono[j])
                    break

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()

        for i in range(0, a.alkioiden_lkm):
            z.lisaa(a.ljono[i])

        for i in range(0, b.alkioiden_lkm):
            z.poista(b.ljono[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i])
                tuotos += ", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1])
            tuotos += "}"
            return tuotos
