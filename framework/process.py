
from tenacity import retry, stop_after_attempt, wait_fixed
import json

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def process_item(item, logger):
    logger.info(f"Processando item ID {item['id']}: valor = {item['value']}")
    if item["value"] == "b":
        raise Exception("Erro simulado para item 'b'")
    logger.info(f"Item ID {item['id']} processado com sucesso")

def run(context, logger):
    retry_count = context["settings"].get("retry_count", 2)
    queue = context["queue"]

    for item in queue:
        if item["status"] != "new":
            continue

        try:
            process_item.retry.stop = stop_after_attempt(retry_count)
            process_item(item, logger)
            item["status"] = "success"
        except Exception as e:
            item["attempts"] += 1
            item["status"] = "failed"
            logger.error(f"Item {item['id']} falhou após {item['attempts']} tentativa(s): {e}")

    with open("data/queue.json", "w") as f:
        json.dump(queue, f, indent=2)
