# task-api

CRUD-сервис для управления задачами. FastAPI + Docker + автодеплой

## Локальный запуск 

    conda create -y -n task-api python=3.11
    conda activate task-api
    pip install -r requirements.txt
    uvicorn app.admin:app --reload

Документация: http://127.0.0.1:8000/docs