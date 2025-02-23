# flink_processing.py

from pyflink.datastream import StreamExecutionEnvironment # type: ignore
from pyflink.table import StreamTableEnvironment # type: ignore

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

# Define a Flink job for sentiment analysis
t_env.execute_sql("""
    CREATE TABLE social_media (
        text STRING,
        platform STRING
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'social_media',
        'properties.bootstrap.servers' = 'localhost:9092',
        'format' = 'json'
    )
""")

result = t_env.sql_query("SELECT text, platform FROM social_media")
result.execute().print()