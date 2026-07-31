
import csv, random
from datetime import datetime
from datetime import date, timedelta

first_names=["Rahul","Kiran","Anitha","Suresh","Priya","Vikram","Ramesh","Lakshmi","Akhil","Divya","Arjun","Sneha","Harish","Keerthi","Ajay","Naveen","Sai","Bhavani","Madhu","Pavan","Ravi","Deepika","Ganesh","Meena","Varun"]
last_names=["Sharma","Kumar","Reddy","Patel","Rao","Naidu","Singh","Gupta","Verma","Das"]
departments=["Python","Java","Testing","HR","Accounts","DevOps","Data Science","React","NodeJS","AI","Marketing","Support","Sales","Security","Cloud","Finance","Networking","UI UX","Business","Operations","Admin","QA","Mobile","ERP","CRM","Design"]
designations=["Intern","Junior Developer","Software Engineer","Senior Software Engineer","Team Lead","Manager","HR Executive","Accountant","Tester","DevOps Engineer","Data Analyst","Project Manager","Business Analyst","Cloud Engineer","Technical Lead"]
roles=["Admin","Manager","Team Lead","Employee","Intern"]
cities=["Hyderabad","Vijayawada","Visakhapatnam","Bengaluru","Chennai","Mumbai","Delhi","Pune","Kolkata","Jaipur","Lucknow","Nagpur","Warangal","Mysuru","Coimbatore","Guntur","Tirupati","Kochi","Bhopal","Indore"]
states=["Andhra Pradesh","Telangana","Karnataka","Tamil Nadu","Maharashtra","Delhi","Rajasthan","Uttar Pradesh","West Bengal","Kerala","Madhya Pradesh"]
genders=["Male","Female"]
statuses=["Active","Inactive","Resigned"]
today=date.today()

fields=["employee_code","first_name","last_name","email","mobile","age","gender","department","designation","role","city","state","country","salary","bonus","experience","status","is_active","is_verified","joining_date","last_login","profile_completed","rating","created_at", "updated_at"]
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("employees.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(fields)
    for i in range(1,501):
        first=random.choice(first_names)
        last=random.choice(last_names)
        join=today-timedelta(days=random.randint(30,3000))
        login=join+timedelta(days=random.randint(0,max((today-join).days,1)))
        w.writerow([
            f"EMP{i:04}",
            first,
            last,
            f"employee{i}@gmail.com",
            "9"+str(random.randint(100000000,999999999)),
            random.randint(20,60),
            random.choice(genders),
            random.choice(departments),
            random.choice(designations),
            random.choice(roles),
            random.choice(cities),
            random.choice(states),
            "India",
            random.randint(15000,250000),
            random.randint(1000,50000),
            random.randint(0,25),
            random.choice(statuses),
            random.choice([0,1]),
            random.choice([0,1]),
            join.isoformat(),
            login.isoformat()+" 10:00:00",
            random.choice([0,1]),
            round(random.uniform(1.0,5.0),1),
            now, now
        ])
print("Generated employees.csv")
with open("employee_data_generator.py","w",encoding="utf-8") as g:
    pass
