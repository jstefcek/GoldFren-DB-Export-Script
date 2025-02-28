# Exporting desticka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class desticka_data:
    def __init__(self, Sortiment, Part_Number, kategorie, subkategorie, vyrobce, oznaceni, typ, objem, rok_od, rok_do, publikovat):
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
    sql_query = '''SELECT 'Destička', 
       LPAD(CAST(d.cislo AS UNSIGNED), 3, '0') as Part_Number, 
       k.kategorie, 
       k.subkategorie, 
       k.vyrobce, 
       k.oznaceni, 
       k.typ, 
       k.objem, 
       k.rok_od, 
       k.rok_do,
       case 
        when d.publikovat = '1' then 'Ano'
        else 'Ne'
       end publikovat
FROM katalog k
LEFT JOIN desticka d ON FIND_IN_SET(d.cislo, k.d_1) > 0
WHERE k.d_1 IS NOT NULL
ORDER BY CAST(d.cislo AS UNSIGNED) ASC'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, desticka_data, 'Destičky')
        
    # Returns adapter data
    return export_data