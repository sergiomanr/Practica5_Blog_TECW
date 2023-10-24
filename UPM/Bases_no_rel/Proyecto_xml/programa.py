from lxml import etree
import xmltodict, json

class Validator:
    def __init__(self, xsd_path: str):
        xmlschema_doc = etree.parse(xsd_path)
        self.xmlschema = etree.XMLSchema(xmlschema_doc)

    #see https://lxml.de/validation.html#xmlschema
    def validate(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        result = self.xmlschema.validate(xml_doc)
        log = self.xmlschema.error_log
        print(log.last_error)
        return result

#descomentar si se ejecuta este archivo directamente en lugar que desde main.py
validator = Validator("viaje.xsd")
validator.validate("viaje.xml")

with open('viaje.xml', 'r', encoding='utf8') as myfile:
    #directamente cojo "catalogo" porque en xml hay un único root y en json eso no me convence
    obj = xmltodict.parse(myfile.read())["viaje"]
    #también existe un parámetro de xmltodict.parse que es force_list que se puede probar para forzar que transforme en listas determinados elementos
    # obj = xmltodict.parse(myfile.read(), force_list=('viaje'))


# print(obj)

#Los arrays los transforma un poco raro, hace un objeto con el primer elemento y ahí pone el array
viajero = obj["viajeros"]['viajero'][0]
viajero['nombre-viajero'] = 'Sergio Manrique' 
viajero['DNI'] = '06035305J'
viajero['email'] = 'sergio.manrique@alumnos.upm.es'
viajero['fecha-nacimiento'] = '2004-04-12'

# añadimos la propiedad $schema
obj["$schema"] = "./viaje.schema.json"
# print(obj)
# print("JSON DEL XML:")
# print(json.dumps(obj, indent=4, ensure_ascii=False))

with open('viaje.json', 'w', encoding='utf8') as outfile:
    json.dump(obj, outfile, indent=4, ensure_ascii=False)