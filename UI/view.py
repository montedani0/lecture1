
import flet as ft


class View:
    def __init__(self,page):
        self._controller = None
        self._page = page
        self._page.title= "Tdp 2025- Software Gestionale"
        self._page.horizontal_alignment= "center" #questo vuol dire allinea tutto rispetto alla mezzaria
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self.update_page()


    def carica_interfaccia(self):
        #Prodotto
        self._txtInNomeP = ft.TextField(label="Nome prodotto", width=200)
        self._txtInPrezzo = ft.TextField(label="Prezzo", width=200)
        self._txtInQuantita = ft.TextField(label="Quantità", width=200)
        row1 = ft.Row(controls=[self._txtInNomeP,self._txtInPrezzo,self._txtInQuantita],
                      alignment=ft.MainAxisAlignment.CENTER)

        #Cliente
        self._txtInNomeC = ft.TextField(label="Nome cliente", width=200)
        self._txtInEmail = ft.TextField(label="E-mail", width=200)
        self._txtInCategoria = ft.TextField(label="Categoria", width=200)

        row2 = ft.Row(controls=[self._txtInNomeC,self._txtInEmail,self._txtInCategoria],
                      alignment=ft.MainAxisAlignment.CENTER)

        #Button

        self._btnAdd = ft.ElevatedButton(text="Aggiungi ordine",
                                         on_click= self._controller.add_ordine,
                                         width=200)
        self._btnGestisciOrdine = ft.ElevatedButton(text="Gestisci prox ordine",
                                         on_click= self._controller.gestisci_ordine,
                                         width=200)
        self._btnGestisciAllOrdini = ft.ElevatedButton(text="Gestisci tutti gli ordini",
                                         on_click= self._controller.gestisci_all_ordine,
                                         width=200)
        self._btnStampaInfo = ft.ElevatedButton(text="Stampa sommario",
                                         on_click= self._controller.stampa_sommario,
                                         width=200)

        row3 = ft.Row([self._btnAdd,self._btnGestisciOrdine,self._btnGestisciAllOrdini,self._btnStampaInfo],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView(expand=True)

        self._page.add(row1,row2, row3, self._lvOut)


    def set_controller(self, c):
        self._controller = c

    def update_page(self):
        self._page.update()