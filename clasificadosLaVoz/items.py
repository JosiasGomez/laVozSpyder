# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClasificadoslavozItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    empresa = scrapy.Field()
    actividad = scrapy.Field()
    lugarTrabajo = scrapy.Field()
    seniority = scrapy.Field()
    area = scrapy.Field()
    descripcion = scrapy.Field()
    #edad = scrapy.Field()
    #residencia = scrapy.Field()
    #remuneracion = scrapy.Field()
    #disponibilidad = scrapy.Field()
    #idioma = scrapy.Field()
    #sexo = scrapy.Field()
    
    pass
