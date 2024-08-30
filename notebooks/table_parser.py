
def get_tables(schema, table_names):

    # Split the schema into individual tables
    tables = schema.split('CREATE TABLE')

    # Dictionary to store table schemas
    table_schemas = {}

    # Iterate over tables and match with requested table names
    for table in tables:
        for table_name in table_names:
            if f' {table_name} ' in table or f'"{table_name}"' in table:
                table_schemas[table_name] = 'CREATE TABLE' + table.strip()

    # Combine the matched table schemas into a single string
    combined_schemas = '\n\n'.join(table_schemas.values())
    
    return combined_schemas
    
'''

import re

def get_table_schemas(schema, table_names):
    """
    Extracts the CREATE TABLE statements for the specified table names from a schema string.

    Parameters:
    - schema (str): The schema as a string.
    - table_names (list of str): List of table names to extract schemas for.

    Returns:
    - str: Combined CREATE TABLE statements for the specified tables.

    Raises:
    - ValueError: If any of the specified table names are not found in the schema.
    """

    # Regular expression pattern to match CREATE TABLE statements
    create_table_pattern = re.compile(
        r'CREATE TABLE(?: IF NOT EXISTS)?\s+("?[a-zA-Z_][a-zA-Z0-9_]*"?)\s*\((.*?)\);',
        re.DOTALL | re.IGNORECASE
    )

    # Find all CREATE TABLE statements in the schema
    tables = create_table_pattern.findall(schema)

    # Dictionary to map table names to their CREATE TABLE statements
    table_schemas = {}

    for table_name_raw, table_definition in tables:
        # Remove quotes if present
        table_name = table_name_raw.strip('"')
        # Clean and reconstruct the CREATE TABLE statement
        create_statement = f'CREATE TABLE {table_name_raw} (\n{table_definition.strip()}\n);'
        table_schemas[table_name.lower()] = create_statement

    # List to hold the CREATE TABLE statements for the requested tables
    requested_schemas = []

    # List to track missing tables
    missing_tables = []

    for name in table_names:
        # Normalize table name for case-insensitive matching
        normalized_name = name.lower()
        if normalized_name in table_schemas:
            requested_schemas.append(table_schemas[normalized_name])
        else:
            missing_tables.append(name)

    if missing_tables:
        missing_tables_str = ', '.join(missing_tables)
        raise ValueError(f"The following table(s) were not found in the schema: {missing_tables_str}")

    # Combine the matched table schemas into a single string with separation
    combined_schemas = '\n\n'.join(requested_schemas)
    
    return combined_schemas
    '''