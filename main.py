
from framework import init, process, end, exception_handler
from framework.logger import setup_logger
#from reframework_python.framework.logger import log_info
from utils.stock_scraper import get_top_gainers

def main():
    logger = setup_logger()
    state = "Init"

    try:
        logger.info("Iniciando processo")
        init_data = init.run(logger)
        state = "Process"

        logger.info("Iniciando automação de maiores altas da bolsa...")
        top_gainers = get_top_gainers()
        for stock in top_gainers:
            print(f"{stock['ticker']};{stock['name']};{stock['price']};({stock['change_percent']})")

        process.run(init_data, logger)
        state = "End"

    except Exception as e:
        logger.error(f"Erro no estado '{state}': {str(e)}")
        exception_handler.handle(e, logger)

    finally:
        end.run(logger)
        logger.info("Processo finalizado")

if __name__ == "__main__":
    main()
