#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/


import bs4 as bs
import urllib.request

class Beautiful:
    def obtenerInformacion(self, url:str, etiqueta:str) ->str:
        self.url = url
        self.etiqueta = etiqueta
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        for titulo in soup.find_all(f"{etiqueta}"):
            print(titulo.string)
            return titulo.string





#print(soup.title)

#print(soup.title.name)

#print(soup.title.string)

