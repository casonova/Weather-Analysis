from datetime import datetime
import logging
import argparse
import Analyze_Data
import load_data as ld

# Configure logging to save log messages to a file
logging.basicConfig(filename='weather_analysis.log', level=logging.INFO)

# Initialize a variable to hold the data
Data = None

def import_data(file_name):
    global Data
    if Data is not None:
        print("Data is already imported. Use 'analyze' command to perform analysis.")
    else:
        print(f"Importing data from {file_name}...")
        # Import data from a CSV file
        Data = ld.import_csv_file(file_name)
        if Data is not None:
            # Log successful data import
            logging.info("Data imported successfully")
            print("Data imported successfully")

            # Replace missing values in specified columns with column means
            columns_to_fill = {1:"Temp", 2:"WindGustSpeed", 3:"Humidity"}
            for column_id, column_name in columns_to_fill.items():
                Data[column_name].fillna(Data[column_name].mean(), inplace=True)

            # Log that missing values have been replaced
            logging.info("Missing values replaced with column means")
        else:
            # Log an error if the file is not found or could not be imported
            logging.error(f"File not found or could not be imported: {file_name}")
            print(f"File not found or could not be imported: {file_name}")

def analyze_data(data, start_date, end_date):
    if data is None:
        print("Data is not imported. Use 'import' command to import the data first.")
        return

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        if (
            start_date < datetime(2016, 1, 3)
            or start_date > datetime(2017, 2, 1)
            or end_date < datetime(2016, 1, 3)
            or end_date > datetime(2017, 2, 1)
        ):
            raise ValueError("Start date or end date is not within the valid range.")

        if end_date < start_date:
            raise ValueError("End date cannot be before the start date.")

        # Perform data analysis and save results to a file
        output_file = "Analysis.txt"
        print("Performing data analysis...")
        Analyze_Data.analysis(data, start_date, end_date, output_file)

        # Log that analysis results have been saved
        logging.info(f"Analysis results have been saved to {output_file}")
        print(f"Analysis results have been saved to {output_file}")

    except ValueError as e:
        print(f"Error: {str(e)}")
        logging.error(f"Invalid input: {str(e)}")

    
def main():
    parser = argparse.ArgumentParser(description="Weather Data Analysis CLI")

    subparsers = parser.add_subparsers(dest="command", help="Subcommands")
    
    # Subparser for the "import" command
    import_parser = subparsers.add_parser("import", help="Import weather data")
    import_parser.add_argument("file", help="CSV file name")

    # Subparser for the "analyze" command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze weather data")
    analyze_parser.add_argument("file", help="CSV file name")
    analyze_parser.add_argument("--start_date", required=True, help="Starting date in format YYYY-MM-DD")
    analyze_parser.add_argument("--end_date", required=True, help="Ending date in format YYYY-MM-DD")

    args = parser.parse_args()

    if args.command == "import":
        import_data(args.file)
    elif args.command == "analyze":
        analyze_data(args.file, args.start_date, args.end_date)


if __name__ == "__main__":
    print("Welcome to Weather Data Analysis CLI")
    main()


