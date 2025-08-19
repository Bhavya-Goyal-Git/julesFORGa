import matplotlib.pyplot as plt

def analyze_inventory_data():
    """
    Analyzes inventory turnover data from data.txt, generates a visualization,
    and saves it as a PNG file.
    """
    quarters = []
    ratios = []
    target = 0

    with open('data.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('Q'):
                parts = line.strip().split(': ')
                quarters.append(parts[0])
                ratios.append(float(parts[1]))
            elif line.startswith('Industry Target'):
                target = float(line.strip().split(': ')[1])

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(quarters, ratios, color='skyblue', label='Quarterly Ratio')
    plt.axhline(y=target, color='r', linestyle='--', label=f'Target: {target}')
    plt.xlabel('Quarter')
    plt.ylabel('Inventory Turnover Ratio')
    plt.title('Inventory Turnover Ratio - 2024 Quarterly Data')
    plt.legend()
    plt.grid(axis='y', linestyle='--')

    # Save the chart
    plt.savefig('inventory_turnover_chart.png')
    print("Chart saved as inventory_turnover_chart.png")

if __name__ == '__main__':
    analyze_inventory_data()
