
from pawpal_system import Task, Pet
# run python -m pytest
# Test that mark_complete() sets the task's completed status to True
def test_task_completion():
	task = Task(description="Test task")
	assert not task.completed
	task.mark_complete()
	assert task.completed

# Test that adding a task to a Pet increases the number of tasks for that pet
def test_task_addition_to_pet():
	pet = Pet(name="TestPet", species="Dog")
	initial_count = len(pet.tasks)
	task = Task(description="Walk")
	pet.add_task(task)
	assert len(pet.tasks) == initial_count + 1
