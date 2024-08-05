from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, NoSuchElementException, TimeoutException
import time, csv, os


# Variables Declaration
driver = webdriver.Chrome()
get_times = False
username = ""
password = ""
location_to_search = "fremont"
sport_to_search = "basketball"
csv_file = "facilitron_scrape_sample.csv"
number_of_months = -10 # for the number of months to scrape the timings for

# Log In to Facilitron
driver.get("https://www.facilitron.com/accounts/signin/")

# Wait for username field
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Locate the email field and enter the email
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(username)

next_button = driver.find_element(By.CLASS_NAME, "btn")
next_button.click()

# Wait for password field
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "password"))
)
# Locate the password field and enter the password
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)

log_in_button = driver.find_element(By.CLASS_NAME, "btn")
log_in_button.click()
time.sleep(10) #waiting for log in, bottle neck

driver.get("https://www.facilitron.com/")
number_of_days = 120


# Adding to our csv
def add_to_csv(facility_id, facility_title, location, image_url, link, sport_name, year, month, day, time_slot, price):
    # Define the header
    header = ['Facility ID', 'Facility Title', 'Location', 'Image URL', 'Link', 'Sport Name', 'Year', 'Month', 'Day', 'Time Slot', 'Price']

    # Check if the CSV file exists
    file_exists = os.path.isfile(csv_file)

    # Open the CSV file in append mode
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writeheader()

        # Write the data
        writer.writerow({
            'Facility ID': facility_id,
            'Facility Title': facility_title,
            'Location': location,
            'Image URL': image_url,
            'Link': link,
            'Sport Name': sport_name,
            'Year': year,
            'Month': month,
            'Day': day,
            'Time Slot': time_slot,
            'Price': price
        })

# Define the function to add data to the CSV file
def add_to_csv_2(facility_title, city, sport_name, location, street_address, zip_code, google_map_embed, description, thumbnail, social_image, all_images, hourly_rate, display_price, list_of_sports, link):
	# Define the header
	header = ['Facility Name', 'City', 'Type', 'Location', 'Street Address', 'Zip Code', 'Google Map Embed',
	          'Listing Description', 'Continent', 'Thumbnail', 'Social:Image', 'Listing Images', 'Hourly Rate',
	          'Display Price', 'Sports', 'Booking Link', 'Rentals Page (INTERNAL USE)', 'Rating', 'Approved',
	          'Manager', 'Email (from Host)', 'Picture (from Host)', 'User (from Host)', 'Host Name (from Host)',
	          'Host Email', 'Users', 'Activities', 'Booking Requests', 'SEO:Index', 'SEO:Title',
	          'SEO:Description', 'Social:Title', 'Social:Description', 'SEO:Slug', 'Activity Reviews (from Activities)',
	          'Latitude', 'Longitude']

	# Check if the CSV file exists
	file_exists = os.path.isfile(csv_file)

	# Open the CSV file in append mode
	with open(csv_file, mode='a', newline='') as file:
		writer = csv.DictWriter(file, fieldnames=header)

		# If the file doesn't exist, write the header
		if not file_exists:
			writer.writeheader()
		# Write the data
		writer.writerow({
			'Facility Name': facility_title,
			'City': city,
			'Type': sport_name,
			'Location': location,
			'Street Address': street_address,
			'Zip Code': zip_code,
			'Google Map Embed': google_map_embed,
			'Listing Description': description,
			'Continent': 'North America',
			'Thumbnail': thumbnail,
			'Social:Image': social_image,
			'Listing Images': all_images,
			'Hourly Rate': hourly_rate,
			'Display Price': display_price,
			'Sports': list_of_sports,
			'Booking Link': link,
		})
