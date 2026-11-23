import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        self._model.crea_grafo()
        # Qui in self._model.grafo ho il grafo creato
        print(self._model.grafo)

        # Mostro le informazioni nella GUI
        self._view._lst_results.controls.clear()
        self._view._lst_results.controls.append(ft.Text(f"# nodi {len(self._model.grafo.nodes)}, #archi {len(self._model.grafo.edges)}"))

        self._view._lst_results.controls.append(ft.Text("********* Nodi *********"))
        for nodo in self._model.grafo.nodes:
            self._view._lst_results.controls.append(ft.Text(f"{nodo}"))

        self._view._lst_results.controls.append(ft.Text("\n********* Archi *********"))
        for arco in self._model.grafo.edges:
            self._view._lst_results.controls.append(ft.Text(f"{arco[0]} - {arco[1]}"))


        self._view.update_page()







    def handle_visita_ampiezza(self, e):
        pass

    def handle_visita_profondita(self, e):
        pass
