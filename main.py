# Exports data from DB c41 catalog to excel

# Modules
from connections.mysql_conn import create_conn
from Category.adapter import export_adapter, export_adapter_detail
from Category.desticka import export_desticka, export_desticka_detail
from Category.kotouc import export_kotouc, export_kotouc_detail
from Category.hadicka import export_hadicka, export_hadicka_detail
from export.export_excel import create_excel
from Category.vozidla import export_vozidla

def main_process():
    """
    Main process that will exprot data from database c41catalog to excel with pivot
    """
    # Creates connection to DB
    conn = create_conn()
    
    # Main array with data
    export_data = {}
    
    # Prepare data for excel from katalog
    export_data = export_adapter(conn, export_data)
    export_data = export_adapter_detail(conn, export_data)
    export_data = export_desticka(conn, export_data)
    export_data = export_desticka_detail(conn, export_data)
    export_data = export_kotouc(conn, export_data)
    export_data = export_kotouc_detail(conn, export_data)
    export_data = export_hadicka(conn, export_data)
    export_data = export_hadicka_detail(conn, export_data)
    export_data = export_vozidla(conn, export_data)
    
    # Ukonceni connectiony do DB
    conn.close()
    
    # Export to excel pivot table
    create_excel(export_data, "GoldFren_WebCatalog_V8.xlsx")
    
    # Log
    print('[INFO] - Export dat byl dokončen')

# Start script
if __name__ == "__main__":
    print('[INFO] - Zacinam export dat do excelu')
    main_process()