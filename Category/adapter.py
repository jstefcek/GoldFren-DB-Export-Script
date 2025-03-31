# Exporting adapter values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class adapter_data:
    def __init__(self, Sortiment, Cislo_Vyrobku, Kategorie, Subkategorie, Vyrobce, Oznaceni_vozidla, Typ, Objem, Specialni_oznaceni, Rok_od, Rok_do, Pozice, Pozice_eng, Publiovat):
        self.Sortiment = Sortiment
        self.Cislo_Vyrobku = Cislo_Vyrobku
        self.Kategorie = Kategorie
        self.Subkategorie = Subkategorie
        self.Vyrobce = Vyrobce
        self.Oznaceni_vozidla = Oznaceni_vozidla
        self.Typ = Typ
        self.objem = Objem
        self.Specialni_oznaceni = Specialni_oznaceni
        self.Rok_od = Rok_od
        self.Rok_do = Rok_do
        self.Pozice = Pozice
        self.Pozice_eng = Pozice_eng
        self.Publikovat = Publiovat
        
class adapter_detail_data:
    def __init__(self, Sortiment, kategorie, Cislo_Vyrobku, typ, prumer, popis, poznamka, publikovat):
        self.Sortiment = Sortiment
        self.kategorie = kategorie
        self.Cislo_Vyrobku = Cislo_Vyrobku
        self.typ = typ
        self.prumer = prumer
        self.popis = popis
        self.poznamka = poznamka
        self.publikovat = publikovat   
        
def export_adapter_detail(conn: MySQLConnection, export_data):
    """
    Function would export all data avaible for adapter
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''select s.nazev as Sortiment, 
		a.kategorie_kod kategorie, 
		a.oznaceni as Cislo_Vyrobku, 
		a.typ, 
		a.prumer, 
		a.popis, 
		a.poznamka, 
		case 
          when a.publikovat = '1' then 'Ano'
          else 'Ne'
        end publikovat
from adapter a
left join sortiment s on s.kod = a.sortiment_kod
order by Cislo_Vyrobku asc'''
    
    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, adapter_detail_data, 'Adaptér_Detail') 
    
    # Returns adapter data
    return export_data

def export_adapter(conn: MySQLConnection, export_data: dict):
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
	'Adaptér' as Sortiment,
 	ad.oznaceni as Cislo_Vyrobku,
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
	  when ad.publikovat = 1 then 'Ano'
	  else 'Ne'
	end as 'Publikovat'
from vozidlo_adapter as vk
inner join vozidlo as vz on vk.vozidlo_kod = vz.kod
inner join vyrobce as vr on vz.vyrobce_kod = vr.kod
inner join pozice as pz on vk.pozice_kod = pz.kod
inner join subkategorie sk on vz.subkategorie_kod = sk.kod
inner join kategorie ka on sk.kategorie_kod = ka.kod
inner join adapter ad on vk.adapter_kod = ad.kod
order by ad.oznaceni asc
limit 18446744073709551615;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, adapter_data, 'Adaptér')
        
    # Returns adapter data
    return export_data