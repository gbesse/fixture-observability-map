# fixture-observability-map

## Français

Déterminer les défauts indiscernables et les mesures qui les séparent.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m fixture_observability_map examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Construit les signatures de chaque défaut et cherche exactement le sous-ensemble de mesures de coût minimal qui conserve toutes les distinctions possibles. Les défauts structurellement indiscernables restent en classes explicites. Différent de MeasurePlan : objectif d’identifiabilité plutôt que couverture de contrôles.

### Limites

64 hypothèses et 16 mesures déterministes maximum ; résultats déclarés sans bruit, aucune découverte de panne ni calibration physique. Méthode classique de séparation de signatures.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find indistinguishable faults and measurements that separate them.

Synthetic data; no network access or secret required.

```sh
python -m fixture_observability_map examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Builds fault signatures and exactly searches for the minimum-cost measurement subset preserving all possible distinctions. Structurally indistinguishable faults remain explicit classes. Unlike MeasurePlan, the objective is identifiability rather than inspection coverage.

### Limits

At most 64 hypotheses and 16 deterministic measurements; declared noiseless outcomes, no fault discovery or physical calibration. Classical signature-separation method.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar fallos indistinguibles y mediciones que los separan.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m fixture_observability_map examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Construye firmas de fallos y busca exactamente el subconjunto de medidas de coste mínimo que conserva todas las distinciones posibles. Los fallos indistinguibles quedan en clases explícitas. A diferencia de MeasurePlan, busca identificabilidad, no cobertura de controles.

### Límites

Máximo 64 hipótesis y 16 mediciones deterministas; resultados declarados sin ruido, sin descubrimiento de fallos ni calibración física. Método clásico de separación de firmas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.atomicmachines.com/
- https://github.com/gbesse/measureplan
