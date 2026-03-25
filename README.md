# NormaLex — Plataforma de Inteligencia Regulatoria

Plataforma local para monitoreo regulatorio y legislativo del sector financiero peruano.

## Estructura

```
normalex/
├── index.html          ← Plataforma (abrir en navegador)
├── server.py           ← Servidor local
├── generate_data.py    ← Generador de JSON desde Excel
├── README.md
└── data/
    ├── BD_LIMPIOS.xlsx ← Base de datos limpia
    ├── instrumentos.json
    ├── eventos.json
    └── stats.json
```

## Uso rápido

```bash
python server.py
```

Se abre automáticamente `http://localhost:8000` en tu navegador.

## Si actualizas el Excel

```bash
python generate_data.py
python server.py
```

## Requisitos

- Python 3.7+
- pandas (`pip install pandas openpyxl`)

## Vistas

- **Dashboard** — Estadísticas generales, gráficos y actividad reciente
- **Buscador General** — Búsqueda transversal con filtros combinables
- **Issue Tracker** — Seguimiento de proyectos de ley por estado
- **Monitor Normativo** — Normas publicadas (resoluciones, decretos, circulares)
- **Consultas Regulatorias** — Proyectos normativos en consulta pública
- **Actividad Reciente** — Timeline cronológico
