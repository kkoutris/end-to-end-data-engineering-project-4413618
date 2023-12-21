from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from .assets import resources

all_assets = load_assets_from_modules([assets])

# define a job that will materialize the assets
big_star_job = define_asset_job("big_star_job", selection=AssetSelection.all())

# ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
update_job_schedule = ScheduleDefinition(
    job=big_star_job,
    cron_schedule="0 * * * *",  # every hour
)


defs = Definitions(assets=all_assets, resources=resources,jobs=[big_star_job], schedules=[update_job_schedule])