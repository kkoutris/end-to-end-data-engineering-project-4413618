## Data Engineering Project
The project shows the flow of data from a Postgres database to a BigQuery data warehouse. For the creation of this data pipeline we used Airbyte as our integration tool to connect the data from the source (Postgres database) to the last destination (BigQuery data warehouse). For the transofrmation of the data we used dbt. Lastly to manage the pipeline better we used Dagster.


<img src="/overview.png" alt="Alt text" title="Overview">

## Prerequisites
Ensure you have Python 3 installed. If not, you can download and install it from Python's official website.

## Installing
1. Fork the Repository:
    - Click the "Fork" button on the top right corner of this repository.
2. Clone the repository:
    - `git clone https://github.com/YOUR_USERNAME/end-to-end-data-engineering-project-4413618.git`
    - Note: Replace YOUR_USERNAME with your GitHub username
3. Navigate to the directory:
    - `cd end-to-end-data-engineering-project-4413618`
4. Set Up a Virtual Environment:
    - For Mac:
        - `python3 -m venv venv` 
        - `source venv/bin/activate`
    - For Windows:
        - `python -m venv venv`
        - `.\venv\Scripts\activate`
5. Install Dependencies:
    - `pip install -e ".[dev]"`
