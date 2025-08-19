import re
import matplotlib.pyplot as plt

def analyze_data():
    """
    Analyzes the inventory turnover ratio data from data.txt,
    generates a visualization, and saves it.
    """
    # Read data from data.txt
    with open('data.txt', 'r') as f:
        content = f.read()

    # Extract quarterly data using regex
    quarterly_data_matches = re.findall(r"Q(\d): ([\d.]+)", content)
    if not quarterly_data_matches:
        print("Could not find quarterly data in data.txt")
        return

    quarters = [f"Q{match[0]}" for match in quarterly_data_matches]
    ratios = [float(match[1]) for match in quarterly_data_matches]

    # Extract target
    target_match = re.search(r"Industry Target: ([\d.]+)", content)
    target = float(target_match.group(1)) if target_match else None

    # Calculate average
    average_ratio = sum(ratios) / len(ratios)

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(quarters, ratios, marker='o', linestyle='-', label='2024 Quarterly Ratio')
    if target:
        plt.axhline(y=target, color='r', linestyle='--', label=f'Industry Target ({target})')
    plt.title('Inventory Turnover Ratio - 2024 Quarterly Data')
    plt.xlabel('Quarter')
    plt.ylabel('Turnover Ratio')
    plt.grid(True)
    plt.legend()
    plt.ylim(0, max(max(ratios), target if target else 0) + 1)


    # Save the plot
    plt.savefig('inventory_turnover_ratio.png')
    print(f"Average Ratio calculated: {average_ratio:.2f}")
    print("Plot saved as inventory_turnover_ratio.png")

if __name__ == "__main__":
    analyze_data()
