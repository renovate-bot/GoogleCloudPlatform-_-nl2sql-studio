"""
  Chain of Thought Executor Sample
"""
import json

# import os
import sys
from os.path import dirname, abspath
from loguru import logger

from nl2sql.llms.vertexai import text_bison_32k
from nl2sql.executors.linear_executor.core import CoreLinearExecutor
from nl2sql.tasks.table_selection.core import CoreTableSelector
from nl2sql.tasks.table_selection.core import prompts as cts_prompts
from nl2sql.tasks.column_selection.core import (
    CoreColumnSelector,
    prompts as ccs_prompts,
)
from nl2sql.tasks.sql_generation.core import CoreSqlGenerator
from nl2sql.tasks.sql_generation.core import prompts as csg_prompts

sys.path.insert(1, dirname(dirname(abspath(__file__))))

dataset_name = "nl2sql_spider"  # @param {type:"string"}
f = open("../utils/spider_md_cache.json", encoding="utf-8")
spider_data = json.load(f)
data_dictionary_read = {
    "nl2sql_spider": {
        "description": "This dataset contains information about the concerts\
                      singers, country they belong to, stadiums where the  \
                      concerts happened",
        "tables": spider_data,
    },
}

llm = text_bison_32k()
# Disabling logs because these steps generate a LOT of logs.
logger.disable("nl2sql.datasets.base")
core_table_selector = CoreTableSelector(
    llm=llm, prompt=cts_prompts.CURATED_FEW_SHOT_COT_PROMPT
)
core_column_selector = CoreColumnSelector(
    llm=llm, prompt=ccs_prompts.CURATED_FEW_SHOT_COT_PROMPT
)
core_sql_generator = CoreSqlGenerator(
    llm=llm, prompt=csg_prompts.CURATED_FEW_SHOT_COT_PROMPT
)
logger.enable("nl2sql.datasets.base")

bigquery_connection_string = "bigquery://sl-test-project-363109/nl2sql_spider"
dataset_name = "nl2sql_spider"

dd_cot_executor = CoreLinearExecutor.from_connection_string_map(
    {dataset_name: bigquery_connection_string},
    core_table_selector=core_table_selector,
    core_column_selector=core_column_selector,
    core_sql_generator=core_sql_generator,
    data_dictionary=data_dictionary_read,
)

print("\n\n", "=" * 25, "Executor Created", "=" * 25, "\n\n")
print("Executor ID :", dd_cot_executor.executor_id)

# # Now run the executor with a sample question

dd_cot_result = dd_cot_executor(
    db_name=dataset_name,
    question="What is the average, minimum, and maximum age \
             of all singers from France ?",  # @param {type:"string"}
)
print("\n\n", "=" * 50, "Generated SQL", "=" * 50, "\n\n")
print("Result ID:", dd_cot_result.result_id, "\n\n")
print(dd_cot_result.generated_query)
