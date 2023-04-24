import requests
import sys

if len(sys.argv) < 2:
    print("Please provide an employee ID")
    sys.exit(1)

employee_id = int(sys.argv[1])

response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code != 200:
    print("Error: Unable to retrieve TODO list")
    sys.exit(1)

todos = response.json()

completed_tasks = [todo for todo in todos if todo["completed"]]
total_tasks = len(todos)

employee_name = todos[0]["name"].split()[0]

print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

for todo in completed_tasks:
    print(f"\t {todo['title']}")


