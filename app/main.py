import os
import subprocess

def run_notebook(notebook_path):
    print(f"Executando {notebook_path}...")
    result = subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path], 
                            capture_output=True, 
                            text=True)
    if result.returncode == 0:
        print(f"Sucesso: {notebook_path}")
    else:
        print(f"Erro ao executar {notebook_path}")

if __name__ == "__main__":
    notebooks = [
        "churn-model-regressionLogistic.ipynb",
        "churn-model-randomForest.ipynb",
        "churn-model-xgboost.ipynb"
    ]
    
    for nb in notebooks:
        run_notebook(nb)
    
    print("Processo completo! O MLflow deve estar com os resultados.")