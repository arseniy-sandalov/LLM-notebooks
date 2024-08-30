import re

# List of SQL command words
sql_commands = [
    "SELECT", "FROM", "WHERE", "INSERT", "INTO", "VALUES", "UPDATE", "SET", 
    "DELETE", "JOIN", "INNER", "LEFT", "RIGHT", "FULL", "OUTER", "ON", 
    "ORDER", "BY", "GROUP", "HAVING", "DISTINCT", "UNION", "ALL", "LIMIT", 
    "OFFSET", "AS", "AND", "OR", "IN", "NOT", "NULL", "IS", "LIKE", 
    "BETWEEN", "EXISTS", "CASE", "WHEN", "THEN", "ELSE", "END", "CREATE", 
    "ALTER", "DROP", "TABLE", "DATABASE", "INDEX", "VIEW", "TRIGGER", 
    "USER", "GRANT", "REVOKE", "WITH", "PRIMARY", "KEY", "FOREIGN", 
    "REFERENCES", "CHECK", "DEFAULT", "CONSTRAINT"
]

# Function to correct SQL queries
def correct_sql_query(query):
    # Create a regex pattern that matches any SQL command words
    pattern = re.compile(r'(' + '|'.join(sql_commands) + r')', re.IGNORECASE)
    
    # Insert spaces around SQL command words
    corrected_query = pattern.sub(r' \1 ', query)
    
    # Remove any extra spaces that might have been added
    corrected_query = re.sub(r'\s+', ' ', corrected_query).strip()
    
    return corrected_query