from kps import KiviPaperiSakset
from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = TekoalyParannettu(10)
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")
        tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto
