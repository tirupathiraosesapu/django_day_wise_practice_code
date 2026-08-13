from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.hashers import make_password

from accounts.models import User
from employees.models import Employee


class Command(BaseCommand):

    help = "Create test employee users and employee records"

    # ---------------------------------------------------------
    # Department -> Designation -> Salary
    # ---------------------------------------------------------

    DEPARTMENT_DATA = {
        "Development": {
            "Software Developer": 50000,
            "Senior Software Developer": 75000,
            "Tech Lead": 100000,
        },
        "Testing": {
            "QA Engineer": 45000,
            "Senior QA Engineer": 70000,
            "Test Lead": 95000,
        },
        "HR": {
            "HR Executive": 40000,
            "HR Manager": 70000,
            "HR Lead": 90000,
        },
        "Finance": {
            "Accountant": 45000,
            "Senior Accountant": 70000,
            "Finance Manager": 95000,
        },
        "Marketing": {
            "Marketing Executive": 40000,
            "Senior Marketing Executive": 65000,
            "Marketing Manager": 90000,
        },
        "Sales": {
            "Sales Executive": 40000,
            "Senior Sales Executive": 60000,
            "Sales Manager": 85000,
        },
        "IT Support": {
            "Support Engineer": 40000,
            "Senior Support Engineer": 65000,
            "System Administrator": 80000,
        },
        "Administration": {
            "Admin Executive": 35000,
            "Office Manager": 60000,
            "Administration Manager": 80000,
        },
    }

    # ---------------------------------------------------------
    # Command Arguments
    # ---------------------------------------------------------

    def add_arguments(self, parser):

        parser.add_argument(
            "--count", type=int, default=500, help="Number of employees to create"
        )

        parser.add_argument(
            "--password",
            type=str,
            default="Employee@123",
            help="Password for all test employees",
        )

    # ---------------------------------------------------------
    # Main Command
    # ---------------------------------------------------------

    @transaction.atomic
    def handle(self, *args, **options):

        count = options["count"]
        password = options["password"]

        # -----------------------------------------------------
        # Validate count
        # -----------------------------------------------------

        if count <= 0:
            self.stdout.write(self.style.ERROR("Count must be greater than 0."))
            return

        # -----------------------------------------------------
        # Generate password hash only ONCE
        # -----------------------------------------------------

        password_hash = make_password(password)

        # -----------------------------------------------------
        # Prepare departments
        # -----------------------------------------------------

        departments = list(self.DEPARTMENT_DATA.keys())

        created_users = 0
        created_employees = 0

        # -----------------------------------------------------
        # Create employees
        # -----------------------------------------------------

        for i in range(1, count + 1):

            # -------------------------------------------------
            # Basic employee information
            # -------------------------------------------------

            username = f"employee{i:03d}"
            email = f"employee{i:03d}@example.com"

            first_name = f"Employee{i}"
            last_name = "Test"

            employee_code = f"EMP{i:03d}"

            # -------------------------------------------------
            # Unique mobile number
            # -------------------------------------------------

            mobile = f"90000{i:05d}"

            # Example:
            #
            # employee001 -> 9000000001
            # employee002 -> 9000000002
            # ...
            # employee500 -> 9000000500

            # -------------------------------------------------
            # Select department
            # -------------------------------------------------

            department = departments[(i - 1) % len(departments)]

            # -------------------------------------------------
            # Select designation
            # -------------------------------------------------

            designation_salary_map = self.DEPARTMENT_DATA[department]

            designations = list(designation_salary_map.keys())

            designation = designations[(i - 1) % len(designations)]

            salary = designation_salary_map[designation]

            # -------------------------------------------------
            # Create / Update User
            # -------------------------------------------------

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

            # -------------------------------------------------
            # Create / Update Employee
            # -------------------------------------------------

            employee, employee_created = Employee.objects.get_or_create(
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

                self.stdout.write(f"Processed {i}/{count} employees...")

        # -----------------------------------------------------
        # Final Result
        # -----------------------------------------------------

        self.stdout.write("")

        self.stdout.write(self.style.SUCCESS(f"Users created: {created_users}"))

        self.stdout.write(self.style.SUCCESS(f"Employees created: {created_employees}"))

        self.stdout.write(self.style.SUCCESS(f"Total requested: {count}"))

        self.stdout.write(self.style.SUCCESS(f"Test password: {password}"))

        self.stdout.write(self.style.SUCCESS("Employee seed completed successfully!"))
