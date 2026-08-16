from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.hashers import make_password

from accounts.models import User
from employees.models import Employee


class Command(BaseCommand):

    help = "Create realistic test employee users and employee records"

    # =========================================================
    # Department -> Designation -> Salary
    # =========================================================

    DEPARTMENT_DATA = {
        "Development": {
            "Software Developer": 50000,
            "Senior Software Developer": 75000,
            "Tech Lead": 100000,
            "Backend Developer": 60000,
            "Frontend Developer": 60000,
            "Full Stack Developer": 70000,
        },

        "Testing": {
            "QA Engineer": 45000,
            "Senior QA Engineer": 70000,
            "Test Lead": 95000,
            "Automation Tester": 60000,
            "Performance Tester": 65000,
        },

        "HR": {
            "HR Executive": 40000,
            "HR Manager": 70000,
            "HR Lead": 90000,
            "Recruiter": 45000,
            "Senior Recruiter": 65000,
        },

        "Finance": {
            "Accountant": 45000,
            "Senior Accountant": 70000,
            "Finance Manager": 95000,
            "Financial Analyst": 60000,
            "Senior Financial Analyst": 80000,
        },

        "Marketing": {
            "Marketing Executive": 40000,
            "Senior Marketing Executive": 65000,
            "Marketing Manager": 90000,
            "Digital Marketing Executive": 50000,
            "SEO Specialist": 55000,
        },

        "Sales": {
            "Sales Executive": 40000,
            "Senior Sales Executive": 60000,
            "Sales Manager": 85000,
            "Business Development Executive": 50000,
            "Business Development Manager": 75000,
        },

        "IT Support": {
            "Support Engineer": 40000,
            "Senior Support Engineer": 65000,
            "System Administrator": 80000,
            "Network Administrator": 70000,
            "IT Support Specialist": 50000,
        },

        "Administration": {
            "Admin Executive": 35000,
            "Office Manager": 60000,
            "Administration Manager": 80000,
            "Administrative Assistant": 40000,
            "Facility Manager": 65000,
        },
    }

    # =========================================================
    # First Names
    # =========================================================

    FIRST_NAMES = [
        "Aarav",
        "Aadhya",
        "Aditya",
        "Akash",
        "Akhil",
        "Amit",
        "Amrutha",
        "Ananya",
        "Anil",
        "Anjali",
        "Anusha",
        "Arjun",
        "Arun",
        "Ashok",
        "Bhargav",
        "Bhavya",
        "Chaitanya",
        "Charan",
        "Deepak",
        "Deepika",
        "Divya",
        "Dinesh",
        "Harini",
        "Harish",
        "Hemanth",
        "Isha",
        "Jahnavi",
        "Karthik",
        "Kavya",
        "Keerthi",
        "Kiran",
        "Krishna",
        "Lakshmi",
        "Madhav",
        "Mahesh",
        "Manoj",
        "Meghana",
        "Monika",
        "Nandini",
        "Naveen",
        "Neha",
        "Nikhil",
        "Pooja",
        "Pradeep",
        "Pranav",
        "Praveen",
        "Priya",
        "Rahul",
        "Rajesh",
        "Rakesh",
        "Ravi",
        "Riya",
        "Rohan",
        "Sahithi",
        "Sai",
        "Sanjay",
        "Sanjana",
        "Sarath",
        "Shiva",
        "Shreya",
        "Sneha",
        "Sowmya",
        "Srinivas",
        "Suresh",
        "Swathi",
        "Tarun",
        "Teja",
        "Uday",
        "Varun",
        "Venkatesh",
        "Vijay",
        "Vikram",
        "Vinay",
        "Vishal",
        "Yash",
    ]

    # =========================================================
    # Last Names
    # =========================================================

    LAST_NAMES = [
        "Reddy",
        "Rao",
        "Kumar",
        "Sharma",
        "Verma",
        "Patel",
        "Singh",
        "Gupta",
        "Naidu",
        "Prasad",
        "Varma",
        "Chowdary",
        "Krishna",
        "Yadav",
        "Mishra",
        "Joshi",
        "Mehta",
        "Iyer",
        "Nair",
        "Pillai",
        "Das",
        "Goud",
        "Raju",
        "Shetty",
        "Babu",
        "Murthy",
        "Rajan",
        "Menon",
        "Kapoor",
        "Malhotra",
        "Agarwal",
        "Bansal",
        "Chandra",
        "Desai",
        "Kulkarni",
        "Patil",
        "Jain",
        "Saxena",
        "Tiwari",
        "Pandey",
    ]

    # =========================================================
    # Command Arguments
    # =========================================================

    def add_arguments(self, parser):

        parser.add_argument(
            "--count",
            type=int,
            default=500,
            help="Number of employees to create",
        )

        parser.add_argument(
            "--password",
            type=str,
            default="Employee@123",
            help="Password for all test employees",
        )

    # =========================================================
    # Main Command
    # =========================================================

    @transaction.atomic
    def handle(self, *args, **options):

        count = options["count"]
        password = options["password"]

        # -----------------------------------------------------
        # Validate count
        # -----------------------------------------------------

        if count <= 0:
            self.stdout.write(
                self.style.ERROR("Count must be greater than 0.")
            )
            return

        # -----------------------------------------------------
        # Generate password hash ONCE
        # -----------------------------------------------------

        password_hash = make_password(password)

        departments = list(self.DEPARTMENT_DATA.keys())

        created_users = 0
        created_employees = 0

        # -----------------------------------------------------
        # Mobile number range
        # -----------------------------------------------------

        MOBILE_START = 6666666666

        MOBILE_END = 9999999999

        available_mobile_numbers = MOBILE_END - MOBILE_START + 1

        if count > available_mobile_numbers:

            self.stdout.write(
                self.style.ERROR(
                    f"Cannot create {count} employees. "
                    f"Only {available_mobile_numbers} mobile numbers "
                    f"are available in the requested range."
                )
            )

            return

        # =====================================================
        # Create Employees
        # =====================================================

        for i in range(1, count + 1):

            # -------------------------------------------------
            # Different First Name
            # -------------------------------------------------

            first_name = self.FIRST_NAMES[
                (i - 1) % len(self.FIRST_NAMES)
            ]

            # -------------------------------------------------
            # Different Last Name
            # -------------------------------------------------

            last_name = self.LAST_NAMES[
                ((i - 1) // len(self.FIRST_NAMES))
                % len(self.LAST_NAMES)
            ]

            # -------------------------------------------------
            # Username
            #
            # Example:
            #
            # rahul.reddy001
            # rahul.rao002
            # priyasharma003
            #
            # -------------------------------------------------

            username = (
                f"{first_name.lower()}."
                f"{last_name.lower()}"
                f"{i:03d}"
            )

            # -------------------------------------------------
            # Email
            # -------------------------------------------------

            email = (
                f"{first_name.lower()}."
                f"{last_name.lower()}"
                f"{i:03d}"
                "@example.com"
            )

            # -------------------------------------------------
            # Employee Code
            # -------------------------------------------------

            employee_code = f"EMP{i:03d}"

            # -------------------------------------------------
            # Unique Mobile Number
            #
            # 6666666666
            # 6666666667
            # 6666666668
            # ...
            #
            # -------------------------------------------------

            mobile = str(MOBILE_START + (i - 1))

            # -------------------------------------------------
            # Department
            # -------------------------------------------------

            department = departments[
                (i - 1) % len(departments)
            ]

            # -------------------------------------------------
            # Department-specific designations
            # -------------------------------------------------

            designation_salary_map = self.DEPARTMENT_DATA[
                department
            ]

            designations = list(
                designation_salary_map.keys()
            )

            # -------------------------------------------------
            # Select designation
            #
            # Important:
            #
            # We select ONLY from the current department.
            #
            # -------------------------------------------------

            designation = designations[
                ((i - 1) // len(departments))
                % len(designations)
            ]

            salary = designation_salary_map[
                designation
            ]

            # =================================================
            # Create / Update User
            # =================================================

            user, user_created = User.objects.get_or_create(

                username=username,

                defaults={
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "role": User.Role.EMPLOYEE,
                    "is_active": True,
                    "password": password_hash,
                },
            )

            # -------------------------------------------------
            # Update existing user
            # -------------------------------------------------

            user.password = password_hash
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.role = User.Role.EMPLOYEE
            user.is_active = True

            user.save(
                update_fields=[
                    "password",
                    "first_name",
                    "last_name",
                    "email",
                    "role",
                    "is_active",
                ]
            )

            if user_created:
                created_users += 1

            # =================================================
            # Create / Update Employee
            # =================================================

            employee, employee_created = (
                Employee.objects.get_or_create(

                    user=user,

                    defaults={
                        "employee_code": employee_code,
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "mobile": mobile,
                        "department": department,
                        "designation": designation,
                        "salary": salary,
                    },
                )
            )

            # -------------------------------------------------
            # Update existing employee
            # -------------------------------------------------

            employee.employee_code = employee_code
            employee.first_name = first_name
            employee.last_name = last_name
            employee.email = email
            employee.mobile = mobile
            employee.department = department
            employee.designation = designation
            employee.salary = salary

            employee.save(
                update_fields=[
                    "employee_code",
                    "first_name",
                    "last_name",
                    "email",
                    "mobile",
                    "department",
                    "designation",
                    "salary",
                ]
            )

            if employee_created:
                created_employees += 1

            # -------------------------------------------------
            # Progress
            # -------------------------------------------------

            if i % 50 == 0:

                self.stdout.write(
                    f"Processed {i}/{count} employees..."
                )

        # =====================================================
        # Final Result
        # =====================================================

        self.stdout.write("")

        self.stdout.write(
            self.style.SUCCESS(
                f"Users created: {created_users}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Employees created: {created_employees}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Total requested: {count}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Test password: {password}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Employee seed completed successfully!"
            )
        )