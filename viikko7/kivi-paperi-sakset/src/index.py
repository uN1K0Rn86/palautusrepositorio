from kps import KiviPaperiSakset
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from luo_peli import luo_peli


def main():
    while True:
        vastaus = input("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan: "
              )

        print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
        
        if vastaus in ["a", "b", "c"]:
            peli = luo_peli(vastaus)
            peli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
