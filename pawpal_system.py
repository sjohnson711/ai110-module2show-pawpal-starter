# pawpal_system.py
"""
Logic layer for PawPal+ app: defines core data model and scheduling classes.
"""
from datetime import datetime, date
from typing import List, Optional, Dict, TYPE_CHECKING

if TYPE_CHECKING:
	from typing import Any

# Task class
class Task:
    """Represents a single activity for a pet."""
    _id_counter = 1
    def __init__(self, description: str, time: Optional[datetime] = None, frequency: str = '', completed: bool = False):
        self.task_id = Task._id_counter
        Task._id_counter += 1
        self.description = description
        self.time = time
        self.frequency = frequency
        self.completed = completed

    def mark_complete(self):
        """Mark this task as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark this task as incomplete."""
        self.completed = False


# Pet class
class Pet:
    """Stores pet details and a list of tasks."""
    _id_counter = 1
    def __init__(self, name: str, species: str, breed: str = '', age: int = 0):
        self.pet_id = Pet._id_counter
        Pet._id_counter += 1
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


# Owner class
class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks for all pets owned by this owner."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks


# Scheduler class
class Scheduler:
    """The 'Brain' that retrieves, organizes, and manages tasks across pets."""
    def __init__(self, owner: Owner):
        """Initialize the Scheduler with an Owner."""
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from all pets."""
        return self.owner.get_all_tasks()

    def get_tasks_by_pet(self, pet: Pet) -> List[Task]:
        """Retrieve all tasks for a specific pet."""
        return pet.get_tasks()

    def get_tasks_by_status(self, completed: bool) -> List[Task]:
        """Retrieve tasks filtered by completion status."""
        return [task for task in self.get_all_tasks() if task.completed == completed]

    def get_tasks_by_frequency(self, frequency: str) -> List[Task]:
        """Retrieve tasks filtered by frequency."""
        return [task for task in self.get_all_tasks() if task.frequency == frequency]
