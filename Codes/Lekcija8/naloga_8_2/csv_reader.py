with open("people.csv", "r") as file: 
        for line in file:
            row_data = line.strip().split(",")
            name = row_data[0]
            age = row_data[1]
            gender = row_data[2]
            print(name + " is " + age + " years old and " + gender)

