#!/bin/bash

USER="JesusFrontelo"
TMP_DIR="repo_tmp"
RESULT="loc_results.txt"

rm -rf $TMP_DIR
mkdir $TMP_DIR
echo "" > $RESULT

# Obtener lista de repos
gh repo list $USER --limit 200 --json name,url | jq -r '.[] | .name' | while read repo; do
    echo "Analizando $repo..."
    git clone --depth 1 https://github.com/$USER/$repo.git $TMP_DIR/$repo >/dev/null 2>&1

    cloc $TMP_DIR/$repo --json --quiet >> $RESULT
done

echo "Análisis completado. Resultados en $RESULT"
