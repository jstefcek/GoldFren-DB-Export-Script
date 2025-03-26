# Exporting hadicka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class hadicka_data:
    def __init__(self,Sortiment, Cislo_vyrobku, Kategorie, Subkategorie, Vyrobce, Oznaceni_vozidla, Typ, Objem, Specialni_oznaceni, Rok_od, Rok_do, Pozice, Pozice_eng):
        self.Sortiment = Sortiment
        self.Cislo_vyrobku = Cislo_vyrobku
        self.Kategorie = Kategorie
        self.Subkategorie = Subkategorie
        self.Vyrobce = Vyrobce
        self.Oznaceni_vozidla = Oznaceni_vozidla
        self.Typ = Typ
        self.oObjembjem = Objem
        self.Specialni_oznaceni = Specialni_oznaceni
        self.Rok_od = Rok_od
        self.Rok_do = Rok_do
        self.Pozice = Pozice
        self.Pozice_eng = Pozice_eng
        
class hadicka_data_detail:
    def __init__(self, Sortiment, Kategorie, Cislo_vyrobku, Popis, Publikovat):
        self.Sortiment = Sortiment
        self.Kategorie = Kategorie
        self.Cislo_vyrobku = Cislo_vyrobku
        self.Popis = Popis
        self.Publikovat = Publikovat
        
def export_hadicka_detail(conn: MySQLConnection, export_data: dict):
    """
    Function would export all data avaible for hadicka
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''SELECT 'Hadička' as Sortiment, ifnull(kategorie_kod, 'Nedefinováno') as Kategorie, oznaceni as Cislo_vyrobku, popis, 
case
	  when publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM hadicka
order by Cislo_vyrobku asc;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, hadicka_data_detail, 'Hadičky_Detail')
    
    # Returns hadicka data
    return export_data

def export_hadicka(conn: MySQLConnection, export_data: dict):
    """
    Function would export all data avaible for hadicka
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''select
	'Hadička' as Sortiment,
	ha.oznaceni as Cislo_vyrobku,
	ka.nazev as Kategorie,
	sk.nazev as Subkategorie,
	vr.nazev as Vyrobce,
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
	vz.typ,
	vz.objem,
	vz.oznaceni as Specialni_oznaceni,
	vz.rok_od,
	vz.rok_do,
	pz.nazev as Pozice,
	pz.nazev_eng as Pozice_eng
from vozidlo_hadicka vb
inner join vozidlo vz on vb.vozidlo_kod = vz.kod
inner join vyrobce vr on vz.vyrobce_kod = vr.kod
inner join pozice pz on vb.pozice_kod = pz.kod
inner join subkategorie sk on vz.subkategorie_kod = sk.kod
inner join kategorie ka on sk.kategorie_kod = ka.kod
inner join hadicka ha on vb.hadicka_kod = ha.kod
order by ha.oznaceni asc
limit 18446744073709551615;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, hadicka_data, 'Hadičky')
    
    # Returns hadicka data
    return export_data