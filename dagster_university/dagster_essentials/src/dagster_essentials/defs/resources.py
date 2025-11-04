import dagster as dg
from dagster_duckdb import DuckDBResource


database_resource = DuckDBResource(
    database=dg.EnvVar("DUCKDB_DATABASE")      # replaced with environment variable
)

@dg.definitions
def resources() -> dg.Definitions:
    return dg.Definitions(resources={"database": database_resource})
