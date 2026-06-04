import sys

from metadata_reader import load_metadata
from pipeline_executor import run_pipeline


def main():

    # =================================================
    # STEP 1 → GET PIPELINE ID
    # =================================================
    if len(sys.argv) < 2:

        print(
            "Usage: python main.py <pipeline_id>"
        )

        return

    pipeline_id = sys.argv[1]

    # =================================================
    # STEP 2 → LOAD METADATA
    # =================================================
    metadata_df = load_metadata(
        pipeline_id
    )

    if metadata_df.empty:

        print(
            f"No pipeline found for "
            f"pipeline_id = {pipeline_id}"
        )

        return

    # =================================================
    # STEP 3 → RUN PIPELINE
    # =================================================
    for _, row in metadata_df.iterrows():

        print(
            f"\nRunning pipeline: "
            f"{row['pipeline_name']} "
            f"({row['pipeline_mode']})"
        )

        try:

            result = run_pipeline(row)

            # -----------------------------------------
            # ENTERPRISE MULTI-FILE INGESTION
            # -----------------------------------------
            if isinstance(result, int):

                print(
                    f"Completed: "
                    f"{result} rows processed"
                )

            # -----------------------------------------
            # DATAFRAME RETURN
            # -----------------------------------------
            else:

                print(
                    f"Completed: "
                    f"{len(result)} rows processed"
                )

        except Exception as e:

            print(f"❌ Failed: {e}")


if __name__ == "__main__":

    main()