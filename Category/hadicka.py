# Exporting hadicka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class hadicka_data:
    def __init__(self,Sortiment, Part_Number, kategorie, subkategorie, vyrobce, oznaceni, typ, objem, rok_od, rok_do, publikovat, poznamka):
        self.Sortiment = Sortiment
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
    sql_query = '''select distinct * from (
SELECT 'Kotouč' as Sortiment,
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
SELECT 'Kotouč',
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
and h.oznaceni is not null) as combined_result
order by Part_Number asc'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, hadicka_data, 'Hadičky')
    
    # Returns hadicka data
    return export_data