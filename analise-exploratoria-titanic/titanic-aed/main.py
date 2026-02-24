
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "titanic.csv"
OUT_DIR = BASE_DIR / "outputs"

PLOT_SEXO = OUT_DIR / "sobrevivencia_por_sexo.png"
PLOT_CLASSE = OUT_DIR / "sobrevivencia_por_classe.png"
PLOT_COMBINADO = OUT_DIR / "sobrevivencia_por_sexo_e_classe.png"
ARQUIVO_INSIGHTS = OUT_DIR / "insights.txt"


def banner(titulo):
    print("\n" + "=" * 80)
    print(titulo)
    print("=" * 80)


def carregar_dados():
    return pd.read_csv(DATA_PATH)


def preparar_dados(df):
    df = df.drop_duplicates()

    if "Embarked" in df.columns:
        df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    if "Fare" in df.columns:
        df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    if "Cabin" in df.columns:
        df["PossuiCabine"] = df["Cabin"].notna().astype(int)

    return df


def analisar(df):
    banner("ANÁLISE PRINCIPAL")

    resultados = {}

    taxa_sexo = df.groupby("Sex")["Survived"].mean()
    taxa_classe = df.groupby("Pclass")["Survived"].mean()
    taxa_combinada = df.groupby(["Sex", "Pclass"])["Survived"].mean()

    print("\nTaxa de sobrevivência por sexo:")
    print((taxa_sexo * 100).round(2).astype(str) + "%")

    print("\nTaxa de sobrevivência por classe:")
    print((taxa_classe * 100).round(2).astype(str) + "%")

    print("\nTaxa de sobrevivência por sexo e classe:")
    print((taxa_combinada * 100).round(2).astype(str) + "%")

    resultados["sexo"] = taxa_sexo
    resultados["classe"] = taxa_classe
    resultados["combinado"] = taxa_combinada

    return resultados


def grafico_barra(dados, eixo_x, eixo_y, titulo, caminho):
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    ax = sns.barplot(data=dados, x=eixo_x, y=eixo_y)
    ax.set_ylim(0, 100)
    ax.set_title(titulo)
    ax.set_ylabel("Sobrevivência (%)")

    for p in ax.patches:
        altura = p.get_height()
        ax.annotate(f"{altura:.1f}%",
                    (p.get_x() + p.get_width() / 2., altura),
                    ha="center", va="bottom",
                    xytext=(0, 3),
                    textcoords="offset points")

    plt.tight_layout()
    plt.savefig(caminho, dpi=200)
    plt.close()


def gerar_visualizacoes(df):
    banner("GERANDO VISUALIZAÇÕES")

    OUT_DIR.mkdir(exist_ok=True)

    df_sexo = df.groupby("Sex")["Survived"].mean().reset_index()
    df_sexo["TaxaSobrevivencia"] = df_sexo["Survived"] * 100
    grafico_barra(df_sexo, "Sex", "TaxaSobrevivencia", "Sobrevivência por Sexo", PLOT_SEXO)

    df_classe = df.groupby("Pclass")["Survived"].mean().reset_index()
    df_classe["TaxaSobrevivencia"] = df_classe["Survived"] * 100
    grafico_barra(df_classe, "Pclass", "TaxaSobrevivencia", "Sobrevivência por Classe", PLOT_CLASSE)

    df_comb = df.groupby(["Sex", "Pclass"])["Survived"].mean().reset_index()
    df_comb["TaxaSobrevivencia"] = df_comb["Survived"] * 100

    plt.figure(figsize=(8, 5))
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(data=df_comb, x="Pclass", y="TaxaSobrevivencia", hue="Sex")
    ax.set_ylim(0, 100)
    ax.set_title("Sobrevivência por Sexo e Classe")
    ax.set_ylabel("Sobrevivência (%)")

    plt.tight_layout()
    plt.savefig(PLOT_COMBINADO, dpi=200)
    plt.close()


def resumo_estatistico(resultados):
    banner("RESUMO ESTATÍSTICO")

    diferenca_sexo = (resultados["sexo"].max() - resultados["sexo"].min()) * 100
    diferenca_classe = (resultados["classe"].max() - resultados["classe"].min()) * 100

    texto = []
    texto.append("INSIGHTS PRINCIPAIS\n")
    texto.append(f"Diferença percentual entre sexos: {diferenca_sexo:.2f}%")
    texto.append(f"Diferença percentual entre classes: {diferenca_classe:.2f}%")
    texto.append("\nConclusão: sexo e classe demonstram impacto significativo na sobrevivência.")

    with open(ARQUIVO_INSIGHTS, "w", encoding="utf-8") as f:
        f.write("\n".join(texto))

    print("\n".join(texto))


def main():
    banner("TITANIC — ANÁLISE EXPLORATÓRIA COMPLETA (PT-BR)")

    df = carregar_dados()
    df = preparar_dados(df)
    resultados = analisar(df)
    gerar_visualizacoes(df)
    resumo_estatistico(resultados)

    banner("PROJETO FINALIZADO COM SUCESSO")


if __name__ == "__main__":
    main()
