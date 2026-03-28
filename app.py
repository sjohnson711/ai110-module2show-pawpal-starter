import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner & Pet Setup")
owner_name = st.text_input("Owner name", value="Jordan")

# Initialize session state for Owner and pets if they don't already exist
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name)

col1, col2 = st.columns(2)
with col1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col2:
    species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    new_pet = Pet(name=pet_name, species=species)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {pet_name} the {species} to {st.session_state.owner.name}'s profile!")

if st.session_state.owner.pets:
    st.write("**Pets:**", ", ".join(p.name for p in st.session_state.owner.pets))
else:
    st.info("No pets added yet. Add one above.")

st.divider()
st.markdown("### Tasks")
st.caption("Select a pet and add tasks to their schedule.")

if st.session_state.owner.pets:
    pet_names = [p.name for p in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Assign task to pet", pet_names)
    selected_pet = next(p for p in st.session_state.owner.pets if p.name == selected_pet_name)

    col1, col2 = st.columns(2)
    with col1:
        task_description = st.text_input("Task description", value="Morning walk")
    with col2:
        task_frequency = st.selectbox("Frequency", ["daily", "weekly", "monthly", "once"])

    if st.button("Add Task"):
        new_task = Task(description=task_description, frequency=task_frequency)
        selected_pet.add_task(new_task)
        st.success(f"Added '{task_description}' to {selected_pet.name}'s tasks!")

    for pet in st.session_state.owner.pets:
        tasks = pet.get_tasks()
        if tasks:
            st.write(f"**{pet.name}'s tasks:**")
            st.table([{"Description": t.description, "Frequency": t.frequency, "Completed": t.completed} for t in tasks])
else:
    st.info("Add a pet first to start adding tasks.")

st.divider()

st.subheader("Build Schedule")
st.caption("Retrieve and display all tasks across all pets using the Scheduler.")

if st.button("Generate Schedule"):
    scheduler = Scheduler(st.session_state.owner)
    all_tasks = scheduler.get_all_tasks()
    if all_tasks:
        st.success("Today's Schedule:")
        rows = []
        for task in all_tasks:
            pet_name_for_task = next(
                (p.name for p in st.session_state.owner.pets if task in p.tasks), "Unknown"
            )
            rows.append({
                "Pet": pet_name_for_task,
                "Task": task.description,
                "Frequency": task.frequency,
                "Completed": task.completed,
            })
        st.table(rows)
    else:
        st.warning("No tasks found. Add pets and tasks first.")