# Outer Dictionary: Keys are years (e.g., 2023, 2024).
# Second Level Dictionary: Keys are months (e.g., 1, 2, ..., 12).
# Innermost Dictionary: Keys are day numbers (e.g., 1 to 31) and values are lists of available time slots.
# Initialize the availability dictionary
availability = {
    2024: {
        1: {day: [] for day in range(1, 32)},
        2: {day: [] for day in range(1, 32)},
        3: {day: [] for day in range(1, 32)},
        4: {day: [] for day in range(1, 32)},
        5: {day: [] for day in range(1, 32)},
        6: {day: [] for day in range(1, 32)},
        7: {day: [] for day in range(1, 32)},
        8: {day: [] for day in range(1, 32)},
        9: {day: [] for day in range(1, 32)},
        10: {day: [] for day in range(1, 32)},
        11: {day: [] for day in range(1, 32)},
        12: {day: [] for day in range(1, 32)}
    },
    2025: {
        1: {day: [] for day in range(1, 32)},
        2: {day: [] for day in range(1, 32)},
        3: {day: [] for day in range(1, 32)},
        4: {day: [] for day in range(1, 32)},
        5: {day: [] for day in range(1, 32)},
        6: {day: [] for day in range(1, 32)},
        7: {day: [] for day in range(1, 32)},
        8: {day: [] for day in range(1, 32)},
        9: {day: [] for day in range(1, 32)},
        10: {day: [] for day in range(1, 32)},
        11: {day: [] for day in range(1, 32)},
        12: {day: [] for day in range(1, 32)}
    },
}

# Input the location and activity into facilitron
print("At this point")
driver.refresh()
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "facilityLocationSearchBox"))
)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "facilityLocationSearchBox"))
)
location_input = driver.find_element(By.ID, "facilityLocationSearchBox")
location_input.send_keys(location_to_search)

activity_input = driver.find_element(By.ID, "facilityActivitySearchBox")
activity_input.send_keys(sport_to_search)


driver.implicitly_wait(10)
time.sleep(10)


activity_input.send_keys(Keys.RETURN)
# Wait for the page to load the facilities
WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.CLASS_NAME, "facility-card__label"))
)

# Find the number of pages to scroll through
try:
    page_buttons = driver.find_elements(By.CLASS_NAME, "v-pagination__item")
    number_of_pages = int(page_buttons[-1].text)
    print(number_of_pages)
except:
    number_of_pages = 0

# Get the number of facilities
number_of_facilities = driver.find_element(By.XPATH,
                                           "/html/body/div/div/div/div/div[2]/main/div/div/div[2]/div[1]/div[1]/div/span")
number_of_facilities = number_of_facilities.text
number_of_facilities = (number_of_facilities.split(" "))[0]
facilities_searched_through = 0

counter = 0

# Function to remove all whitespace characters
def remove_all_whitespace(s):
    return ''.join([char for char in s if char.isnumeric()])

def fetch_facilities():
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "facility-card__label"))
    )
    return driver.find_elements(By.CLASS_NAME, "facility-card__label")

