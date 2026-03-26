install:
	uv sync


brain-games:
	uv run brain-games


build:
	uv build


package-install:
	uv tool install dist/*.whl

lint:
	.venv/bin/ruff check brain_games/
