
import pandas as pd
from sparql import query, display_result

async def main():
    df = await query("""

    SELECT DISTINCT ?Prädikat ?Objekt WHERE {
        
        <https://fedlex.data.admin.ch/eli/cc/1999/404> ?Prädikat ?Objekt .
    } 

    """, "fedlex_sparqlendpoint")

display_result(df)

# Call the async function
await main()
