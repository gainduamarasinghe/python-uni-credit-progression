#I declare that my work contains no examples of misconduct , such as plagiarism, or collusion.
#Any code taken from other soures is referenced within my code solution.

#Student ID: w20537836

#Date: 10.12.2023


from graphics import *

# List with credit input range
credits_range = [0, 20, 40, 60, 80, 100, 120]

# Variables
total_outcomes = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

# Lists for storing progression data
progress_data = []
trailer_data = []
retriever_data = []
excluded_data = []

# Function for validation part
def correct_inputs(user_input):
    """Check user input is in valid range and input is an integer"""
    while True:
        try:
            get_user_input = int(input(user_input))  # Get input from the user.
            if get_user_input in credits_range:
                return get_user_input
            else:
                print("Out of Range.\n")
        except ValueError:
            print("Integer required.\n")

            
#This input choese the staff user of student user.
person_select = input("Enter '1' for staff use '2' for student use: ")

if (person_select == '1'):
    print("Staff User\n")
    while True:
        while True:
            # Call the function for inputs
            pass_credit = correct_inputs('Please enter your credits at pass: ')
            defer_credit = correct_inputs('Please enter your credits at defer: ')
            fail_credit = correct_inputs('Please enter your credits at fail: ')

            # Get the total of user inputs
            total = pass_credit + defer_credit + fail_credit

            # Checking Total is equal to 120 or not
            if total != 120:
                print("Total incorrect.")
                print()
            else:
                total_outcomes += 1

                # Progression Outcomes
                if pass_credit == 120:
                    print("Progress")
                    progress_count += 1
                    progress_data.append([pass_credit, defer_credit, fail_credit])

                elif pass_credit == 100:
                    print("Progress (module trailer)")
                    trailer_count += 1
                    trailer_data.append([pass_credit, defer_credit, fail_credit])

                elif 0 <= pass_credit <= 80 and 0 <= fail_credit <= 60:
                    print("Do not progress - module retriever")
                    retriever_count += 1
                    retriever_data.append([pass_credit, defer_credit, fail_credit])

                else:
                    print("Exclude")
                    excluded_count += 1
                    excluded_data.append([pass_credit, defer_credit, fail_credit])
                break

        # Multiple Outcomes
        print("\nWould you like to enter another set of data?")

        # Choose for exit and graph
        more_entries = str(input("Enter 'y' for yes or 'q' to quit and view results: ")).lower()

        if more_entries == 'q':
            print()  # Put space after selection

            # Function made for common editing in graph
            def editing_text(name, f_size):
                """Editing x-axis names."""
                name.setTextColor("grey")
                name.setFace("helvetica")
                name.setStyle("bold")
                name.setSize(f_size)
                name.draw(win)
                return name

            # Create the window for histogram
            win = GraphWin("Histogram", 640, 480)

            # Heading 1
            heading_1 = Text(Point(100, 20), "Histogram Results")
            heading_1.setTextColor("black")
            heading_1.setSize(15)
            heading_1.draw(win)

            # Y axis of graph
            yLine = Line(Point(20, 400), Point(580, 400))
            yLine.setFill("grey")
            yLine.draw(win)

            # Axis naming 1(Progress)
            name_1 = Text(Point(115, 410), "Progress")
            editing_text(name_1, 11)

            # Axis naming 2(Trailer)
            name_2 = Text(Point(235, 410), "Trailer")
            editing_text(name_2, 11)

            # Axis naming 3(Retriever)
            name_3 = Text(Point(355, 410), "Retriever")
            editing_text(name_3, 11)

            # Axis naming 4(Excluded)
            name_4 = Text(Point(475, 410), "Excluded")
            editing_text(name_4, 11)

            # Outcomes text
            last_text = Text(Point(110, 430), f'{total_outcomes} outcomes in total.')
            editing_text(last_text, 13)

            # Bar 1(display Progress)
            data_bar1 = Rectangle(Point(60, (400 - (progress_count * 25))), Point(170, 400))
            data_bar1.setFill("lightgreen")
            data_bar1.draw(win)

            # Bar 1 (Progress Total)
            progress_total = Text(Point(115, (390 - (progress_count * 25))), f'{progress_count}')
            editing_text(progress_total, 12)

            # Bar 2 (Display Trailer)
            data_bar2 = Rectangle(Point(180, (400 - (trailer_count * 25))), Point(290, 400))
            data_bar2.setFill("green")
            data_bar2.draw(win)

            # Bar 2 (Trailer Total)
            trailer_total = Text(Point(235, (390 - (trailer_count * 25))), f'{trailer_count}')
            editing_text(trailer_total, 12)

            # Bar 3 (Display Retriever)
            data_bar3 = Rectangle(Point(300, (400 - (retriever_count * 25))), Point(410, 400))
            data_bar3.setFill("yellow4")
            data_bar3.draw(win)

            # Bar 3 (Retriever Total)
            retriever_total = Text(Point(355, (390 - (retriever_count * 25))), f'{retriever_count}')
            editing_text(retriever_total, 12)

            # Bar 4 (Display Exclude)
            data_bar1 = Rectangle(Point(420, (400 - (excluded_count * 25))), Point(530, 400))
            data_bar1.setFill("pink")
            data_bar1.draw(win)

            # Bar 4 (Trailer Total)
            excluded_total = Text(Point(475, (390 - (excluded_count * 25))), f'{excluded_count}')
            editing_text(excluded_total, 12)

            #part2
            print("\nPart 2:")
            for entry in progress_data:
                print("Progress: ", *entry)
            for entry in trailer_data:
                print("Progress (module trailer): ", *entry)
            for entry in retriever_data:
                print("Module retriever: ", *entry)
            for entry in excluded_data:
                print("Exclude: ", *entry)

            #Flexiple. (2023) How to Print a List in Python?. [Online]
            #Available from: https://flexiple.com/python/python-print-list#section2
            #[Accessed: 2nd December 2023].
                
            print() # Get space between part 2 and 3
            
            #part3
            data = open('Outputs.txt','wt')
            data.write('Part 3:\n')
            data.close()

            data = open('Outputs.txt','a')
            for entry in progress_data:
                data.write(f'Progress: {entry[0]} {entry[1]} {entry[2]}\n')
            for entry in trailer_data:
                data.write(f'Progress (module trailer): {entry[0]} {entry[1]} {entry[2]}\n')
            for entry in retriever_data:
                data.write(f'Module retriever: {entry[0]} {entry[1]} {entry[2]}\n')
            for entry in excluded_data:
                data.write(f'Exclude: {entry[0]} {entry[1]} {entry[2]}\n')
            data.close()
            
            data = open('Outputs.txt','r')
            result = data.readlines()
            print(*result)
            data.close()

            break
        elif more_entries == 'y':
            print()  # Put space after selection
        else:
            print("Invalid Selection")
            print()
            
elif (person_select == '2'):
    print("Student User\n")
    pass_credit = correct_inputs('Please enter your credits at pass: ')
    defer_credit = correct_inputs('Please enter your credits at defer: ')
    fail_credit = correct_inputs('Please enter your credits at fail: ')

    # Get the total of user inputs
    total = pass_credit + defer_credit + fail_credit

    # Checking Total is equal to 120 or not
    if total != 120:
        print("Total incorrect.")
        print()
    else:
        total_outcomes += 1
        
        # Progression Outcomes
        if pass_credit == 120:
            print("Progress")            
        elif pass_credit == 100:
            print("Progress (module trailer)")           
        elif 0 <= pass_credit <= 80 and 0 <= fail_credit <= 60:
            print("Do not progress - module retriever")        
        else:
            print("Exclude")
else:
    print("Invalid user Selection")
