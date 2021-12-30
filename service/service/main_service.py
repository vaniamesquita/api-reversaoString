import time
import json
from typing import Text
from loguru import logger
from service.constants import mensagens
import pandas as pd


class StringReverseService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o serviço
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

        
        response_predicts = [text [::-1] for text in texts['textoMensagem']]
        # response_predicts = [text.lower() for text in texts['textoMensagem']]

        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['resultado'] = response_predicts

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {
                     "stringReverso": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    