import json
import matplotlib.pyplot as plt

file = "loc_results.txt"
languages = {}

with open(file, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
            for lang, stats in data.items():
                if isinstance(stats, dict) and "code" in stats:
                    languages[lang] = languages.get(lang, 0) + stats["code"]
        except:
            pass

# Ordenar por LOC
languages = dict(sorted(languages.items(), key=lambda x: x[1], reverse=True))

# Crear gráfico
plt.figure(figsize=(12, 8))
plt.barh(list(languages.keys()), list(languages.values()))
plt.xlabel("Líneas de código (LOC)")
plt.title("Lenguajes reales usados por Jesús Frontelo")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("jesus_frontelo_languages.png")

print("Gráfico generado: jesus_frontelo_languages.png")
