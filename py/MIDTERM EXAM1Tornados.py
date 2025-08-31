def tornado_scanner():
    # Get and validate the number of reports
    number_of_reports = int(input("Please enter the number of reports: \n"))
    while number_of_reports <= 0: 
        print("Invalid number of reports. You must have at least 1 report.")
        number_of_reports = int(input("Please enter the number of reports: \n"))
    
    Advisory_types = ['No warning required', 'High Wind Advisory', 'High Wind Warning']
    
    # Loops through each report
    for reports in range(1, number_of_reports + 1):
        wind_report = input("Please enter the report number: \n")
        wind_speed = int(input("Please enter the windspeed: \n"))
        
        # Validate wind speed
        while wind_speed < 1:
            print("Invalid wind speed. Wind speed must be at least 1 mph.")
            wind_speed = int(input("Please enter the windspeed: \n"))
        
        # Determine advisory type based on wind speed
        if 1 <= wind_speed <= 45:
            advisories = Advisory_types[0]
        elif 46 <= wind_speed <= 57:
            advisories = Advisory_types[1]
        else:  # wind_speed >= 58
            advisories = Advisory_types[2]
        
        # Print the report details in formatted columns
        print(f"\nWind Report: {reports}")
        print(f"{'Report number':<50} {wind_report:<50}")
        print(f"{'Wind Speed':<50} {wind_speed:<50}")
        print(f"{'Warning:':<50} {advisories:<50}")

# Call the function
tornado_scanner()