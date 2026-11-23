import networkx as nx

from database.DAO import DAO
class Model:
    def __init__(self):
        self.lista_luoghi = None
        self.dizionario_luoghi = {}
        self.lista_sentieri = None
        self.grafo = None

    def get_luoghi(self):
        # Leggo i luoghi dal DAO, se non già letti
        if self.lista_luoghi is None:
            self.lista_luoghi = DAO.read_all_luoghi()
        # Mi costruisco anche il dizionario, non si sa mai
        for luogo in self.lista_luoghi:
            self.dizionario_luoghi[luogo.id] = luogo
        # Poi restituisco la lista, letta ora o in precedenza
        return self.lista_luoghi


    def get_sentieri(self):
        # Leggo i sentieri dal DAO, se non già letti
        if self.lista_sentieri is None:
            self.lista_sentieri = DAO.read_all_sentieri()
        # Poi restituisco la lista, letta ora o in precedenza
        return self.lista_sentieri

    def crea_grafo(self):
        # Se la variabile grafo non è ancora stata dichiarata, la dichiaro
        if self.grafo is None:
            self.grafo = nx.Graph() # Mi creo il grafo vuoto
        # Se il grafo è ancora stato popolato esco
        if self.grafo.number_of_nodes()>0:
            return
        # Se sono qui il grafo deve ancora essere popolato di nodi, e poi archi

        nodi = self.get_luoghi()
        #self.grafo.add_nodes_from(nodi)
        for n in nodi:
            self.grafo.add_node(n)

        # Aggiungo gli archi con 600 x 600 query (lentissimo)
        """
        for u in nodi:
            for v in nodi:
                if len(DAO.check_if_u_and_v_connected(u.id, v.id)):
                    #Aggiungo un arco tra u e v
                    #print(f"Aggiungo arco tra {u.id} e {v.id}")
                    self.grafo.add_edge(u, v)
        """

        # Aggiungo gli archi con 600 query per estrarre i vicini dei nodi
        """
        for u in nodi:
            # La query mi restituisce gli id dei nodi vicini
            id_vicini = DAO.read_all_vicini(u.id)
            for id_v in id_vicini:
                v = self.dizionario_luoghi[id_v] # Ottengo il vicino dall'id
                self.grafo.add_edge(u, v)
        """

        # Aggiungo gli archi con una query soltanto con la quale ottengo tutti i sentieri in un colpo solo
        # sentieri = DAO.read_all_sentieri()
        sentieri = self.get_sentieri()
        for sentiero in sentieri:
            # Per poter costruire il lato mi servono dei luoghi u e v
            u = self.dizionario_luoghi[sentiero.id_luogo_1] # li ottengo dal dizionario dei luoghi per id
            v = self.dizionario_luoghi[sentiero.id_luogo_2]
            self.grafo.add_edge(u, v)


