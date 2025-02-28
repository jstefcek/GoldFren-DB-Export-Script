# Exports data from DB c41 catalog to excel

# Modules
from connections.mysql_conn import create_conn
from Category.adapter import export_adapter
from Category.desticka import export_desticka
from export.export_excel import create_excel

def main_process():
    """
    Main process that will exprot data from database c41catalog to excel with pivot
    """
    # Creates connection to DB
    conn = create_conn()
    
    # Main array with data
    export_data = {}
    
    # Prepare data for excel
    export_data = export_adapter(conn, export_data)
    export_data = export_desticka(conn, export_data)
    
    # Ukonceni connectiony do DB
    conn.close()
    
    # Export to excel pivot table
    create_excel(export_data, "GoldFren_WebCatalog_V2.xlsx")
    
    # Log
    print('[INFO] - Export dat byl dokončen')

# Start script
if __name__ == "__main__":
    print('[INFO] - Zacinam export dat do excelu')
    main_process()