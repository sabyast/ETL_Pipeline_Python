# etl.py - Python ETL (Extract, Transform, Load) application using Spark DataFrame to process data
# from a dummy URL API and load it into a MySQL database table.

import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

class ETL:
    def __init__(self, url):
        # Constructor to initialize the ETL class with the dummy URL API endpoint.
        self.url = url
        self.spark = SparkSession.builder \
            .appName("ETLJob") \
            .getOrCreate()

    def extract(self):
        # Extract data from the dummy URL API.
        response = requests.get(self.url)
        data = response.json()
        return data

    def transform(self, data):
        # Perform data transformation using Spark DataFrame.
        # Create a Spark DataFrame from the extracted data and apply data manipulation steps.
        spark_df = self.spark.createDataFrame(data)
        
        # Advanced data transformation using Spark DataFrame.
        # Renaming columns, filtering data, and selecting specific columns.
        transformed_df = spark_df.select(
            col("name").alias("full_name"),
            col("age"),
            col("email"),
            col("address.city").alias("city"),
            col("address.country").alias("country")
        ).filter(col("age") > 18)
        
        return transformed_df

    def load(self, df, db_config):
        # Load the transformed data into the MySQL database.
        # Use JDBC to connect to the MySQL database and save the data.
        df.write \
            .format("jdbc") \
            .option("url", db_config["url"]) \
            .option("dbtable", db_config["table"]) \
            .option("user", db_config["username"]) \
            .option("password", db_config["password"]) \
            .mode("overwrite") \
            .save()

    def run(self):
        # Main ETL process flow.
        data = self.extract()
        transformed_data = self.transform(data)
        db_config = self.read_config("config/database.conf")  # Read MySQL database configuration
        self.load(transformed_data, db_config)

    def read_config(self, file_path):
        # Read configuration file and return a dictionary of configurations.
        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return config

if __name__ == "__main__":
    # Main entry point of the program.
    url = "dummy_url_api"
    etl = ETL(url)
    etl.run()
