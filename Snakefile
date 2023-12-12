rule prepare:
    output:
        "data/car.csv"
    shell:
        "python3 /Users/victordashuaibi/Desktop/is477-fall2023-final-project/scripts/prepare_data.py"

rule profile:
    input:
        infile="data/car.csv"
    output:
        "profiling/report.html"
    shell:
        "python3 /Users/victordashuaibi/Desktop/is477-fall2023-final-project/scripts/profile_fixed_error.py"

rule analyze:
    input:
        infile="data/car.data"
    output: 
        summary="results/summary_statistics.csv",
        vis="results/simple_vis.png",
        report="results/classification_report.txt"
    shell:
        "python3 /Users/victordashuaibi/Desktop/is477-fall2023-final-project/scripts/analysis.py"
