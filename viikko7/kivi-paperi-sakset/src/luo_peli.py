from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly()
    if tyyppi == 'c':
        return KPSParempiTekoaly()