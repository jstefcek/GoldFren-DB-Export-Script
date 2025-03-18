# Exporting hadicka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class hadicka_data:
    def __init__(self,Sortiment, database_id, Part_Number, kategorie, subkategorie, vyrobce, oznaceni, typ, objem, rok_od, rok_do, publikovat, poznamka, pozice, pozice_eng):
        self.Sortiment = Sortiment
        self.database_id = database_id
        self.Part_Number = Part_Number
        self.kategorie = kategorie
        self.subkategorie = subkategorie
        self.vyrobce = vyrobce
        self.oznaceni = oznaceni
        self.typ = typ
        self.objem = objem
        self.rok_od = rok_od
        self.rok_do = rok_do
        self.publikovat = publikovat
        self.poznamka = poznamka
        self.pozice = pozice
        self.pozice_eng = pozice_eng
        
class hadicka_data_detail:
    def __init__(self, Sortiment, Kategorie, Part_Number, Popis, Publikovat):
        self.Sortiment = Sortiment
        self.Kategorie = Kategorie
        self.Part_Number = Part_Number
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
    sql_query = '''SELECT 'Hadička' as Sortiment, ifnull(kategorie_kod, 'Nedefinováno') as Kategorie, oznaceni as Part_Number, popis, 
case
	  when publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM hadicka
order by Part_Number asc;'''

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
    sql_query = '''select distinct rs.*, p.nazev as pozice, p.nazev_eng as pozice_eng from (
SELECT 'Hadička' as Sortiment,
	h.kod, 
	h.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when h.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat,
	h.poznamka
FROM katalog k
LEFT JOIN hadicka h ON h.oznaceni = k.h_13
WHERE k.h_13 IS NOT NULL
and h.oznaceni is not null
union 
SELECT 'Hadička' as Sortiment,
	h.kod, 
	h.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when h.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat,
	h.poznamka
FROM katalog k
LEFT JOIN hadicka h ON h.oznaceni = k.h_15
WHERE k.h_15 IS NOT NULL
and h.oznaceni is not null) as rs
left join vozidlo_hadicka vh on vh.hadicka_kod = rs.kod
left join pozice p on p.kod = vh.pozice_kod
order by rs.Part_Number asc'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, hadicka_data, 'Hadičky')
    
    # Returns hadicka data
    return export_data