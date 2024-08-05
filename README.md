# Facilitron Web Scraper
This project is a web scraper for the Facilitron website using Selenium. The scraper logs in to the site, searches for facilities based on specified criteria, and collects detailed information about each facility, including its name, address, images, description, price, and available sports. The collected data is saved in a CSV file for further use.

## Features
Automated Login: Automatically logs in to the Facilitron website using provided credentials.
Facility Search: Searches for facilities based on location and sport.
Data Scraping: Extracts detailed information about each facility, including name, address, images, description, price, and available sports.
Data Storage: Saves the extracted data into a CSV file.
Error Handling: Handles common exceptions like NoSuchElementException, TimeoutException, and StaleElementReferenceException.

## Dependencies
selenium
csv
os
time

## Requirements
Python 3.x
Google Chrome
Install Selenium: Install the Selenium package using pip:
`pip install selenium`

## How to Use
### Clone the Repository: Clone the repository to your local machine.
bash
Copy code
`git clone <repository-url>
cd <repository-directory>`

### Set Up Variables: Update the variable values in the script:
location to search and sport to search are used within the facilitron website as your search inquiry
`username = "your-email@example.com"
password = "your-password"
location_to_search = "your-location"
sport_to_search = "your-sport"
csv_file = "your-csv-file.csv"
number_of_months = your-number-of-months`
### Run the Script: Execute the script:
main.py

## Variable Declarations
driver: Selenium WebDriver instance for Chrome.
get_times: Boolean flag to indicate if time slots should be scraped.
username: User's email for Facilitron login.
password: User's password for Facilitron login.
location_to_search: Location to search for facilities.
sport_to_search: Sport to search for facilities.
csv_file: Name of the CSV file to store scraped data.
number_of_months: Number of months to scrape the timings for.

## Helper Functions
add_to_csv(facility_id, facility_title, location, image_url, link, sport_name, year, month, day, time_slot, price): Adds a row of data to the CSV file.
add_to_csv_2(facility_title, city, sport_name, location, street_address, zip_code, google_map_embed, description, thumbnail, social_image, all_images, hourly_rate, display_price, list_of_sports, link): Adds a row of detailed data to the CSV file.
remove_all_whitespace(s): Removes all whitespace characters from a string.
fetch_facilities(): Fetches the list of facilities from the current page.

## Main Script Logic
Initialize WebDriver: Set up the Chrome WebDriver.
Login: Navigate to the login page and log in using the provided credentials.
Search: Navigate to the main page and perform a search for facilities based on location and sport.
Scrape Data: Iterate through the list of facilities and extract detailed information for each facility.
Save Data: Store the extracted data in a CSV file.
Handle Errors: Implement error handling for common exceptions.

## Notes
Timeouts: The script includes various timeouts to ensure elements are loaded before interactions.
Implicit Waits: The script uses implicit waits to handle dynamic loading of elements.
Error Handling: Exception handling is implemented to manage elements that may not be found or clickable.
The stress testing has been limited on this, but it hasn't crashed under my testing.
Be wary of the legal issues of web scraping for commercial use.

## Future Advancements
Parallel Scraping: Implement parallel scraping to speed up the data collection process.
Extended Error Handling: Improve error handling to manage additional edge cases.
User Interface: Develop a user-friendly interface for setting up search parameters and viewing results.
Additional Data Points: Extract and store more data points as required.
Database Integration: Integrate with a database for more efficient data storage and querying.

### With permission from Facilitron
