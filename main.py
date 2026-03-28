from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

# Create an Owner
owner = Owner(name="Alex")

# Create two Pets
pet1 = Pet(name="Buddy", species="Dog", breed="Labrador", age=5)
pet2 = Pet(name="Mittens", species="Cat", breed="Siamese", age=3)

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create Tasks with different times
now = datetime.now()
task1 = Task(description="Morning walk", time=now.replace(hour=7, minute=0), frequency="daily")
task2 = Task(description="Feed breakfast", time=now.replace(hour=8, minute=0), frequency="daily")
task3 = Task(description="Playtime", time=now.replace(hour=17, minute=0), frequency="daily")

task4 = Task(description="Litter box cleaning", time=now.replace(hour=9, minute=0), frequency="daily")
task5 = Task(description="Feed dinner", time=now.replace(hour=18, minute=0), frequency="daily")
task6 = Task(description="Evening cuddle", time=now.replace(hour=20, minute=0), frequency="daily")

# Assign tasks to pets
pet1.add_task(task1)
pet1.add_task(task2)
pet1.add_task(task3)

pet2.add_task(task4)
pet2.add_task(task5)
pet2.add_task(task6)

# Create Scheduler
scheduler = Scheduler(owner)

# Print Today's Schedule
print("Today's Schedule:")
all_tasks = scheduler.get_all_tasks()
# Sort tasks by time
all_tasks_sorted = sorted(all_tasks, key=lambda t: t.time or datetime.max)
for task in all_tasks_sorted:
	pet_name = None
	for pet in owner.pets:
		if task in pet.tasks:
			pet_name = pet.name
			break
	time_str = task.time.strftime('%H:%M') if task.time else 'No time'
	print(f"{time_str} - {task.description} (Pet: {pet_name})")

