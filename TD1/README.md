# TD1 - BFS & DFS

Fix erreur images SVG sur windows : ``winget install tschoonj.GTKForWindows`` + changement de "SPRITE_DIRECTORY = Path("./pokemon-sprites")" en "SPRITE_DIRECTORY = Path(__file__).resolve().parent / "pokemon-sprites"" (ligne 53 de pokemon_game.py)

Lancer le TD1 (venv à la racine du dépôt `IntelligenceArtificiel`) :
```
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r TD1\requirements.txt

python.exe -m pip install --upgrade pip

cd TD1

python main.py
```