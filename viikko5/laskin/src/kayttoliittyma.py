from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._historia = []

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote, self._historia),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote, self._historia),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote, self._historia),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote, self._historia) # ei ehkä tarvita täällä...
        }

    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except ValueError:
            return 0

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)


    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

class BinaariOperaatio:
    def __init__(self, sovelluslogiikka, syote, historia):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote
        self._historia = historia

class Summa(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, syote, historia):
        super().__init__(sovelluslogiikka, syote, historia)

    def suorita(self):
        self.arvo = self._syote()
        self._sovelluslogiikka.plus(self.arvo)
        self._historia.append(self)

    def kumoa(self):
        self._sovelluslogiikka.miinus(self.arvo)

class Erotus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, syote, historia):
        super().__init__(sovelluslogiikka, syote, historia)

    def suorita(self):
        self.arvo = self._syote()
        self._sovelluslogiikka.miinus(self.arvo)
        self._historia.append(self)

    def kumoa(self):
        self._sovelluslogiikka.plus(self.arvo)

class Nollaus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, syote, historia):
        super().__init__(sovelluslogiikka, syote, historia)

    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, syote, historia):
        super().__init__(sovelluslogiikka, syote, historia)

    def suorita(self):
        if self._historia:
            viimeisin = self._historia.pop()
            viimeisin.kumoa()