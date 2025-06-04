
import json

def run(logger):
    logger.info("Executando etapa de inicialização")

    with open("config/settings.json") as f:
        settings = json.load(f)

    with open("data/queue.json") as f:
        queue = json.load(f)

    logger.info(f"Fila carregada com {len(queue)} itens")
    return {"settings": settings, "queue": queue}
