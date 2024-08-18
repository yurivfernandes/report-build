import json

import requests
from docx import Document
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from git_reports.api.views import GITLABReport
from gpt_reports.settings import FINAL_PLAYBOOK, INITIAL_PLAYBOOK

LINK = "https://api.openai.com/v1/chat/completions"
SALVAR_NA_PASTA = 'C:\\Users\\YuriVianaFernandes\\Downloads\\'
MODEL_4_O = "gpt-4o-2024-05-13"


class GPTReport(APIView):
    """Efetua a consulta na api do GITLab e retorna um relatório das modificações efetuadas."""

    def get(self, request: Request, *args, **kwargs) -> Response:
        self.project_id = request.query_params.get('project')
        self.commit_id = request.query_params.get('commit')
        self.gitlab_url = request.query_params.get("gitlab_url")
        self.gitlab_token = request.query_params.get("gitlab_token")
        self.user_story = request.query_params.get('user_story')
        gpt_api_key = request.query_params.get("gpt_api_key")
        self.headers = {
            "Authorization": f"Bearer {gpt_api_key}",
            "content-type": "Application/json"}
        self.text = None
        self.text = self._get_gpt_data

        if self.text != None:
            self._save_to_word()
            return Response(
                {"message": "O arquivo foi salvo com sucesso na pasta"},
                status=status.HTTP_202_ACCEPTED)
        else:
            return Response(
                {"message": "Não há dados a serem salvos! Verifique os filtros e o commit!"},
                status=status.HTTP_400_BAD_REQUEST)

    def _save_to_word(self):
        """Salva a resposta do gpt em um arquivo do word no computador."""
        doc = Document()
        doc.add_paragraph(self.text)
        doc.save(f'{SALVAR_NA_PASTA}Report{self.commit_id}.docx')

    @property
    def _get_gpt_data(self) -> str:
        """Busca os dados da API do Git Lab para efetuar os tratamentos necessários"""
        print('Iniciado...')
        body = json.dumps({
            "model": MODEL_4_O,
            "messages": [
                {
                    "role": "system",
                    "content": f"{FINAL_PLAYBOOK + str(self.user_story)}"},
                {"role": "user", "content": f"{self._code_analysis_response}"}]})
        print(f'Buscando o relatório final...')
        final_response = requests.post(
            url=LINK, headers=self.headers, data=body)
        print(f'Relatório final recebido. Finalizando a requisição...')
        return final_response.json()['choices'][0]['message']['content']

    @property
    def _code_analysis_response(self) -> list:
        """Cria uma lista com os resultados dos playbooks intermediários"""
        playbooks = self._playbook_dataset
        print('Playbook com os dados do Commit criado...')
        i = 1
        code_analysis_response = []
        for playbook in playbooks:
            body = json.dumps({
                "model": MODEL_4_O,
                "messages": [
                    {"role": "system",
                        "content": f"{INITIAL_PLAYBOOK + str(self.user_story)}"},
                    {"role": "user", "content": f"{playbooks[playbook]}"}]})

            response = (
                requests.post(
                    url=LINK, headers=self.headers, data=body))
            print(f'Enviado o arquivo: {i}. Aguardando Resposta...')
            code_analysis_response.append(
                response.json()['choices'][0]['message']['content'])
            print(f'Resposta do arquivo {i} recebida...')
            i = i+1
        return code_analysis_response

    @property
    def _playbook_dataset(self) -> dict:
        """Método que monta o Playbook para enviar ao GPT"""
        print('Buscando os dados do Commit...')
        files = (
            GITLABReport(
                commit=self.commit_id,
                project=self.project_id,
                gitlab_url=self.gitlab_url,
                gitlab_token=self.gitlab_token)
            .main())
        return {
            'playbook' + str(i+1): file for i,
            file in enumerate(files)}
