print("Welcome to car rentals!")
carry_on = input("Would you like to continue (y/n)? ")

while carry_on == 'y':
    customer_code = input("Customer code (b or d): ")
    number_days = int(input("Number of days: "))
    odometer_start = int(input("Odometer reading at the start: "))
    odometer_end = int(input("Odometer reading at the end: "))
    #input sem ég nota í útreikninga

    miles_driven = (odometer_end - odometer_start)
    b_budget = 40 * number_days + 0.25 * miles_driven
    d_budget = 60 * number_days + 0.25 * (miles_driven - number_days*100)
    #útreikningar

    
    if customer_code == 'b':
        print("Miles driven:", miles_driven)
        print("Amount due:", float(round(b_budget,1)))
        #passa að amount komi út sem float og námunda með round
    elif customer_code == 'd':
        print("Miles driven:", miles_driven)
        print("Amount due:", float(round(d_budget,1)))
        #passa að amount komi út sem float og námunda með round
    
    carry_on = input("Would you like to continue (y/n)? ")
    #Set aftur neðst svo að forritið spyrji aftur þessa spurningu


