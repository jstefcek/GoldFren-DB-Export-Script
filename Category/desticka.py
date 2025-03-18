# Exporting desticka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class desticka_data:
    def __init__(self, Sortiment, database_id, Part_Number, kategorie, subkategorie, vyrobce, oznaceni, typ, objem, rok_od, rok_do, publikovat, pozice, pozice_eng):
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
        self.pozice = pozice
        self.pozice_eng = pozice_eng
        
class desticka_detail_data:
    def __init__(self, Sortiment, kategorie, Part_Number, typ, plech_a_material, plech_a_tloustka, plech_a_matrice, plech_b_material, plech_b_tloustka, plech_b_matrice, izolator_a_material, 
                 izolator_a_tloustka, izolator_a_matrice, izolator_b_material, izolator_b_tloustka, izolator_b_matrice, segment_a_material, segment_a_tloustka, segment_a_matrice, 
                 segment_b_material, segment_b_tloustka, segment_b_matrice, konkurence_sbs, konkurence_ebc, konkurence_ferodo, konkurence_a2z, konkurence_rapco, konkurence_grove, 
                 konkurence_cleveland, konkurence_matco, material, poznamka, oem_cisla, obchodni_nazev, publikovat):
        self.Sortiment = Sortiment
        self.kategorie = kategorie
        self.Part_Number = Part_Number
        self.typ = typ
        self.plech_a_material = plech_a_material
        self.plech_a_tloustka = plech_a_tloustka
        self.plech_a_matrice = plech_a_matrice
        self.plech_b_material = plech_b_material
        self.plech_b_tloustka = plech_b_tloustka
        self.plech_b_matrice = plech_b_matrice
        self.izolator_a_material = izolator_a_material
        self.izolator_a_tloustka = izolator_a_tloustka
        self.izolator_a_matrice = izolator_a_matrice
        self.izolator_b_material = izolator_b_material
        self.izolator_b_tloustka = izolator_b_tloustka
        self.izolator_b_matrice = izolator_b_matrice
        self.segment_a_material = segment_a_material
        self.segment_a_tloustka = segment_a_tloustka
        self.segment_a_matrice = segment_a_matrice
        self.segment_b_material = segment_b_material
        self.segment_b_tloustka = segment_b_tloustka
        self.segment_b_matrice = segment_b_matrice
        self.konkurence_sbs = konkurence_sbs
        self.konkurence_ebc = konkurence_ebc
        self.konkurence_ferodo = konkurence_ferodo
        self.konkurence_a2z = konkurence_a2z
        self.konkurence_rapco = konkurence_rapco
        self.konkurence_grove = konkurence_grove
        self.konkurence_cleveland = konkurence_cleveland
        self.konkurence_matco = konkurence_matco
        self.material = material
        self.poznamka = poznamka
        self.oem_cisla = oem_cisla
        self.obchodni_nazev = obchodni_nazev
        self.publikovat = publikovat
        
def export_desticka_detail(conn: MySQLConnection, export_data: dict):
    """
    Function would export all data avaible for desticka
    
    Params:
        conn (MySQLConnection): Open connection to MySQL DB
        export_data (dict): Exported data for excel
    
    Returns:
        export_data (dict): Exported data for excel
    """
    # Prepare SQL statement
    sql_query = '''SELECT 'Destičká' as Sortiment, IFNULL(k.nazev, 'Nedefinováno') kategorie, d.cislo as Part_Number, IFNULL(dt.nazev, 'Nedefinováno') typ, 
d.plech_a_material, d.plech_a_tloustka, d.plech_a_matrice, d.plech_b_material, d.plech_b_tloustka, d.plech_b_matrice, 
d.izolator_a_material, d.izolator_a_tloustka, d.izolator_a_matrice, d.izolator_b_material, d.izolator_b_tloustka, 
d.izolator_b_matrice, d.segment_a_material, d.segment_a_tloustka, d.segment_a_matrice, d.segment_b_material, d.segment_b_tloustka, 
d.segment_b_matrice, d.konkurence_sbs, d.konkurence_ebc, d.konkurence_ferodo, d.konkurence_a2z, d.konkurence_rapco, d.konkurence_grove, 
d.konkurence_cleveland, d.konkurence_matco, d.material, d.poznamka, d.oem_cisla, d.obchodni_nazev, d.publikovat
FROM desticka d
LEFT JOIN sortiment s ON s.kod = d.sortiment_kod
LEFT JOIN kategorie k ON k.kod = d.kategorie_kod
LEFT JOIN desticka_typ dt ON dt.kod = d.typ
order by Part_Number asc;'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, desticka_detail_data, 'Destičky_Detail')
    
    # Returns adapter data
    return export_data
        
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
    sql_query = '''select distinct rs.*, p.nazev as pozice, p.nazev_eng as pozice_eng from (
SELECT 'Destička',
	d.kod,
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
UNION
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_1k
WHERE k.d_1k IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_2k
WHERE k.d_2k IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_2
WHERE k.d_2 IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_3
WHERE k.d_3 IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_3k
WHERE k.d_3k IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_4
WHERE k.d_4 IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_4k
WHERE k.d_4k IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_17
WHERE k.d_17 IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_17k
WHERE k.d_17k IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_26
WHERE k.d_26 IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_26k
WHERE k.d_26k IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_27
WHERE k.d_27 IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_27k
WHERE k.d_27k IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_28
WHERE k.d_28 IS NOT NULL
and d.cislo is not null
union
SELECT 'Destička',
	d.kod,
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
LEFT JOIN desticka d ON d.cislo = k.d_28k
WHERE k.d_28k IS NOT NULL
and d.cislo is not null
) as rs
left join vozidlo_desticka vd on vd.desticka_kod = rs.kod
left join pozice p on p.kod = vd.pozice_kod 
ORDER BY Part_Number asc'''

    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, desticka_data, 'Destičky')
        
    # Returns adapter data
    return export_data