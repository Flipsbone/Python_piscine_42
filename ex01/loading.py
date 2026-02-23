try:
    import sys
    import pandas as pd
    import matplotlib.pyplot as plt
    import requests
    import numpy as np
    DEPENDENCIES_INSTALLED = True
except ImportError as e:
    DEPENDENCIES_INSTALLED = False
    missing_module = str(e).split("'")[1] if "'" in str(e) else "required libraries"

def run_analysis() -> None:
    url = "https://data.ademe.fr/data-fair/api/v1/datasets/liste-des-entreprises-rge-2/lines"

    params = {
        "q": '"Pompe à chaleur"',
        "size": 10000,
        "select": "code_postal"
    }

    try:
        print("Analyzing Matrix data...")
        print("Processing 10000 data points...")

        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json().get('results', [])

        if not data:
            print("No data found in the Matrix.")
            return

        df = pd.DataFrame(data)

        df['dept'] = df['code_postal'].astype(str).str.zfill(5).str[:2]

        df_stats = df['dept'].value_counts().reset_index()
        df_stats.columns = ['Departement', 'Nombre']

        counts = df_stats['Nombre'].values
        indices_tries = np.argsort(counts)[::-1]
        df_final = df_stats.iloc[indices_tries]

        print("Generating visualization...")

        plt.figure(figsize=(12, 8))
        df_plot = df_final.head(20)
        
        colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(df_plot)))
        
        bars = plt.barh(df_plot['Departement'], df_plot['Nombre'], color=colors, edgecolor='white')
        plt.gca().invert_yaxis()
        
        plt.title('Distribution of RGE-Certified Heat Pump Installers by Department (10k Sample)', fontsize=14)
        plt.xlabel('Number of Companies')
        plt.ylabel('Department (Code)')

        for bar in bars:
            plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                     int(bar.get_width()), va='center', fontweight='bold')

        plt.grid(axis='x', linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.savefig("matrix_analysis.png")
        
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"Error during execution: {e}")
        
def check_dependencies()-> None:
    if not DEPENDENCIES_INSTALLED:
        print(f"\n[ERROR] Missing dependency: {missing_module}")
        print("Please install requirements: pip install -r requierement")
        sys.exit(1)

        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
        print(f"[OK] matplotlib ({plt.matplotlib.__version__}) - Visualization ready")
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")

def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    check_dependencies()
    run_analysis()

if __name__ == "__main__":
    main()