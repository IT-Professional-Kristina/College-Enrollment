input_name = input("What is your name? ")

def greet(input_name):
    print(f"Welcome to Standford University, {input_name}!")

greet(input_name)

degree_list_selection = ["Associates", "Bachelors", "Masters", "Ph.D"]
print(degree_list_selection)

pick = input("What Degree are you pursuing? ")
print(pick)

def greet_2(input_name):
    print(f"Thank You, {input_name}!")

greet_2(input_name)


associates_message = """Here is a list of Associates Degrees we offer: Associates of Arts, Associates of Accounting, Associates of Criminal Justice"""

bachelors_message = """Here is a list of Bachelor of Science Degrees we offer: Bachelors of Science in Nursing, Bachelors of Science in Information Technology,
 Bachelors of Science in Physhology, Bachelors of Science in Computer Science, Bachelors of Science in Mechanical Engineering"""

masters_message = """Here is a list of Master Degrees we offer: Masters in Information Technology, Masters in Computer Science, Masters in Business Administration """

phd_message = """Here is a list of PH.D Degrees we offer: Ph.D in Psychology, Ph.D in Business Adminstration, Ph.D Database Adminstration"""

if pick == "Associates":
    print(associates_message)
elif pick == "Bachelors":
     print(bachelors_message)
elif pick == "Masters":
     print(masters_message)
elif pick == "Ph.D":
     print(phd_message)
else:
    print("Invalid choice. Please enter a vailid degree option")


def greet_3(input_name):
    print(f"Hello, {input_name} are you ready to enroll in the {pick} program? ")

greet_3(input_name)

response_message = input("Yes or No ").lower()

if response_message =="yes":
    print("We will proceed with the following overview statements for the Degree Program.")

    acceptance_message = """Acceptance Confirmation: Once a student receives an acceptance letter, they are typically required to confirm their intention to enroll in the chosen degree program.
    This is often done by submitting a confirmation form and, in some cases, paying a tuition deposit. """
    print(acceptance_message)

    orientation_message = """Orientation Session: Many universitites organize orientation sessions for incoming studenets.
    These sessions provide essential information about the campus, academic policies, support services, 
    and extracurricular activities. They may also include tours of campus facilities."""
    print(orientation_message)

    course_registration = """Course Registration: After conforming enrollment, students are usually guided through the course registration process. 
    THis involves selecting courses for the upcoming semester based on the program
    requirements and any specific electives or concentrations."""
    print(course_registration)
else:
    print("Let us know when are ready to enroll")

