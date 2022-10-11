from gc import callbacks
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from clasificadosLaVoz.items import ClasificadoslavozItem
from scrapy.linkextractors import LinkExtractor


class LaVozSpider(CrawlSpider):
    name = 'laVoz'
    start_urls = ['https://empleos.clasificadoslavoz.com.ar/buscar?page=1&key=Buscar+por+palabras+clave&rubro=0&zona=596&buscar=buscar']
    
    
    rules = (
            Rule(LinkExtractor(allow='buscar', deny='aviso')),
            Rule(LinkExtractor(allow='aviso'), callback='parseJob')
    )
    
          
    def parseAll(self,response):

        for link in response.css('div.datos h2 a::attr(href)'):
            yield response.follow(link.get(),callback=self.parseJob)
    
    def parseJob(self, response):
        
        items = ClasificadoslavozItem()
        try:
                    
            items['titulo'] = response.css('div.tit h1::text').get()
            items['empresa'] = response.css('div.tit a::text').get()
            items['actividad'] = response.css('ul.resumen a::text').getall()[0]
            items['lugarTrabajo'] = response.css('ul.resumen a::text').getall()[1]
            items['seniority'] = response.css('ul.resumen li::text').getall()[0]
            items['area'] = response.css('ul.resumen a::text').getall()[2]
            items['descripcion'] = response.css('div.descripcion p::text').getall()
            #items['edad'] = response.css('ul.requisitos li::text').getall()[0]
            #items['residencia'] = response.css('ul.requisitos li::text').getall()[1]
            #items['remuneracion'] = response.css('ul.requisitos li::text').getall()[2]
            #items['disponibilidad'] = response.css('ul.requisitos li::text').getall()[3]
            #items['idioma'] = 
            #items['sexo'] = 
        
        except:
            pass
            
        yield items
        
        