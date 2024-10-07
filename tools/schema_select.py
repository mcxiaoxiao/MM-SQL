from tools.sql_execute import sqlite_execute as execute
import os
import pandas as pd
import json


def sql_evoke(query, db_name):
    result, execution_time, executable = execute(
        "datasets/cosql_dataset/database/" + db_name + "/" + db_name + ".sqlite",
        query,
    )
    return result


def schema_select(dbname, table_config):
    """
    Retrieves the database description, filtering tables and columns
    based on the provided configuration.

    Args:
        dbname (str): The name of the database.
        table_config (dict): A dictionary specifying which tables and
                             columns to keep or drop. Keys are table names,
                             values are either:
                                - "drop_all" to drop the entire table,
                                - "keep_all" to keep the entire table, or
                                - a list of column names to keep.

    Returns:
        str: The formatted database description with the selected tables
             and columns, including example data.
    """

    filepath = "datasets/cosql_dataset/tables.json"

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    result = [item for item in data if "db_id" in item and item["db_id"] == dbname]

    if not result:
        return " none "

    table_names_original = result[0]["table_names_original"]
    column_names_original = result[0]["column_names_original"]
    column_names = result[0]["column_names"]
    column_types = result[0]["column_types"]
    primarys = result[0]["primary_keys"]

    desc = ""
    for table_index, table_name in enumerate(table_names_original):

        
        
        if table_name in table_config:
            
            if table_config[table_name] == "drop_all":
                continue

            desc += "Table:" + table_name + "\n[\n"

            for column_index, column_value in enumerate(column_names_original):
                if (column_value[0] == table_index
                    and (table_config[table_name] == "keep_all"
                    or column_value[1] in table_config[table_name]
                    )):
                    isp = " PRIMARY KEY" if column_index in primarys else ""
                    
                    # 获取当前列的 example 数据
                    sql_get_eg = f"SELECT DISTINCT {column_value[1]} FROM {table_name} LIMIT 3;"
                    examples_raw = sql_evoke(sql_get_eg, dbname)
                    examples = ", ".join([str(row[0]) for row in examples_raw])

                    desc += (
                        '('
                        + column_value[1]
                        + ":"
                        + column_names[column_index][1]
                        + " type:"
                        + column_types[column_index]
                        + isp
                        + " Value examples:"
                        + examples
                        + "),\n"
                    )
            desc = desc.rstrip("|") + "]\n"

    return desc
