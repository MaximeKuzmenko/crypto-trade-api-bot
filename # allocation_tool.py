# allocation_tool.py
import matplotlib.pyplot as plt

def calculate_allocations(total_tokens, percentages):
    return {category: total_tokens * percent / 100 for category, percent in percentages.items()}

def plot_allocations(allocations):
    labels = allocations.keys()
    sizes = allocations.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Token Allocations')
    plt.show()

if __name__ == "__main__":
    total_tokens = 1000000
    percentages = {
        "Team": 20,
        "Investors": 30,
        "Community": 25,
        "Marketing": 15,
        "Reserve": 10
    }
    allocations = calculate_allocations(total_tokens, percentages)
    print("Allocations:", allocations)
    plot_allocations(allocations)
