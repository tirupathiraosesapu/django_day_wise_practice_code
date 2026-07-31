import csv
import random
from datetime import datetime, timedelta


TOTAL_EMPLOYEES = 500


departments = [
    "Python Development",
    "MERN Development",
    "Java Development",
    "Data Analytics",
    "Data Science",
    "Testing",
    "Human Resources",
    "Finance",
    "Marketing",
    "Sales",
    "Operations",
    "Administration",
    "DevOps",
    "UI/UX Design",
]


designations = [
    "Software Engineer",
    "Senior Software Engineer",
    "Junior Software Engineer",
    "Team Lead",
    "Project Manager",
    "Data Analyst",
    "Data Scientist",
    "QA Engineer",
    "HR Executive",
    "Finance Executive",
    "Marketing Executive",
    "Business Analyst",
    "DevOps Engineer",
    "UI/UX Designer",
]


roles = [
    "Admin",
    "Manager",
    "Employee",
]


statuses = [
    "Active",
    "Inactive",
]


first_names = [
    "Aarav",
    "Vivaan",
    "Aditya",
    "Arjun",
    "Rohan",
    "Rahul",
    "Kiran",
    "Suresh",
    "Praveen",
    "Vijay",
    "Anil",
    "Rajesh",
    "Nikhil",
    "Sai",
    "Ravi",
    "Teja",
    "Pavan",
    "Manoj",
    "Sanjay",
    "Varun",
    "Priya",
    "Ananya",
    "Sneha",
    "Pooja",
    "Divya",
    "Kavya",
    "Keerthi",
    "Swathi",
    "Lakshmi",
    "Harika",
    "Sravani",
    "Deepika",
    "Bhavya",
    "Akhila",
    "Pallavi",
    "Sushmitha",
    "Mounika",
    "Sowmya",
    "Navya",
    "Anusha",
]


last_names = [
    "Kumar",
    "Reddy",
    "Rao",
    "Sharma",
    "Patel",
    "Singh",
    "Verma",
    "Gupta",
    "Naidu",
    "Varma",
    "Yadav",
    "Mishra",
    "Mehta",
    "Das",
    "Iyer",
    "Nair",
    "Pillai",
    "Joshi",
    "Agarwal",
    "Chowdary",
]


file_name = "employees.csv"


with open(
    file_name,
    mode="w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "employee_code",
        "first_name",
        "last_name",
        "email",
        "mobile",
        "department",
        "designation",
        "role",
        "salary",
        "status",
        "created_at",
        "updated_at",
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()


    for i in range(1, TOTAL_EMPLOYEES + 1):

        first_name = random.choice(first_names)

        last_name = random.choice(last_names)

        employee_code = f"EMP{i:04d}"

        email = (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{i}@company.com"
        )

        mobile = (
            f"9"
            f"{random.randint(100000000, 999999999)}"
        )

        department = random.choice(departments)

        designation = random.choice(designations)

        role = random.choice(roles)

        status = random.choice(statuses)

        salary = random.randint(
            25000,
            250000
        )


        # ----------------------------------
        # Generate Created Date
        # ----------------------------------

        created_at = datetime.now() - timedelta(
            days=random.randint(1, 1000)
        )


        # ----------------------------------
        # Generate Updated Date
        # ----------------------------------

        updated_at = created_at + timedelta(
            days=random.randint(0, 365)
        )


        # Ensure updated_at is not in future
        if updated_at > datetime.now():

            updated_at = datetime.now()


        writer.writerow({

            "employee_code": employee_code,

            "first_name": first_name,

            "last_name": last_name,

            "email": email,

            "mobile": mobile,

            "department": department,

            "designation": designation,

            "role": role,

            "salary": salary,

            "status": status,

            "created_at": created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "updated_at": updated_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        })


print(
    f"{TOTAL_EMPLOYEES} employee records generated successfully."
)

print(
    f"File created: {file_name}"
)