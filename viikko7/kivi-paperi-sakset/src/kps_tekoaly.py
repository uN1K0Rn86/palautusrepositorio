from kps import KiviPaperiSakset
from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = Tekoaly()
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
