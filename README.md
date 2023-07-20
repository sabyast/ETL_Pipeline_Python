# ETL_Pipeline_Python

# ETLApp - Extract, Transform, Load Application

ETLApp is a Python-based ETL (Extract, Transform, Load) application that leverages Spark DataFrame to process data from a dummy URL API and load it into a MySQL database table. The application is designed to simplify the process of data extraction, transformation, and loading for your data pipeline.

## Overview

The ETLApp performs the following steps:

1. **Extract**: The application extracts data from a dummy URL API. You can replace the URL with your actual data source.

2. **Transform**: Using Spark DataFrame, the extracted data is transformed and manipulated to meet specific data requirements. In this example, the application renames columns, filters data, and selects specific columns.

3. **Load**: The transformed data is loaded into a MySQL database table. You need to provide your MySQL database details in the configuration file.

## Installation

Follow these steps to install and set up the ETLApp on your machine:

1. Clone the repository:


2. Navigate to the project directory:


3. Install dependencies:


The installation will also install the necessary dependencies: pyspark, requests, and mysql-connector-python.

## Configuration

Before running the ETLApp, you need to set up the database configuration. Create a file named `database.conf` inside the `config` directory with the following format:


Replace the placeholders `<database_host>`, `<port>`, `<database_name>`, `<your_username>`, `<your_password>`, and `<target_table_name>` with your actual MySQL database details. Ensure that the specified table exists in the provided database, and the specified user has the necessary privileges to access and modify the table.

## Usage

To run the ETLApp, execute the following command in the terminal or command prompt:


The ETL process will start, extracting data from the dummy URL API, transforming it using Spark DataFrame, and loading the transformed data into the specified MySQL database table.

## Dependencies

The ETLApp relies on the following dependencies:

- pyspark
- requests
- mysql-connector-python

These dependencies will be installed automatically during the setup process.

## Contributing

Contributions to the ETLApp are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

The ETLApp is open-source and licensed under the [MIT License](LICENSE).

Happy ETLing!
