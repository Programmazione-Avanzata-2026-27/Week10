import flet as ft

class View:
    def __init__(self, page):
        self._page = page
        self._page.title = "Sentieri - grafo e visite"
        self._page.scroll = ft.ScrollMode.AUTO
        self._controller = None
        self._dd_luogo = ft.Dropdown(label="Luogo di partenza", width=350, disabled = True)
        self._lst_results = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

    def set_controller(self, controller):
        self._controller = controller

    def load_interface(self):
        self._btn_va = ft.Button("Visita in ampiezza", on_click=self._controller.handle_visita_ampiezza, disabled=True)
        self._btn_vp = ft.Button("Visita in profondità", on_click=self._controller.handle_visita_profondita, disabled=True)

        self._page.add(
            ft.Text("Rete dei sentieri", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Costruisci il grafo, scegli un luogo e visita i luoghi raggiungibili."),
            ft.Row([ft.Button("Crea grafo", on_click=self._controller.handle_crea_grafo)],
                   wrap=True),
            ft.Row([self._dd_luogo,
                    self._btn_va,
                    self._btn_vp],
                   wrap=True),
            self._lst_results)

        self._controller.populate_dropdown(self._dd_luogo)

        self.update_page()

    def update_page(self):
        self._page.update()

    def alert(self, msg):
        self._page.open(ft.AlertDialog(title=ft.Text(msg)))