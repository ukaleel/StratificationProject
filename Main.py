# Usman Kaleel
# This code is meant to simulate how differing initial resources for people
# can lead to future widened gaps in resources and opportunities


import random
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources
        self.knowledge = 0
        self.career_opportunities = 0

    def add_resources(self, amount):
        self.resources += amount

    #Simulate life developments with compounding effects
    def develop(self, growth_rate):

        self.resources *= (1 + growth_rate)
        self.knowledge += self.resources * random.uniform(0.1, 0.3)
        self.career_opportunities += (self.knowledge * 0.3)
        random_event_chance = random.uniform(0, 1)

        #random event chance
        if random_event_chance < 0.1:
            random_effect = random.uniform(-10, 10)
            self.resources = max(0, self.resources + random_effect)

    def display_status(self, year):
        print(f"Year {year}: {self.name}: Resources = {self.resources:.1f}, "
              f"Knowledge = {self.knowledge:.1f},"
              f"Career Opportunities = {self.career_opportunities:.1f}")




def plot_progress_during_simulation(students, years, equity_flag=False, growth_rate=0.1):
    metrics = ['resources', 'knowledge', 'career_opportunities']
    data = {}


    for student in students:
        student_data = {}
        for metric in metrics:
            student_data[metric] = []
        data[student.name] = student_data
    target_resources = 50

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axes = axs.flatten()

    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        total_resources = sum(student.resources for student in students)
        num_students = len(students)

        for student in students:
            # Apply equity adjustments if flag is true
            if equity_flag:
                average_resources = total_resources / num_students
                redistribution = average_resources - student.resources
                student.add_resources(redistribution)
            else:
                student.add_resources(10)

            student.develop(growth_rate=growth_rate)

            student.display_status(year)

            data[student.name]['resources'].append(student.resources)
            data[student.name]['knowledge'].append(student.knowledge)
            data[student.name]['career_opportunities'].append(student.career_opportunities)

        # Update the plot after each year
        for i, metric in enumerate(metrics):
            ax = axes[i]
            ax.clear()
            ax.set_title(f"{metric.capitalize()} Over Time")
            ax.set_xlabel("Year")
            ax.set_ylabel(metric.capitalize())

            for student in students:
                ax.plot(range(1, year + 1), data[student.name][metric], label=student.name)

            ax.legend()

    # Display the final graph
    plt.tight_layout()
    plt.show()


students = [
    Student("Arthur", 10),
    Student("Billy", 50),
    Student("Charlie", 100)
]

# Simulate with Equality
print("Simulation with Equality:")
plot_progress_during_simulation(students, years=10, equity_flag=False, growth_rate=0.1)


students = [
    Student("Arthur", 10),
    Student("Billy", 50),
    Student("Charlie", 100)
]

# Simulate with Equity
print("\nSimulation with Equity:")
plot_progress_during_simulation(students, years=10, equity_flag=True, growth_rate=0.1)
