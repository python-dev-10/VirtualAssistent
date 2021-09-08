#Aqui ficará a parte de pesquisas no navegador
import webbrowser
#Abre no navegador padrao, em uma nova aba, uma pesquisa no Google
def pesquisar_no_google(pesquisa):
    busca="https://www.google.com/search?q=" + pesquisa
    webbrowser.open_new_tab(busca)
    yield "Sua busca sobre" + pesquisa + "foi aberta no navegador"
#Abre no navegador padrao, em uma nova aba, uma pesquisa no Bing
def pesquisar_no_bing(pesquisa):
    busca="https://www.bing.com/search?q=" + pesquisa
    webbrowser.open_new_tab(busca)
    yield "Sua busca sobre" + pesquisa + "foi aberta no navegador"
#Abre no navegador padrao, em uma nova aba, uma pesquisa no Duckduckgo
def pesquisar_no_duckduckgo(pesquisa):
    busca="https://duckduckgo.com/?q=" + pesquisa
    webbrowser.open_new_tab(busca)
    yield "Sua busca sobre" + pesquisa + "foi aberta no navegador"