# For the number of pages we have, we are going to access the facility
for counter in range(0, number_of_pages + 1):
    print("123")
    # Wait for the page to load the facilities
    facilities = fetch_facilities()

    # If we have facilities to access, then we will click on it and perform our scraping
    if facilities:
        time.sleep(5)
        facilities = fetch_facilities()
        facility_index = 0
        for facility_index in range(0,len(facilities)):
            retries = 3
            while retries > 0:
                try:
                    facilities = fetch_facilities()
                    facility = facilities[facility_index]
                    facility_text = facility.text
                    print(facility_text)
                    # Scroll the element into view before clicking
                    driver.execute_script("arguments[0].scrollIntoView(true);", facility)
                    # Wait until the element is clickable
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "facility-card__label")))
                    # Use JavaScript to click the element
                    driver.execute_script("arguments[0].click();", facility)

                    #open tab that we want to work on
                    parent = driver.window_handles[0]
                    chld = driver.window_handles[1]
                    driver.switch_to.window(chld)

                    #wait for it to load
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "facility-card__label"))
                    )

                    #scrape the name
                    facility_name = driver.find_element(By.CLASS_NAME, "facility-card__label").text
                    print(facility_name);

                    #scrape the address
                    facility_address = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/main/div/div/div[1]/div/div[1]/div[2]/div/span").text
                    print("Facility Address: " , facility_address);

                    # Split the address into its components
                    parts = facility_address.split(", ")

                    # Extract specific address, city, state, and zip code
                    specific_address = parts[0]
                    city = parts[1]
                    state_zip = parts[2].split(" ")
                    state = state_zip[0]
                    zip_code = state_zip[1]

                    # Print the components
                    print("Specific Address:", specific_address)
                    print("City:", city)
                    print("State:", state)
                    print("Zip Code:", zip_code)


                    #scrape the url
                    current_url = driver.current_url
                    print("current_url " , current_url)

                    #scrape the images into an array
                    facility_images = driver.find_elements(By.CLASS_NAME, "banner-img__img")
                    facility_image_list = []
                    for image in facility_images:
                        facility_image_list.append(image.get_attribute('src'))
                        print(image.get_attribute('src'))


                    #scrape the description
                    try:
                        show_more_button = driver.find_element(By.CLASS_NAME, "app-show-more")
                        driver.execute_script("arguments[0].click();", show_more_button)
                    except NoSuchElementException:
                        pass

                    facility_description_and_price_info = driver.find_elements(By.CLASS_NAME, "app-show-more__text")
                    facility_description = facility_description_and_price_info[0].text
                    print("Facility Description: " , facility_description)

                    #scrape the price which requires you to log in
                    facility_price = facility_description_and_price_info[1].text
                    print("hi", facility_price)

                    #scrape the uses/sports into an array or list
                    #1) click the show more if needed
                    try:
                        potential_show_more_buttons = driver.find_elements(By.CLASS_NAME, "v-btn__content" )
                        for i in range(0, len(potential_show_more_buttons)):
                            potential_show_more_buttons = driver.find_elements(By.CLASS_NAME, "v-btn__content")
                            if potential_show_more_buttons[i].text.strip() == "Show more":
                                driver.execute_script("arguments[0].click();", potential_show_more_buttons[i])
                                break;

                        #show_more_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/main/div/div/div[3]/div[1]/div[3]/div/button/span")

                    except NoSuchElementException:
                        print("Button not found")

                    #2) get all the ma-0 elements and find the one that is the sports header
                    list_of_elements = driver.find_elements(By.CLASS_NAME, "ma-0")

                    print()
                    facility_sports_array = {"N/A"}

                    facility_sports_use ="N/A";
                    print("len " , len(list_of_elements))
                    for i in range(0, len(list_of_elements)):
                        if list_of_elements[i].text.strip() == "Sports":
                            facility_sports_use = list_of_elements[i+1].text;
                            facility_sports_array = facility_sports_use.split(" • ")
                            print(facility_sports_array)
                            break;


                    print("sports use " , facility_sports_use)

                    # SEND TO CSV
                    # AT THIS POINT WE HAVE THE FOLLOWING DATA
                    # name, address, images array, description, price, offered sports array, availabilitiy
                    # the date
                    print("ADDING TO CSV")
                    add_to_csv_2(facility_name, city, sport_to_search, facility_address, specific_address,
                                 zip_code, "N/A", facility_description, facility_image_list[0],
                                 facility_image_list[0], facility_image_list, facility_price, facility_price,
                                 facility_sports_array, current_url)


                    #scrape the availabilities into a dictionary
                    if get_times:
	                    number_of_months = 6

                    finished = False;
                    for i in range(1, number_of_months+1):
                        if finished: break

                        print("I AM SCRAPING THE TIMINGS")
                        # wait for it to load
                        WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "v-btn--rounded"))
                        )
                        # Locate all the calendar buttons we can access + a few extra thangs
                        try:
                            calendar_buttons = driver.find_elements(By.CLASS_NAME, 'v-btn--rounded')
                        except NoSuchElementException:
                            continue;

                        # The following code is for scraping the times
                        list_of_days_covered = []
                        list_of_days_covered_test = []
                        button_index = 0
                        stale_counter = 0 # counts how many stale errors have occured
                        successful_button_counter = 0 # used to cover edge cases: 1 and 2
                        for button_index in range(0, len(calendar_buttons)): # go through all the buttons
                            if finished: break
                            try:
                                WebDriverWait(driver, 20).until( #reload buttons to minimize stailness
                                    EC.presence_of_element_located((By.CLASS_NAME, "v-btn--rounded"))
                                )
                                calendar_buttons = driver.find_elements(By.CLASS_NAME, 'v-btn--rounded')

                                if button_index >= len(calendar_buttons):
                                    print("Breaking because of this")
                                    break  # Check immediately after re-fetching the list

                                current_button = calendar_buttons[button_index]  # get the current calendar button
                                try:
                                    day = current_button.find_element(By.CSS_SELECTOR, 'div.v-btn__content').text.strip() # try to access a day
                                    list_of_days_covered_test.append(day)
                                    if day not in list_of_days_covered:  # if it is an available date
                                        list_of_days_covered.append(day);  # add to our list of days
                                        print("Performing operations on calendar date")
                                        # we click the button no matter what
                                        driver.execute_script("arguments[0].click();", current_button)
                                        #PERFORM ACTIONS: scrape our available times

                                        calendar_times_list = []
                                        calendar_times_index = 0
                                        try:
                                            print("We are testing this day : " , day)
                                            WebDriverWait(driver, 0.05).until(  # reload buttons to minimize stailness
                                                EC.presence_of_element_located((By.CLASS_NAME, "booking-time-table__el"))
                                            )

                                            #if we are here we were successful and HAVE entered to the goal

                                            # if this works that means that there are available times --> so we want to go back two
                                            WebDriverWait(driver, 5).until(  # reload buttons to minimize stailness
                                                EC.presence_of_element_located(
                                                    (By.CLASS_NAME, "booking-time-arrow"))
                                            )

                                            back_button_to_previous_day = \
                                            driver.find_elements(By.CLASS_NAME, "booking-time-arrow")[0]
                                            driver.execute_script("arguments[0].click();", back_button_to_previous_day)

                                            WebDriverWait(driver, 5).until(  # reload buttons to minimize stailness
                                                EC.presence_of_element_located(
                                                    (By.CLASS_NAME, "booking-time-arrow"))
                                            )
                                            back_button_to_previous_day = \
                                            driver.find_elements(By.CLASS_NAME, "booking-time-arrow")[0]
                                            driver.execute_script("arguments[0].click();", back_button_to_previous_day)

                                            for number_of_days in range(0, number_of_days): # for the number of days we want we will get our timings
                                                calendar_times_list = []

                                                try:
                                                    WebDriverWait(driver, 0.1).until(
                                                        # reload buttons to minimize stailness
                                                        EC.presence_of_element_located(
                                                            (By.CLASS_NAME, "booking-time-table__el"))
                                                    )
                                                    calendar_times = driver.find_elements(By.CLASS_NAME, 'booking-time-table__el')
                                                    for calendar_times_index in range(0, len(calendar_times)): # loop through all of our times
                                                        try:
                                                            calendar_times = driver.find_elements(By.CLASS_NAME,
                                                                                                  'booking-time-table__el')
                                                            current_time = calendar_times[calendar_times_index].text
                                                            calendar_times_list.append(current_time) # add our time to our list
                                                        except StaleElementReferenceException:
                                                            time.sleep(5)
                                                            calendar_times_index -= 1;
                                                            continue;
                                                    date = driver.find_element(By.CLASS_NAME, "booking-time-date").text
                                                    print("date: ", date, "with these timings ", calendar_times_list)



                                                except TimeoutException:
                                                    pass
                                                next_button_to_next_day = driver.find_elements(By.CLASS_NAME, "booking-time-arrow")[1]
                                                driver.execute_script("arguments[0].click();", next_button_to_next_day)
                                            finished = True;
                                            break;
                                        except TimeoutException: # no available times lets just move on from this date
                                            print("No available times found")
                                            continue;


                                        # exit out
                                        WebDriverWait(driver, 20).until(
                                            EC.presence_of_element_located((By.CLASS_NAME, "v-size--x-small"))
                                        )
                                        if finished: break
                                        calendar_back_button = driver.find_elements(By.CLASS_NAME, "v-size--x-small")[0]
                                        driver.execute_script("arguments[0].click();", calendar_back_button)

                                        # after we exit test to see if we have any times for our current day
                                        print("day: ", day , "with these timings " , calendar_times_list)  # print for debugging
                                    counter += 1
                                    stale_counter = 0;
                                    continue;
                                except NoSuchElementException: # that means it doesn't have a text
                                    print("Continuing on because of NoSuchElementException ")
                                    if finished: break
                                    continue;
                            except StaleElementReferenceException:
                                print("StaleElementReferenceException occurred. Retrying calendar button...")
                                stale_counter += 1
                                if finished: break
                                if (stale_counter >= 10):
                                     print("We have tried 10 times. Something is going wrong.")
                                     break;
                                button_index -= 1;
                                time.sleep(5)
                                continue;


                        # exit out
                        WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "v-size--x-small"))
                        )
                        time.sleep(0.1)
                        calendar_back_button = driver.find_elements(By.CLASS_NAME, "v-size--x-small")[0]
                        driver.execute_script("arguments[0].click();", calendar_back_button)

                        print("this is a test to see if the first: " , list_of_days_covered_test)
                        print("\n")

                        # repeat process on next page / month
                        print("Moving on to next month")
                        i += 1;
                        calendar_next_button = driver.find_elements(By.CLASS_NAME, "v-btn--icon")[2]
                        driver.execute_script("arguments[0].click();", calendar_next_button) # move onto the next calendar page


                    #Close the tab and switch back
                    driver.close()
                    driver.switch_to.window(parent)

                    facilities_searched_through += 1
                    break
                except StaleElementReferenceException:
                    print("StaleElementReferenceException occurred. Retrying...")
                    time.sleep(5)
                    retries -= 1
                    facility = fetch_facilities()[facilities.index(facility)]
                    if retries == 0:
                        print("Failed to fetch facility text after 3 retries.")
                        continue
                except ElementClickInterceptedException:
                    print("ElementClickInterceptedException occurred. Retrying...")
                    retries -= 1
                    time.sleep(5)

                    if retries == 0:
                        print("Failed to click facility after 3 retries.")
                        continue

        time.sleep(1)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "v-pagination__navigation"))
        )
        # If we are able to get another page, we will click the next page button and restart
        try:
            navigation_buttons = driver.find_elements(By.CLASS_NAME, "v-pagination__navigation")
            next_button = navigation_buttons[-1]
            next_button.click()
        except:
            print("Number of facilities searched through: " , number_of_facilities)
            print("No next button found.")
            break

    else:
        print("No facilities found.")
        break


# Calender Helper Functions

# Function to check availability (returns the list of times)
def get_availability(year, month, day):
    if year in availability and month in availability[year] and day in availability[year][month]:
        return availability[year][month][day]
    else:
        raise ValueError("Invalid year, month, or day")


# Function to update availability (adds a time slot)
def update_availability(year, month, day, time_slot):
    if year in availability and month in availability[year] and day in availability[year][month]:
        availability[year][month][day].append(time_slot)
    else:
        raise ValueError("Invalid year, month, or day")


# Function to add a new year with availability data
def add_year_availability(year, availability_data):
    if year in availability:
        raise ValueError(f"Year {year} already exists in availability dictionary")

    availability[year] = availability_data



print("Total searched through: " , counter)

driver.quit()
