import snowflake.snowpark
from snowflake.snowpark import Session

conn = {
    "user": "BINDU",
    "password": "B!ndu@41",
    "account": "jfduvyp-sb86292",
    "warehouse": "COMPUTE_WH",
    "database": "FIVETRAN_DATABASE",
    "schema": "SNOW_SCHEMA"
}

session = Session.builder.configs(conn).create()

sql = (
    "CREATE OR REPLACE PROCEDURE states_pro_loc(from_table STRING)\n"
    "   RETURNS TABLE()\n"
    "    LANGUAGE PYTHON \n"
    "    RUNTIME_VERSION ='3.8'\n"
    "    PACKAGES = ('snowflake-snowpark-python')\n"
    "    HANDLER = 'data_fun'\n"
    "AS\n"
    "$$\n"
    "import pandas as pd\n"
    
    "def data_fun(session, from_table):\n"
    "    df_business = session.table(from_table)\n"
    "    pd_df = df_business.to_pandas()\n"
    "    data_df = session.createDataFrame(pd_df)\n"
    "    state = [\n"
    "        ('CA', 'California'), ('MO', 'Missouri'), ('AZ', 'Arizona'), ('TN', 'Tennessee'), ('FL', 'Florida'),\n"
    "        ('IN', 'Indiana'), ('LA', 'Louisiana'), ('AB', 'Alberta'), ('NV', 'Nevada'), ('ID', 'Idaho'),\n"
    "        ('NJ', 'New Jersey'), ('IL', 'Illinois'), ('CO', 'Colorado'), ('WA', 'Washington'), ('TX', 'Texas'),\n"
    "        ('UT', 'Utah'), ('MT', 'Montana'), ('MI', 'Michigan'), ('SD', 'South Dakota'), ('VT', 'Vermont'),\n"
    "        ('PA', 'Pennsylvania'), ('DE', 'Delaware'), ('NC', 'North Carolina'), ('HI', 'Hawaii'),\n"
    "       ('XMS', 'Xaimas'), ('MA', 'Massachusetts'), ('VI', 'Virgin Islands')\n"
    "    ]\n"
    "    state_df = session.createDataFrame(state, ['state', 'state_names'])\n"
    "    result_df = data_df.join(state_df, data_df['state'] == state_df['state'], 'left') "  
    "    .select(data_df['name'], data_df['city'], state_df['state_names'])\n" 
    "$$;"
)


result = session.sql(sql)
result.show()
sql_call = "CALL states_pro_loc('YELP_ACADEMIC_DATASET_BUSINESS');"
result1 = session.sql(sql_call)
result1.show()
