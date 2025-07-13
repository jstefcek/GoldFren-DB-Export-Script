# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

class Vozidla_Detail:
    def __init__(self, vozidlo_kod, subkategorie, vyrobce, model_vozidla, typ, objem, oznaceni, rok_od, rok_do, vykon, poznamka, publikovat):
        self.vozidlo_kod = vozidlo_kod
        self.subkategorie = subkategorie
        self.vyrobce = vyrobce
        self.model_vozidla = model_vozidla
        self.typ = typ
        self.objem = objem
        self.oznaceni = oznaceni
        self.rok_od = rok_od
        self.rok_do = rok_do
        self.vykon = vykon
        self.poznamka = poznamka
        self.publikovat = publikovat
        
def export_vozidla(conn: MySQLConnection, export_data):
    """
    Function would export all data avaible for Vozidla_Detail
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''select * from (
select 
	v.kod as vozidlo_kod, 
	s.nazev , 
	v2.nazev as vyrobce,
	CONCAT(v2.nazev, ' ', 
		if (ISNULL(v.typ), '', CONCAT(v.typ, ' ')), 
		if (ISNULL(v.objem),'',CONCAT(v.objem, ' ')), 
		if (ISNULL(v.oznaceni),'',CONCAT(v.oznaceni, ' '))) 
	as model_vozidla,
	v.typ, v.objem, 
	v.oznaceni, 
	v.rok_od, 
	v.rok_do, 
	v.vykon, 
	v.poznamka, 
	v.publikovat
from vozidlo v
left join vyrobce v2 on v2.kod = v.vyrobce_kod
left join subkategorie s on s.kod = v.subkategorie_kod 
) data
order by data.vyrobce asc'''
    
    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, Vozidla_Detail, 'Vozidla_Detail') 
    
    # Returns Vozidla_Detail data
    return export_data