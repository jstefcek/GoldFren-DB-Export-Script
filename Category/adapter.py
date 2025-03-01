# Exporting adapter values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class adapter_data:
    def __init__(self, sortiment, Part_Number, kategorie, subkategorie, vyrobce, oznaceni, typ, objem, rok_od, rok_do, publikovat):
        self.sortiment = sortiment
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
        
class adapter_detail_data:
    def __init__(self, Sortiment, kategorie, Part_Number, typ, prumer, popis, poznamka, publikovat):
        self.Sortiment = Sortiment
        self.kategorie = kategorie
        self.Part_Number = Part_Number
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
		a.oznaceni as Part_Number, 
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
order by Part_Number asc'''
    
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
    sql_query = '''select distinct * from (
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_18
WHERE k.a_18 IS NOT NULL
and a.oznaceni is not null
union
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_18k
WHERE k.a_18k IS NOT NULL
and a.oznaceni is not null
union
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_19
WHERE k.a_19 IS NOT NULL
and a.oznaceni is not null
union
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_19k
WHERE k.a_19k IS NOT NULL
and a.oznaceni is not null
union
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_20
WHERE k.a_20 IS NOT NULL
and a.oznaceni is not null
union
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_20k
WHERE k.a_20k IS NOT NULL
and a.oznaceni is not null
union
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_21
WHERE k.a_21 IS NOT NULL
and a.oznaceni is not null
union
SELECT 'Adaptér',
	a.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	case
	  when a.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN adapter a ON a.oznaceni = k.a_21k
WHERE k.a_21k IS NOT NULL
and a.oznaceni is not null
) as combined_result
order by Part_Number asc'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, adapter_data, 'Adaptér')
        
    # Returns adapter data
    return export_data