import snowflake.snowpark
from snowflake.snowpark import Session
conn={
        "user":"BINDU",
        "password":"B!ndu@41",
        "account":"jfduvyp-sb86292",
        "warehouse":"COMPUTE_WH",
        "database":"FIVETRAN_DATABASE",
        "schema":"SNOW_SCHEMA"
    }


session=Session.builder.configs(conn).create()
# df_check=session.table("YELP_ACADEMIC_DATASET_BUSINESS")
# df_busi=df_check.select('address').collect()
# for i in df_busi:
#     print(i)

sql=(
    "CREATE OR REPLACE PROCEDURE FIRST_P(from_table STRING) \n "
    "RETURNS TABLE() \n "
    "LANGUAGE PYTHON \n "
    "RUNTIME_VERSION ='3.8'\n "
    "PACKAGES = ('snowflake-snowpark-python')\n "
    "HANDLER = 'data'\n "
"AS \n "
"$$ \n"
"import pandas  \n"
"def data(session,from_table):\n"
"   result =session.table(from_table )\n"
"   data_df=result.to_pandas()\n"
"   display=session.createDataFrame(data_df)\n"
"   return display \n "
"$$;")
result=session.sql(sql)
# result.show()
sql_call="CALL FIRST_P('YELP_ACADEMIC_DATASET_BUSINESS'); "
result1=session.sql(sql_call)
result1.show(2)

