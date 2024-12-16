import snowflake.connector

def update_missing_addresses(from_table):
    try:
        conn = {
            "user": "BINDU",
            "password": "B!ndu@41",
            "account": "jfduvyp-sb86292",
            "warehouse": "COMPUTE_WH",
            "database": "FIVETRAN_DATABASE",
            "schema": "SNOW_SCHEMA"
        }

       
        connection = snowflake.connector.connect(
            user=conn["user"],
            password=conn["password"],
            account=conn["account"],
            warehouse=conn["warehouse"],
            database=conn["database"],
            schema=conn["schema"]
        )

        
        cursor = connection.cursor()

        query_count = f"SELECT COUNT(ADDRESS) FROM {from_table} WHERE ADDRESS = ''"
        cursor.execute(query_count)
        count_missing_addresses = cursor.fetchone()[0]

        if count_missing_addresses > 0:
          
            update_query = f"UPDATE {from_table} SET ADDRESS = 'address not yet updated' WHERE ADDRESS = ''"
            cursor.execute(update_query)
            connection.commit()
            print(f"Updated {count_missing_addresses} missing addresses.")
            
        else:
            print("No missing addresses found.")

    except Exception as e:
        print( e)

    finally:
       
        if cursor:
            cursor.close()
        if connection:
            connection.close()


update_missing_addresses("YELP_ACADEMIC_DATASET_BUSINESS")
