# Intelligence Artificielle

- [TD1 - BFS & DFS](TD1/README.md)
- [TD2 - Dijkstra & A*](TD2/README.md)
- [TD3 - Minimax, Alpha-Beta & MCTS (Puissance 4)](TD3/README.md)

Fix erreur images SVG sur windows (TD1 et TD2 uniquement) : ``winget install tschoonj.GTKForWindows``

Lancer le TD X (venv à la racine du dépôt `IntelligenceArtificiel`) :
```
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r TDX\requirements.txt

python.exe -m pip install --upgrade pip

cd TDX

python main.py   (TD1, TD2)
ou
python app.py    (TD3, puis ouvrir http://127.0.0.1:5000)
```
