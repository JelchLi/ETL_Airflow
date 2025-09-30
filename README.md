# Proyecto Airflow ETL

Este proyecto implementa una arquitectura de orquestación de flujos ETL utilizando Apache Airflow, Docker y servicios complementarios como PostgreSQL y Redis. Está diseñado para facilitar la gestión, ejecución y monitoreo de pipelines de datos en un entorno local de desarrollo.

## Estructura de Carpetas

- **dags/**
  - Contiene los DAGs (Directed Acyclic Graphs) de Airflow, que definen los flujos de trabajo ETL. Ejemplo: `ETL_dummy.py` y `etl_real.py`.
  - Subcarpeta `__pycache__/` almacena archivos compilados de Python para optimizar la ejecución.

- **logs/**
  - Almacena los registros generados por la ejecución de los DAGs y tareas de Airflow.
  - Estructura jerárquica por `dag_id`, `run_id`, `task_id` y `attempt`, permitiendo trazabilidad detallada de cada ejecución.
  - Subcarpeta `dag_processor/` contiene logs específicos del procesador de DAGs, organizados por fecha y tipo de DAG.

- **config/**
  - Incluye archivos de configuración personalizados para Airflow, como `airflow.cfg`, permitiendo ajustar parámetros del entorno y la plataforma.

- **plugins/**
  - Espacio reservado para plugins personalizados de Airflow, que pueden extender la funcionalidad nativa (actualmente vacío).

## Archivos Principales

- **docker-compose.yaml**
  - Define los servicios del entorno: Airflow (varios componentes), PostgreSQL, Redis, Flower y sus dependencias.
  - Permite levantar el entorno completo con un solo comando, facilitando el desarrollo y pruebas locales.

- **Dockerfile**
  - Extiende la imagen oficial de Airflow, instalando dependencias adicionales especificadas en `requirements.txt`.
  - Permite personalizar el entorno de ejecución de Airflow.

- **requirements.txt**
  - Lista de dependencias Python requeridas por los DAGs y el entorno Airflow.

## Funcionamiento General

1. **Orquestación ETL**: Los DAGs en `dags/` definen los procesos ETL, que pueden incluir extracción de datos desde APIs, transformación y carga en bases de datos.
2. **Ejecución y Monitoreo**: Airflow ejecuta los DAGs según la programación definida, almacenando logs detallados en `logs/` para auditoría y depuración.
3. **Configuración Personalizada**: El archivo `airflow.cfg` en `config/` permite ajustar parámetros como conexiones, rutas y seguridad.
4. **Extensibilidad**: La carpeta `plugins/` permite agregar funcionalidades personalizadas a Airflow si es necesario.
5. **Contenerización**: El uso de Docker y `docker-compose.yaml` facilita la replicación del entorno y la gestión de dependencias.

## Implementación

- **Despliegue**: Ejecuta `docker-compose up` para iniciar todos los servicios. Los DAGs se detectan automáticamente desde la carpeta `dags/`.
- **Desarrollo de DAGs**: Agrega o modifica archivos Python en `dags/` para definir nuevos flujos ETL.
- **Logs y Debugging**: Revisa la carpeta `logs/` para analizar el comportamiento y posibles errores de los DAGs y tareas.
- **Configuración**: Modifica `config/airflow.cfg` para personalizar el entorno según tus necesidades.
- **Plugins**: Desarrolla plugins en `plugins/` para extender Airflow si se requiere funcionalidad adicional.

## Recomendaciones

- No usar esta configuración en producción; está pensada para desarrollo local.
- Para agregar dependencias, usa `requirements.txt` y reconstruye la imagen con Docker.
- Consulta la documentación oficial de Airflow para mejores prácticas y personalización avanzada.

---

**Autor:**
- Adaptado y documentado por el equipo de desarrollo.
# ETL_Airflow
