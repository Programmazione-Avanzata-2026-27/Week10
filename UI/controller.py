import flet as ft
import networkx as nx

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

        self._view._dd_luogo.disabled = False
        self._view._btn_va.disabled = False
        self._view._btn_vp.disabled = False

        self._view.update_page()


    def populate_dropdown(self, dd):
        luoghi = self._model.get_luoghi()
        for luogo in luoghi:
            dd.options.append(ft.dropdown.Option(key=luogo.id, text=luogo.nome))


    def handle_visita_ampiezza(self, e):

        id_luogo_selezionato = self._view._dd_luogo.value
        print(id_luogo_selezionato)
        if id_luogo_selezionato is None:
            self._view.alert("Seleziona una luogo")
            return

        luogo_sorgente = self._model.dizionario_luoghi[int(id_luogo_selezionato)]
        albero = nx.bfs_tree(self._model.grafo, luogo_sorgente)
        print(albero)

        # Mostro le informazioni nella GUI
        self._view._lst_results.controls.clear()
        self._view._lst_results.controls.append(ft.Text(f"# nodi {len(albero.nodes)}, #archi {len(albero.edges)}"))

        self._view._lst_results.controls.append(ft.Text("********* Nodi *********"))
        for nodo in albero.nodes:
            self._view._lst_results.controls.append(ft.Text(f"{nodo}"))

        self._view._lst_results.controls.append(ft.Text("\n********* Archi *********"))
        for arco in albero.edges:
            self._view._lst_results.controls.append(ft.Text(f"{arco[0]} - {arco[1]}"))

        self._view.update_page()


    def handle_visita_profondita(self, e):
        id_luogo_selezionato = self._view._dd_luogo.value
        print(id_luogo_selezionato)
        if id_luogo_selezionato is None:
            self._view.alert("Seleziona una luogo")
            return

        luogo_sorgente = self._model.dizionario_luoghi[int(id_luogo_selezionato)]
        albero = nx.dfs_tree(self._model.grafo, luogo_sorgente)
        print(albero)

