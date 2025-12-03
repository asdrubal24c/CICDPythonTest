# CICD Python Test

Proyecto mínimo para probar pipelines CI/CD.

Contenido:
- `src/main.py`: función `add` y CLI de ejemplo.
- `tests/test_main.py`: tests con pytest.
- `.github/workflows/test_and_build.yml`: workflow de GitHub Actions que ejecuta `pytest`.

Cómo ejecutar localmente:

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```
# CICDPythonTest
Mini test with Github actions and python test
