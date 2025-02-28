def fetch_data(conn, sql_query, export_data, data_class, category_name='Adaptér'):
    """
    Fetches data from database and maps it to adapter objects.
    
    Args:
        conn: Database connection object
        sql_query: SQL query to execute
        export_data: Dictionary to store the results
        adapter_data_class: Class to instantiate for each row of data
        category_name: Key name to use in export_data dictionary (default: 'Adaptér')
    
    Returns:
        Updated export_data dictionary with adapter data
    """
    # Prepare cursor and execute query
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    # Create adapter dict if it doesn't exist
    if category_name not in export_data:
        export_data[category_name] = {}
    
    # Cycle in result data
    for index, value in enumerate(cursor.fetchall(), start=1):
        key = f"{index}"
        export_data[category_name][key] = data_class(*value)
    
    # Log
    print(f'[INFO] - Data pro {category_name} byla připravena!')
    
    # Return updated dictionary
    return export_data