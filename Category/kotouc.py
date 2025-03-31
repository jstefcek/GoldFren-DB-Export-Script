# Exporting hadicka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class kotouc_data:
    def __init__(self, Sortiment, Cislo_vyrobku, Kategorie, Subkategorie, Vyrobce, Oznaceni_vozidla, Typ, Objem, Specialni_oznaceni, Rok_od, Rok_do, Pozice, Pozice_eng, Publikovat):

        self.Sortiment = Sortiment
        self.Cislo_vyrobku = Cislo_vyrobku
        self.Kategorie = Kategorie
        self.Subkategorie = Subkategorie
        self.Vyrobce = Vyrobce
        self.Oznaceni_vozidla = Oznaceni_vozidla
        self.typ = Typ
        self.objem = Objem
        self.Specialni_oznaceni = Specialni_oznaceni
        self.Rok_od = Rok_od
        self.Rok_do = Rok_do
        self.Pozice = Pozice
        self.Pozice_eng = Pozice_eng
        self.Publikovat = Publikovat
        
class kotouc_detail_data:
    def __init__(self, Sortiment, Kategorie, Cislo_vyrobku, Typ, Konkurence_Braking, Konkurence_Ngbrakes, Od, Hd, Id, Thk, Poznamka):
        self.Sortiment = Sortiment
        self.Kategorie = Kategorie
        self.Cislo_vyrobku = Cislo_vyrobku
        self.Typ = Typ
        self.Konkurence_Braking = Konkurence_Braking
        self.Konkurence_Ngbrakes = Konkurence_Ngbrakes
        self.Od = Od
        self.Hd = Hd
        self.Id = Id
        self.Thk = Thk
        self.Poznamka = Poznamka
        
def export_kotouc_detail(conn: MySQLConnection, export_data):
    """
    Function would export all data avaible for kotouc
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''select 'Kotouč' as Sortiment, IFNULL(k2.nazev, 'Nedefinováno') as Kategorie, k.oznaceni as Cislo_vyrobku, IFNULL(kt.nazev, 'Nedefinováno'), k.konkurence_braking, k.konkurence_ngbrakes, k.od, k.hd, k.id, k.thk, k.poznamka 
from kotouc k 
left join kategorie k2 on k2.kod = k.kategorie_kod
left join kotouc_typ kt on kt.kod = k.typ
order by Cislo_vyrobku asc;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, kotouc_detail_data, 'Kotouče_Detail')
    
    # Returns kotouc data
    return export_data

def export_kotouc(conn: MySQLConnection, export_data):
    """
    Function would export all data avaible for kotouc
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''select
	'Kotouč' as Sortiment,
	ko.oznaceni as Cislo_vyrobku,
	ka.nazev as Kategorie,
	sk.nazev as Subkategorie,
	vr.nazev as vyrobce,
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
	pz.nazev as pozice,
	pz.nazev_eng as pozice_eng,
    case 
	  when ko.publikovat = 1 then 'Ano'
	  else 'Ne'
	end as 'Publikovat'
from vozidlo_kotouc as vk
inner join vozidlo as vz on vk.vozidlo_kod = vz.kod
inner join vyrobce as vr on vz.vyrobce_kod = vr.kod
inner join pozice as pz on vk.pozice_kod = pz.kod
inner join subkategorie sk on vz.subkategorie_kod = sk.kod
inner join kategorie ka on sk.kategorie_kod = ka.kod
inner join kotouc ko on vk.kotouc_kod = ko.kod
order by ko.oznaceni asc
limit 18446744073709551615'''
    
    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, kotouc_data, 'Kotouče')
        
    # Returns kotouc data
    return export_data