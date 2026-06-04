from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


default_args = {

    "owner": "haritha",

    "depends_on_past": False,

    "start_date": datetime(2025, 1, 1),

    "retries": 1

}


def get_pipeline_metadata():

    hook = PostgresHook(
        postgres_conn_id="metadata_db"
    )

    records = hook.get_records(
        """
        SELECT

            pipeline_id,

            pipeline_name,

            cron_expression

        FROM pipeline_master

        WHERE is_active = TRUE

        ORDER BY pipeline_id
        """
    )

    return records


pipelines = get_pipeline_metadata()


for row in pipelines:

    pipeline_id = row[0]

    pipeline_name = row[1]

    cron_expression = row[2]


    dag = DAG(

        dag_id=pipeline_name,

        default_args=default_args,

        schedule=cron_expression,

        catchup=False,

        tags=["metadata","dynamic"]

    )


    with dag:

        BashOperator(

            task_id=f"run_{pipeline_name}",

            bash_command=(

                f"cd /opt/airflow/src && "

                f"python main.py {pipeline_id}"

            )

        )


    globals()[pipeline_name] = dag