# Exporting hadicka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class kotouc_data:
    def __init__(self, Sortiment, Part_Number, kategorie, subkategorie, vyrobce, oznaceni, typ, objem, rok_od, rok_do, konkurence_braking, konkurence_ngbrakes, poznamka, publikovat):
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
        self.konkurence_braking = konkurence_braking
        self.konkurence_ngbrakes = konkurence_ngbrakes
        self.poznamka = poznamka
        self.publikovat = publikovat
        
class kotouc_detail_data:
    def __init__(self, Sortiment, Kategorie, Part_Number, Typ, Konkurence_Braking, Konkurence_Ngbrakes, Od, Hd, Id, Thk, Poznamka):
        self.Sortiment = Sortiment
        self.Kategorie = Kategorie
        self.Part_Number = Part_Number
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
    sql_query = '''select 'Kotouč' as Sortiment, IFNULL(k2.nazev, 'Nedefinováno') as Kategorie, k.oznaceni as Part_Number, IFNULL(kt.nazev, 'Nedefinováno'), k.konkurence_braking, k.konkurence_ngbrakes, k.od, k.hd, k.id, k.thk, k.poznamka 
from kotouc k 
left join kategorie k2 on k2.kod = k.kategorie_kod
left join kotouc_typ kt on kt.kod = k.typ
order by Part_Number asc;'''

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
    sql_query = '''select distinct * from (
SELECT 'Kotouč' as Sortiment,
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_5)
WHERE k.k_5 IS NOT NULL
and k2.oznaceni is not null
union
SELECT 'Kotouč',
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_5k)
WHERE k.k_5k IS NOT NULL
and k2.oznaceni is not null
union
SELECT 'Kotouč',
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_6)
WHERE k.k_6 IS NOT NULL
and k2.oznaceni is not null
union
SELECT 'Kotouč',
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_6k)
WHERE k.k_6k IS NOT NULL
and k2.oznaceni is not null
union
SELECT 'Kotouč',
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_7)
WHERE k.k_7 IS NOT NULL
and k2.oznaceni is not null
union
SELECT 'Kotouč',
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_7k)
WHERE k.k_7k IS NOT NULL
and k2.oznaceni is not null
union
SELECT 'Kotouč',
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_8)
WHERE k.k_8 IS NOT NULL
and k2.oznaceni is not null
union
SELECT 'Kotouč',
	k2.oznaceni as Part_Number,
	k.kategorie,
	k.subkategorie,
	k.vyrobce,
	k.oznaceni,
	k.typ,
	k.objem,
	k.rok_od,
	k.rok_do,
	k2.konkurence_braking,
	k2.konkurence_ngbrakes,
	k2.poznamka,
	case
	  when k2.publikovat = '1' then 'Ano'
	  else 'Ne'
	end publikovat
FROM katalog k
LEFT JOIN kotouc k2 ON FIND_IN_SET(k2.oznaceni, k.k_8k)
WHERE k.k_8k IS NOT NULL
and k2.oznaceni is not null
) as combined_result
order by Part_Number asc;'''
    
    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, kotouc_data, 'Kotouče')
        
    # Returns kotouc data
    return export_data