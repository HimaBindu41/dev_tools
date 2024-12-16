from snowflake.snowpark import Session

def drop_null_columns(table_name):
    try:
        # Create Snowpark session
        conn_parm ={
            "user":"BINDU",
            "password":"B!ndu@41",
            "account":"jfduvyp-sb86292",
            "warehouse":"COMPUTE_WH",
            "database":"FIVETRAN_DATABASE",
            "schema":"SNOW_SCHEMA"
        }
        session = Session.builder.configs(conn_parm).create()

      
        table_df = session.sql(f"SELECT * FROM {table_name}")

        
        columns = table_df.columns

        
        null_columns = []
        for column in columns:
            null_count = table_df.filter(table_df[column].isNull()).count()
            if null_count > 0:
                null_columns.append(column)

        if null_columns:
            
            for column in null_columns:
                table_check=session.sql(f"ALTER TABLE {table_name} DROP COLUMN {column}")
                print(table_check)
            print("Null columns dropped successfully.")
            print(column)
        else:
            print("No nullable columns found in the table.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        
        session.close()


drop_null_columns('YELP_ACADEMIC_DATASET_CHECKIN')
