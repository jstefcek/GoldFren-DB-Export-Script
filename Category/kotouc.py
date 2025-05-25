# Exporting hadicka values

# Custom modules
from export.export_data import fetch_data
from mysql.connector import MySQLConnection

# Custom class
class kotouc_data:
    def __init__(self, Sortiment, Kod_Kotouce, Cislo_vyrobku, Kategorie, Subkategorie, Vyrobce, Vozidlo_Kod, Oznaceni_vozidla, Typ, Objem, Specialni_oznaceni, Rok_od, Rok_do, Pozice, Pozice_eng, Publikovat):
        self.Sortiment = Sortiment
        self.Kod_Kotouce = Kod_Kotouce
        self.Cislo_vyrobku = Cislo_vyrobku
        self.Kategorie = Kategorie
        self.Subkategorie = Subkategorie
        self.Vyrobce = Vyrobce
        self.Vozidlo_Kod = Vozidlo_Kod
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
    def __init__(self, Kod, Sortiment, Kategorie, Cislo_vyrobku, Typ, Konkurence_Braking, Konkurence_Ngbrakes, Od, Hd, Id, Thk, Poznamka):
        self.Kod = Kod
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
    sql_query = '''select k.kod as ID, 'Kotouč' as Sortiment, IFNULL(k2.nazev, 'Nedefinováno') as Kategorie, k.oznaceni as Cislo_vyrobku, IFNULL(kt.nazev, 'Nedefinováno'), k.konkurence_braking, k.konkurence_ngbrakes, k.od, k.hd, k.id, k.thk, k.poznamka 
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
    sql_query = '''SELECT
	'Kotouč' AS Sortiment,
	ko.kod as Kod_Kotouce,
	ko.oznaceni AS Cislo_vyrobku,
	ka.nazev AS Kategorie,
	sk.nazev AS Subkategorie,
	vr.nazev AS vyrobce,
	vz.kod as Vozidlo_Kod,
	CONCAT(
		vr.nazev, ' ',
		IF(ISNULL(vz.typ), '', CONCAT(vz.typ, ' ')),
		IF(ISNULL(vz.objem), '', CONCAT(vz.objem, ' ')),
		IF(ISNULL(vz.oznaceni), '', CONCAT(vz.oznaceni, ' ')),
		IF(ISNULL(vz.rok_od), '', CONCAT(vz.rok_od, '-')),
		IF(ISNULL(vz.rok_do), '', CONCAT(IF(ISNULL(vz.rok_od), '-', ''), vz.rok_do))
	) AS Oznaceni_vozidla,
	vz.typ,
	vz.objem,
	vz.oznaceni AS Specialni_oznaceni,
	vz.rok_od,
	vz.rok_do,
	pz.nazev AS pozice,
	pz.nazev_eng AS pozice_eng,
	CASE 
		WHEN ko.publikovat = 1 THEN 'Ano'
		ELSE 'Ne'
	END AS Publikovat
FROM vozidlo_kotouc AS vk
INNER JOIN vozidlo AS vz ON vk.vozidlo_kod = vz.kod
INNER JOIN vyrobce AS vr ON vz.vyrobce_kod = vr.kod
INNER JOIN pozice AS pz ON vk.pozice_kod = pz.kod
INNER JOIN subkategorie sk ON vz.subkategorie_kod = sk.kod
INNER JOIN kategorie ka ON sk.kategorie_kod = ka.kod
INNER JOIN kotouc ko ON vk.kotouc_kod = ko.kod

UNION

SELECT
	'Kotouč' AS Sortiment,
	ko.kod as Kod_Kotouce,
	CONCAT(ko.oznaceni, '-', kov.varianta_kod) AS Cislo_vyrobku,
	ka.nazev AS Kategorie,
	sk.nazev AS Subkategorie,
	vr.nazev AS vyrobce,
	vz.kod as Vozidlo_Kod,
	CONCAT(
		vr.nazev, ' ',
		IF(ISNULL(vz.typ), '', CONCAT(vz.typ, ' ')),
		IF(ISNULL(vz.objem), '', CONCAT(vz.objem, ' ')),
		IF(ISNULL(vz.oznaceni), '', CONCAT(vz.oznaceni, ' ')),
		IF(ISNULL(vz.rok_od), '', CONCAT(vz.rok_od, '-')),
		IF(ISNULL(vz.rok_do), '', CONCAT(IF(ISNULL(vz.rok_od), '-', ''), vz.rok_do))
	) AS Oznaceni_vozidla,
	vz.typ,
	vz.objem,
	vz.oznaceni AS Specialni_oznaceni,
	vz.rok_od,
	vz.rok_do,
	pz.nazev AS pozice,
	pz.nazev_eng AS pozice_eng,
	CASE 
		WHEN ko.publikovat = 1 THEN 'Ano'
		ELSE 'Ne'
	END AS Publikovat
FROM vozidlo_kotouc AS vk
INNER JOIN vozidlo AS vz ON vk.vozidlo_kod = vz.kod
INNER JOIN vyrobce AS vr ON vz.vyrobce_kod = vr.kod
INNER JOIN pozice AS pz ON vk.pozice_kod = pz.kod
INNER JOIN subkategorie sk ON vz.subkategorie_kod = sk.kod
INNER JOIN kategorie ka ON sk.kategorie_kod = ka.kod
INNER JOIN kotouc ko ON vk.kotouc_kod = ko.kod
INNER JOIN kotouc_varianta kov ON ko.kod = kov.kotouc_kod
ORDER BY Cislo_vyrobku ASC
LIMIT 18446744073709551615;'''
    
    # Fetch data from database
    export_data = fetch_data(conn, sql_query, export_data, kotouc_data, 'Kotouče')
        
    # Returns kotouc data
    return export_data