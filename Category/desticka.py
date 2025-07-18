# Exporting desticka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class desticka_data:
    def __init__(self, Sortiment, Kod_Desticky, Cislo_Vyrobku, Kategorie, Subkategorie, Vyrobce, Vozidlo_Kod, Oznaceni_vozidla, Typ, Objem, Specialni_oznaceni, Rok_od, Rok_do, 
                 Pozice, Pozice_eng, SBS, EBC, Ferodo, A2Z, Rapco, Grove, Cleveland, Matco, Publikovat):
        self.Sortiment = Sortiment
        self.Kod_Desticky = Kod_Desticky
        self.Cislo_Vyrobku = Cislo_Vyrobku
        self.Kategorie = Kategorie
        self.Subkategorie = Subkategorie
        self.Vyrobce = Vyrobce
        self.Vozidlo_Kod = Vozidlo_Kod
        self.Oznaceni_vozidla = Oznaceni_vozidla
        self.Typ = Typ
        self.Objem = Objem
        self.Specialni_oznaceni = Specialni_oznaceni
        self.Rok_od = Rok_od
        self.Rok_do = Rok_do
        self.Pozice = Pozice
        self.Pozice_eng = Pozice_eng
        self.SBS = SBS
        self.EBC = EBC
        self.Ferodo = Ferodo
        self.A2Z = A2Z
        self.Rapco = Rapco
        self.Grove = Grove
        self.Cleveland = Cleveland
        self.Matco = Matco
        self.Publikovat = Publikovat
        
class desticka_detail_data:
    def __init__(self, Kod, Sortiment, kategorie, Cislo_Vyrobku, typ, plech_a_material, plech_a_tloustka, plech_a_matrice, plech_b_material, plech_b_tloustka, plech_b_matrice, izolator_a_material, 
                 izolator_a_tloustka, izolator_a_matrice, izolator_b_material, izolator_b_tloustka, izolator_b_matrice, segment_a_material, segment_a_tloustka, segment_a_matrice, 
                 segment_b_material, segment_b_tloustka, segment_b_matrice, konkurence_sbs, konkurence_ebc, konkurence_ferodo, konkurence_a2z, konkurence_rapco, konkurence_grove, 
                 konkurence_cleveland, konkurence_matco, material, poznamka, oem_cisla, obchodni_nazev, publikovat):
        self.Kod = Kod
        self.Sortiment = Sortiment
        self.kategorie = kategorie
        self.Cislo_Vyrobku = Cislo_Vyrobku
        self.typ = typ
        self.plech_a_material = plech_a_material
        self.plech_a_tloustka = plech_a_tloustka
        self.plech_a_matrice = plech_a_matrice
        self.plech_b_material = plech_b_material
        self.plech_b_tloustka = plech_b_tloustka
        self.plech_b_matrice = plech_b_matrice
        self.izolator_a_material = izolator_a_material
        self.izolator_a_tloustka = izolator_a_tloustka
        self.izolator_a_matrice = izolator_a_matrice
        self.izolator_b_material = izolator_b_material
        self.izolator_b_tloustka = izolator_b_tloustka
        self.izolator_b_matrice = izolator_b_matrice
        self.segment_a_material = segment_a_material
        self.segment_a_tloustka = segment_a_tloustka
        self.segment_a_matrice = segment_a_matrice
        self.segment_b_material = segment_b_material
        self.segment_b_tloustka = segment_b_tloustka
        self.segment_b_matrice = segment_b_matrice
        self.konkurence_sbs = konkurence_sbs
        self.konkurence_ebc = konkurence_ebc
        self.konkurence_ferodo = konkurence_ferodo
        self.konkurence_a2z = konkurence_a2z
        self.konkurence_rapco = konkurence_rapco
        self.konkurence_grove = konkurence_grove
        self.konkurence_cleveland = konkurence_cleveland
        self.konkurence_matco = konkurence_matco
        self.material = material
        self.poznamka = poznamka
        self.oem_cisla = oem_cisla
        self.obchodni_nazev = obchodni_nazev
        self.publikovat = publikovat
        
