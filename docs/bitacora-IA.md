# Bitácora de Uso de IA

## Prompt usado
> Vamos a comenzar directamente con el proyecto, dame archivos a crear  
> nunca he usado projects en github, cree el project con plantilla kanban.  
> Crea mis issues como asocio el proyecto a las tareas a los commits?  
> Dame el .gitignore

## Herramienta utilizada
ChatGPT (modelo GPT-5, OpenAI).

## Resumen crítico
Tomé de la IA:
- Estructura de carpetas y archivos iniciales del proyecto.
- Código base para main.py, ingest.py, stats.py y report.py.
- Contenido de .gitignore adaptado para proyecto Python.
- Guía para configurar GitHub Projects, issues y su asociación con commits y PRs.

Descarté:
- Sugerencia de ignorar CSVs adicionales en .gitignore (mantendré control manual).
- Uso de IA para resolver el conflicto en utils.py (no se pidió ayuda en esa parte).

## Cambios realizados sobre la respuesta de la IA
- Ajusté rutas y nombres de archivos para coincidir con la estructura de mi repositorio.
- Reemplacé mensajes impresos por advertencias personalizadas.
- Adapté la lógica de validación de datos para que sea más estricta según el enunciado.
- Error en main.py con las nombres: __name__ y __main__