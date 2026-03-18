import sys
import importlib


def check_dependencies() -> None:
    dependencies = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
        "numpy": "Numerical computation ready"
    }
    all_ok = True

    for name, description in dependencies.items():
        try:
            module = importlib.import_module(name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")
        except ImportError:
            print(f"[ERROR] Missing dependency: {name}")
            all_ok = False

    if not all_ok:
        print("\n[ERROR] Missing dependencies."
              "Please install requirements: pip install -r requirements.txt")
        sys.exit(1)


def run_analysis() -> None:
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import requests

    url = (
        "https://data.ademe.fr/data-fair/api/v1/"
        "datasets/liste-des-entreprises-rge-2/lines"
        )

    filter = {
        "query": '"Pompe à chaleur"',
        "size": 10000,
        "select": "code_postal"
    }

    try:
        print("Analyzing Matrix data...")
        print("Processing 10000 data points...")

        response = requests.get(url, params=filter, timeout=20)
        response.raise_for_status()
        data = response.json().get('results', [])

        if not data:
            print("No data found in the Matrix.")
            return

        df = pd.DataFrame(data)

        df['dept'] = df['code_postal'].astype(str).str.zfill(5).str[:2]
        df = df[df['dept'] != "0["]

        df_stats = df['dept'].value_counts().reset_index()
        df_stats.columns = ['Departement', 'Number']

        counts = df_stats['Number'].values
        indices_tries = np.argsort(counts)[::-1]
        df_final = df_stats.iloc[indices_tries]

        print("Generating visualization...")

        plt.figure(figsize=(12, 8))
        df_plot = df_final.head(20)

        colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(df_plot)))

        bars = plt.barh(df_plot['Departement'],
                        df_plot['Number'],
                        color=colors,
                        edgecolor='white')
        plt.gca().invert_yaxis()

        plt.title(
            'Distribution of RGE-Certified'
            'Heat Pump Installers by Department (10k Sample)', fontsize=14)
        plt.xlabel('Number of Companies')
        plt.ylabel('Department (Code)')

        for bar in bars:
            plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
                     int(bar.get_width()), va='center', fontweight='bold')

        plt.grid(axis='x', linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.savefig("matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"Error during execution: {e}")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    check_dependencies()
    print()
    run_analysis()


if __name__ == "__main__":
    main()
