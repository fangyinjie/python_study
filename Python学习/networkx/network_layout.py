
# 需要导入模块: import networkx [as 别名]
# 或者: from networkx import spectral_layout [as 别名]
def test_smoke_int(self):
        G = self.Gi
        vpos = nx.random_layout(G)
        vpos = nx.circular_layout(G)
        vpos = nx.planar_layout(G)
        vpos = nx.spring_layout(G)
        vpos = nx.fruchterman_reingold_layout(G)
        vpos = nx.fruchterman_reingold_layout(self.bigG)
        vpos = nx.spectral_layout(G)
        vpos = nx.spectral_layout(G.to_directed())
        vpos = nx.spectral_layout(self.bigG)
        vpos = nx.spectral_layout(self.bigG.to_directed())
        vpos = nx.shell_layout(G)
        if self.scipy is not None:
            vpos = nx.kamada_kawai_layout(G)
            vpos = nx.kamada_kawai_layout(G, dim=1)