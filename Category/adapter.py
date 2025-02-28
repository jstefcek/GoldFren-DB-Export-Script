# Exporting adapter values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class adapter_data:
    def __init__(self, sortiment, kategorie, obrazek, obrazek_nazev, vektor, vektor_nazev, oznaceni, typ, prumer, popis, poznamka, publikovat):
        self.sortiment = sortiment
        self.kategorie = kategorie
        self.obrazek = obrazek
        self.obrazek_nazev = obrazek_nazev
        self.vektor = vektor
        self.vektor_nazev = vektor_nazev
        self.oznaceni = oznaceni
        self.typ = typ
        self.prumer = prumer
        self.popis = popis
        self.poznamka = poznamka
        self.publikovat = publikovat

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
    sql_query = '''select  s.nazev, 
		a.kategorie_kod kategorie, 
		a.obrazek, 
		a.obrazek_nahled obrazek_nazev, 
		a.vektor, 
		a.vektor_nazev, 
		a.oznaceni, 
		a.typ, 
		a.prumer, 
		a.popis, 
		a.poznamka, 
		case 
          when a.publikovat = '1' then 'Ano'
          else 'Ne'
        end publikovat
from adapter a
left join sortiment s on s.kod = a.sortiment_kod;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, adapter_data, 'Adaptér')
        
    # Returns adapter data
    return export_data