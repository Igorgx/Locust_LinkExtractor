import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# =========================
# CONFIG (opcional)
# =========================
OUTPUT_DIR = "graficos"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# =========================
# FUNÇÃO PARA EXTRAIR INFO DO NOME DO ARQUIVO
# =========================
def parse_filename(filename):
    name = os.path.basename(filename).replace(".csv", "")
    parts = name.split("_")
    
    lang = parts[0].capitalize()
    
    if "sem" in parts:
        cache = "Sem Cache"
    else:
        cache = "Com Cache"
    
    users = int(parts[-1])
    
    return lang, cache, users

# =========================
# LER TODOS OS CSVs
# =========================
data = []

files = glob.glob("*.csv")

if len(files) == 0:
    print("❌ Nenhum CSV encontrado na pasta!")
    exit()

for file in files:
    try:
        df = pd.read_csv(file)

        # tenta pegar linha aggregated de forma robusta
        if "Name" in df.columns:
            row = df[df["Name"] == "Aggregated"]
            if row.empty:
                row = df[df["Type"].isna()]
        else:
            row = df[df["Type"].isna()]

        row = row.iloc[0]

        lang, cache, users = parse_filename(file)

        data.append({
            "lang": lang,
            "cache": cache,
            "users": users,
            "avg": row["Average Response Time"],
            "median": row["Median Response Time"],
            "rps": row["Requests/s"],
            "fail": row["Failure Count"]
        })

        print(f"✔ Processado: {file}")

    except Exception as e:
        print(f"❌ Erro ao processar {file}: {e}")

df_all = pd.DataFrame(data)

# ordenar
df_all = df_all.sort_values(by=["lang", "cache", "users"])

print("\n📊 Dados consolidados:")
print(df_all)

# =========================
# FUNÇÃO DE PLOT
# =========================
def plot_metric(metric, title, ylabel, filename):
    plt.figure()

    for lang in df_all["lang"].unique():
        for cache in df_all["cache"].unique():
            subset = df_all[
                (df_all["lang"] == lang) &
                (df_all["cache"] == cache)
            ].sort_values("users")

            if len(subset) > 0:
                label = f"{lang} - {cache}"
                plt.plot(subset["users"], subset[metric], marker='o', label=label)

    plt.title(title)
    plt.xlabel("Número de Usuários")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()

    # salvar imagem
    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path)

    print(f"📁 Gráfico salvo em: {path}")

    plt.show()

# =========================
# GERAR GRÁFICOS
# =========================
plot_metric("avg", "Tempo Médio de Resposta", "ms", "tempo_medio.png")
plot_metric("median", "Mediana do Tempo de Resposta", "ms", "mediana.png")
plot_metric("rps", "Requisições por Segundo (RPS)", "req/s", "rps.png")
plot_metric("fail", "Número de Falhas", "falhas", "falhas.png")

# =========================
# GRÁFICOS EXTRAS (POR LINGUAGEM)
# =========================
def plot_lang(lang):
    df_lang = df_all[df_all["lang"] == lang]

    plt.figure()

    for cache in df_lang["cache"].unique():
        subset = df_lang[df_lang["cache"] == cache].sort_values("users")

        plt.plot(subset["users"], subset["avg"], marker='o', label=cache)

    plt.title(f"{lang}: Cache vs Sem Cache")
    plt.xlabel("Usuários")
    plt.ylabel("Tempo Médio (ms)")
    plt.legend()
    plt.grid()

    filename = f"{lang.lower()}_comparacao.png"
    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path)

    print(f"📁 Gráfico salvo em: {path}")

    plt.show()

# gerar gráficos por linguagem
for lang in df_all["lang"].unique():
    plot_lang(lang)