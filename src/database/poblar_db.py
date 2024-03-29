# gracias a Rosa por datos de capacidad de salas

# nm: no modificado
# no son relevantes por el momento de todas formas, dado que 
# no son utilizadas en el testing del sistema

from src.models.models import Sala

def poblar():
    """
    Sala.crear(svg_id="rect954", nombre="A-001", ocupacion_max = 80)
    Sala.crear(svg_id="rect954-8", nombre="A-002", ocupacion_max = 80)
    Sala.crear(svg_id="rect954-1", nombre="A-003", ocupacion_max = 50)
    Sala.crear(svg_id="rect4907", nombre="A-004", ocupacion_max = 50)
    Sala.crear(svg_id="rect4909", nombre="A-005", ocupacion_max = 50)
    Sala.crear(svg_id="rect4915", nombre="A-006", ocupacion_max = 50)
    Sala.crear(svg_id="rect4917", nombre="A-007", ocupacion_max = 50)
    Sala.crear(svg_id="rect4903", nombre="A-008", ocupacion_max = 50)
    Sala.crear(svg_id="rect4897", nombre="A-009", ocupacion_max = 50)
    Sala.crear(svg_id="rect4895", nombre="A-010", ocupacion_max = 79)
    Sala.crear(svg_id="rect4891", nombre="A-011", ocupacion_max = 80)
    Sala.crear(svg_id="rect5073-1", nombre="A-012", ocupacion_max = 42)
    Sala.crear(svg_id="rect5073", nombre="A-013", ocupacion_max = 42)
    Sala.crear(svg_id="rect5071", nombre="A-014", ocupacion_max = 42)
    Sala.crear(svg_id="rect5069", nombre="A-015", ocupacion_max = 42)
    Sala.crear(svg_id="rect4905", nombre="A-016", ocupacion_max = 99)
    Sala.crear(svg_id="rect954-9", nombre="A-017", ocupacion_max = 50)
    Sala.crear(svg_id="rect4725", nombre="B-001", ocupacion_max = 56)
    Sala.crear(svg_id="rect4672-1", nombre="B-002", ocupacion_max = 56)
    Sala.crear(svg_id="rect4672-30", nombre="B-003", ocupacion_max = 70)
    Sala.crear(svg_id="rect4672-36", nombre="B-004", ocupacion_max = 70)
    Sala.crear(svg_id="rect4672-3", nombre="B-005", ocupacion_max = 70)
    Sala.crear(svg_id="rect4672-0", nombre="B-006", ocupacion_max = 70)
    Sala.crear(svg_id="rect4672-2", nombre="B-007", ocupacion_max = 70)
    Sala.crear(svg_id="rect4602-8-2,-2", nombre="B-008", ocupacion_max = 70)
    Sala.crear(svg_id="rect4602-8-2", nombre="B-009", ocupacion_max = 70)
    Sala.crear(svg_id="rect4602-8", nombre="B-010", ocupacion_max = 70)
    Sala.crear(svg_id="rect4602", nombre="B-011", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect4541", nombre="B-012", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect5195", nombre="B-015", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect5197", nombre="B-016", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect5002", nombre="Oficinas Primos", ocupacion_max = 20) # nm
    Sala.crear(svg_id="rect5026", nombre="Sala Reuniones", ocupacion_max = 20) # nm
    Sala.crear(svg_id="rect4746", nombre="LDS", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect4780", nombre="Arquitectura 1", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect4780-3", nombre="Auditorio", ocupacion_max = 300) # nm
    Sala.crear(svg_id="rect4833", nombre="Arquitectura 2", ocupacion_max = 100) # nm
    Sala.crear(svg_id="path5040", nombre="Noac Frontal", ocupacion_max = 200) # nm
    Sala.crear(svg_id="rect1261", nombre="Noac Trasero", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect4837", nombre="B-031", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect4849-1-1", nombre="B-033", ocupacion_max = 35)
    Sala.crear(svg_id="rect4849-1", nombre="B-035", ocupacion_max = 34)
    Sala.crear(svg_id="rect4849", nombre="B-037", ocupacion_max = 35)
    Sala.crear(svg_id="rect4851", nombre="B-039", ocupacion_max = 57)
    Sala.crear(svg_id="path351", nombre="Patio de las Lamparas", ocupacion_max = 300) # nm
    Sala.crear(svg_id="path1035", nombre="Testamento", ocupacion_max = 300) # nm
    Sala.crear(svg_id="rect211", nombre="Aula Magna", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect1087", nombre="Relaciones Estudiantiles", ocupacion_max = 60) # nm
    Sala.crear(svg_id="rect4857", nombre="Defider", ocupacion_max = 300) # nm
    Sala.crear(svg_id="path4863", nombre="Casino", ocupacion_max = 200) # nm
    Sala.crear(svg_id="rect4938", nombre="Dep. Humanística", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect4942", nombre="Dep. Matematica", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect1163", nombre="Dep. Ingeniería Minas", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect129", nombre="Ingeniería Mecánica", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect952", nombre="Ingeniería Eléctrica", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect5024", nombre="LPA", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect5026-7", nombre="Sala Postgrado", ocupacion_max = 30) # nm
    Sala.crear(svg_id="rect1245", nombre="Sala de Descanso", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect1269", nombre="Dep. Ing. Diseño de Productos", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect1247", nombre="Fablab", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect938", nombre="Taller Metal Mecánico", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect950", nombre="Lab. de Procesos", ocupacion_max = 100) # nm
    Sala.crear(svg_id="rect1159", nombre="B-064", ocupacion_max = 50) # nm
    Sala.crear(svg_id="rect1161", nombre="B-065", ocupacion_max = 50) # nm
    """

    Sala.crear(svg_id="rect954",   nombre="A-001",              ocupacion_max =80)
    Sala.crear(svg_id="rect954-8", nombre="A-002",              ocupacion_max =80)
    Sala.crear(svg_id="rect954-1", nombre="A-003",              ocupacion_max =50)
    Sala.crear(svg_id="rect4907",  nombre="A-004",              ocupacion_max =50)
    Sala.crear(svg_id="rect4909",  nombre="A-005",              ocupacion_max =50)
    Sala.crear(svg_id="rect4915",  nombre="A-006",              ocupacion_max =50)
    Sala.crear(svg_id="rect4917",  nombre="A-007",              ocupacion_max =50)
    Sala.crear(svg_id="rect4903",  nombre="A-008",              ocupacion_max =50)
    Sala.crear(svg_id="rect4897",  nombre="A-009",              ocupacion_max =50)
    Sala.crear(svg_id="rect4895",  nombre="A-010",              ocupacion_max =79)
    Sala.crear(svg_id="rect4891",  nombre="A-011",              ocupacion_max =80)
    Sala.crear(svg_id="rect5073-1", nombre="A-012",             ocupacion_max =42)
    Sala.crear(svg_id="rect5073",   nombre="A-013",             ocupacion_max =42)
    Sala.crear(svg_id="rect5071",   nombre="A-014",             ocupacion_max =42)
    Sala.crear(svg_id="rect5069",   nombre="A-015",             ocupacion_max =42)
    Sala.crear(svg_id="rect4905",   nombre="A-016",             ocupacion_max =99) #16
    Sala.crear(svg_id="rect954-9",  nombre="A-017",             ocupacion_max =50)
    Sala.crear(svg_id="rect4725",   nombre="B-001",             ocupacion_max =56)
    Sala.crear(svg_id="rect4672-1",  nombre="B-002",            ocupacion_max =56)
    Sala.crear(svg_id="rect4672-30", nombre="B-003",            ocupacion_max =70)
    Sala.crear(svg_id="rect4672-36", nombre="B-004",            ocupacion_max =70)
    Sala.crear(svg_id="rect4672-3",  nombre="B-005",            ocupacion_max =70)
    Sala.crear(svg_id="rect4672-0",  nombre="B-006",            ocupacion_max =70)
    Sala.crear(svg_id="rect4672-2",  nombre="B-007",            ocupacion_max =70)
    Sala.crear(svg_id="rect4603",    nombre="B-008",            ocupacion_max =70)
    Sala.crear(svg_id="rect4602-8-2",nombre="B-009",            ocupacion_max =70)
    Sala.crear(svg_id="rect4602-8",  nombre="B-010",            ocupacion_max =70)
    Sala.crear(svg_id="rect4602",    nombre="B-011",            ocupacion_max =50)
    Sala.crear(svg_id="rect4541",    nombre="B-012",            ocupacion_max =50)
    Sala.crear(svg_id="rect5195",    nombre="B-015",            ocupacion_max =50)
    Sala.crear(svg_id="rect5197",    nombre="B-016",            ocupacion_max =50)
    Sala.crear(svg_id="rect5002",   nombre="Oficinas Primos",   ocupacion_max =20) #32
    Sala.crear(svg_id="rect5026",   nombre="Sala Reuniones",    ocupacion_max =20)
    Sala.crear(svg_id="rect4746",   nombre="LDS",               ocupacion_max =100) #34
    Sala.crear(svg_id="path5040",   nombre="Noac Frontal",      ocupacion_max =200)
    Sala.crear(svg_id="rect4780",   nombre="Arquitectura 1",    ocupacion_max =100)
    Sala.crear(svg_id="rect4780-3", nombre="Auditorio",         ocupacion_max =300)
    Sala.crear(svg_id="rect4833", nombre="Arquitectura 2",      ocupacion_max =100)
    Sala.crear(svg_id="rect4837", nombre="B-031",               ocupacion_max =50)
    Sala.crear(svg_id="rect4849", nombre="B-037",               ocupacion_max =35)
    Sala.crear(svg_id="rect4851", nombre="B-039",               ocupacion_max =57)
    Sala.crear(svg_id="rect4857", nombre="Defider",             ocupacion_max =300)
    Sala.crear(svg_id="path4863", nombre="Casino",              ocupacion_max =200)
    # Sala.crear(svg_id="rect4869", nombre="Escaleras/Ascensor",  ocupacion_max =80)
    # Sala.crear(svg_id="rect5028",   nombre="Baño H",            ocupacion_max =80)
    # Sala.crear(svg_id="rect4921", nombre="Baño M",              ocupacion_max =80)
    # Sala.crear(svg_id="rect4921-3", nombre="Baño H",            ocupacion_max =80)
    Sala.crear(svg_id="rect4938", nombre="Dep. Humanística",    ocupacion_max =50)
    Sala.crear(svg_id="rect4942", nombre="Dep. Matematica",     ocupacion_max =50)
    Sala.crear(svg_id="rect5024", nombre="LPA",                 ocupacion_max =100)
    Sala.crear(svg_id="rect5042", nombre="Baño M",              ocupacion_max =80)
    Sala.crear(svg_id="rect5026-7", nombre="Sala Postgrado",  ocupacion_max =30)
    # Sala.crear(svg_id="rect5026-70",nombre="Baño M",          ocupacion_max =80)
    # Sala.crear(svg_id="rect5042-5", nombre="Baño H",            ocupacion_max =80)
    Sala.crear(svg_id="rect129",    nombre="Ingeniería Mecánica", ocupacion_max =100)
    Sala.crear(svg_id="rect1019",   nombre="Caja",               ocupacion_max =80)
    # Sala.crear(svg_id="rect1031",   nombre="Baño H",             ocupacion_max =80)
    # Sala.crear(svg_id="rect1031-5", nombre="Baño M",             ocupacion_max =80)
    Sala.crear(svg_id="rect1087",   nombre="Relaciones Estudiantiles", ocupacion_max =60)
    Sala.crear(svg_id="rect4849-1-1", nombre="B-033",            ocupacion_max =35)
    Sala.crear(svg_id="rect4849-1", nombre="B-035",              ocupacion_max =34)
    Sala.crear(svg_id="rect1245",  nombre="Sala de Descanso",    ocupacion_max =100)
    Sala.crear(svg_id="rect1261",  nombre="Noac Trasero",        ocupacion_max =100)
    Sala.crear(svg_id="rect1269",  nombre="Dep. Ing. Diseño de Productos", ocupacion_max =50)
    Sala.crear(svg_id="rect1031-5-8", nombre="Secretaría",       ocupacion_max =80)
    Sala.crear(svg_id="rect269",   nombre="Baño común",          ocupacion_max =80)
    Sala.crear(svg_id="rect1247",  nombre="Fablab",              ocupacion_max =50)
    # Sala.crear(svg_id="rect248",   nombre="Baño M",              ocupacion_max =80)
    # Sala.crear(svg_id="rect248-8", nombre="Baño H",              ocupacion_max =80)
    Sala.crear(svg_id="path351",  nombre="Patio de las Lamparas",ocupacion_max =300)
    Sala.crear(svg_id="rect938",  nombre="Taller Metal Mecánico",ocupacion_max =100)
    Sala.crear(svg_id="rect950",  nombre="Lab. de Procesos",     ocupacion_max =100)
    Sala.crear(svg_id="rect952",  nombre="Ingeniería Eléctrica", ocupacion_max =100)
    Sala.crear(svg_id="rect1159", nombre="B-064",                ocupacion_max =50)
    Sala.crear(svg_id="rect1161", nombre="B-065",                ocupacion_max =50)
    Sala.crear(svg_id="rect1163", nombre="Dep. Ingeniería Minas",ocupacion_max =100)
    # Sala.crear(svg_id="rect179",  nombre="Escalera",             ocupacion_max =80)
    Sala.crear(svg_id="path1013", nombre="Dep. Ing. Química Ambiental", ocupacion_max =80)
    Sala.crear(svg_id="path1035", nombre="Testamento",           ocupacion_max =300)
    Sala.crear(svg_id="rect1056", nombre="Don Fede",             ocupacion_max =80)
    Sala.crear(svg_id="rect211",  nombre="Aula Magna",           ocupacion_max =100)
    Sala.crear(svg_id="rect1439",  nombre="Oficina FabLab",      ocupacion_max =10) #71