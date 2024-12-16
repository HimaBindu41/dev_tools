# # import snowflake.snowpark
# from snowflake.snowpark import Session

# conn_parm ={
#     "user":"BINDU",
#     "password":"B!ndu@41",
#     "account":"jfduvyp-sb86292",
#     "warehouse":"COMPUTE_WH",
#     "database":"FIVETRAN_DATABASE",
#     "schema":"SNOW_SCHEMA"
# }
# session=Session.builder.configs(conn_parm).create()

# # tipS_df = session.table("YELP_ACADEMIC_DATASET_TIP")
# tip_df=session.sql("select * from  YELP_ACADEMIC_DATASET_TIP limit 10")
# my_tip_parm={'QUERY_TAG':'test_limit'}
# tip_df.show(n=5,max_width=100,statement_params=my_tip_parm)
# session.close()

from snowflake.snowpark import Session
conn_parm ={
    "user":"BINDU",
    "password":"B!ndu@41",
    "account":"jfduvyp-sb86292",
    "warehouse":"COMPUTE_WH",
    "database":"HB_DB",
    "schema":"HB_DB_SCHEMA"
}
session=Session.builder.configs(conn_parm).create()

from snowflake.snowpark.functions import col, concat, lit, lower, replace

df_table = session.table("emp")
df_transformed = df_table.withColumn("email", concat(lower(replace(col("first_name"), " ", "")), lower(col("last_name")), lit("@gmail.com")))
df_transformed.show()

# df_deduplicated = df_transformed.drop_duplicates()
# df_deduplicated.show()