def export_desticka_detail(conn: MySQLConnection, export_data: dict):
    """
    Function would export all data avaible for desticka
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''SELECT d.kod as Kod, 'Destičká' as Sortiment, IFNULL(k.nazev, 'Nedefinováno') kategorie, d.cislo as Cislo_Vyrobku, IFNULL(dt.nazev, 'Nedefinováno') typ, 
d.plech_a_material, d.plech_a_tloustka, d.plech_a_matrice, d.plech_b_material, d.plech_b_tloustka, d.plech_b_matrice, 
d.izolator_a_material, d.izolator_a_tloustka, d.izolator_a_matrice, d.izolator_b_material, d.izolator_b_tloustka, 
d.izolator_b_matrice, d.segment_a_material, d.segment_a_tloustka, d.segment_a_matrice, d.segment_b_material, d.segment_b_tloustka, 
d.segment_b_matrice, d.konkurence_sbs, d.konkurence_ebc, d.konkurence_ferodo, d.konkurence_a2z, d.konkurence_rapco, d.konkurence_grove, 
d.konkurence_cleveland, d.konkurence_matco, d.material, d.poznamka, d.oem_cisla, d.obchodni_nazev, d.publikovat
FROM desticka d
LEFT JOIN sortiment s ON s.kod = d.sortiment_kod
LEFT JOIN kategorie k ON k.kod = d.kategorie_kod
LEFT JOIN desticka_typ dt ON dt.kod = d.typ
order by Cislo_Vyrobku asc;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, desticka_detail_data, 'Destičky_Detail')
    
    # Returns adapter data
    return export_data
        
def export_desticka(conn: MySQLConnection, export_data: dict):
    """
    Function would export all data avaible for adapter
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''select
	'Destička' as Sortiment,
    de.kod as Kod_Desticky,
	de.cislo as Part_Number,
	ka.nazev as Kategorie,
	sk.nazev as Subkategorie,
	vr.nazev as Vyrobce,
    vz.kod as Vozidlo_Kod,
	CONCAT(
            		vr.nazev,
            		' ',
            
            	if (
            		ISNULL(vz.typ),
            		'',
            		CONCAT(vz.typ, ' ')
            	),
            
            if (
            	ISNULL(vz.objem),
            	'',
            	CONCAT(vz.objem, ' ')
            ),
            
            if (
            	ISNULL(vz.oznaceni),
            	'',
            	CONCAT(vz.oznaceni, ' ')
            ),
            
            if (
            	ISNULL(vz.rok_od),
            	'',
            	CONCAT(vz.rok_od, '-')
            ),
            
            if (
            	ISNULL(vz.rok_do),
            	'',
            	CONCAT(
            
            		if (ISNULL(vz.rok_od), '-', ''),
            		vz.rok_do
            	)
            )
            	) as Oznaceni_vozidla,
	vz.typ as Typ,
	vz.objem as Objem,
	vz.oznaceni as Specialni_oznaceni,
	vz.rok_od as Rok_od,
	vz.rok_do as Rok_do,
	pz.nazev as Pozice,
	pz.nazev_eng as Pozice_eng,
	de.konkurence_sbs as SBS,
	de.konkurence_ebc as EBC,
	de.konkurence_ferodo as Ferodo,
	de.konkurence_a2z as A2Z,
	de.konkurence_rapco as Rapco,
	de.konkurence_grove as Grove,
	de.konkurence_cleveland as Cleveland,
	de.konkurence_matco as Matco,
	case 
	  when de.publikovat = 1 then 'Ano'
	  else 'Ne'
	end as 'Publikovat'
from vozidlo_desticka vd
inner join vozidlo vz on vd.vozidlo_kod = vz.kod
inner join vyrobce vr on vz.vyrobce_kod = vr.kod
inner join pozice pz on vd.pozice_kod = pz.kod
inner join subkategorie sk on vz.subkategorie_kod = sk.kod
inner join kategorie ka on sk.kategorie_kod = ka.kod
inner join desticka de on vd.desticka_kod = de.kod
order by cast(de.cislo as UNSIGNED) asc
limit 18446744073709551615;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, desticka_data, 'Destičky')
        
    # Returns adapter data
    return export_data