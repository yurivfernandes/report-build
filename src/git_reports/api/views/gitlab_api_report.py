import json
import sys

import httpx
import pandas as pd
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from git_reports.settings._git_credentials import GITLAB_TOKEN, GITLAB_URL

# SUBSTITUA O GITLAB_TOKEN PELA STRING COM O TOKEN DO SEU GITLAB
# SUBSTITUA O GITLAB_URL PELA STRING COM A URL DO SEU GITLAB.


class GITLABReport(APIView):
    """Efetua a consulta na api do GITLab e retorna um relatório das modificações efetuadas."""

    def __init__(self, **kwargs) -> None:
        self.project_id = kwargs.get("project")
        self.commit_id = kwargs.get("commit")

    def get(self, request: Request, *args, **kwargs) -> Response:
        self.project_id = request.query_params.get('project')
        self.commit_id = request.query_params.get('commit')
        return Response(self.main())

    def main(self) -> list:
        self._extract_and_transform_dataset()
        return self.dataset.to_dict(orient='records')

    def _extract_and_transform_dataset(self) -> None:
        """Extrai e transforma o dataset principal"""
        self.dataset = (
            self._get_git_commits
            .assign(
                new_path=lambda d_: d_['new_path'].astype(str),
                info=lambda d_: d_.apply(lambda row: {
                    'new_path': row['new_path'],
                    'old_path': row['old_path'],
                    'is_new_file': row['is_new_file'],
                    'is_renamed_file': row['is_renamed_file'],
                    'is_deleted_file': row['is_deleted_file'],
                    'changes': row['changes'].replace(" ", "")},
                    axis=1))
            .loc[lambda d_: d_['new_path'].str.endswith('.py')]
            .drop([
                'new_path', 'old_path', 'is_new_file',
                'is_renamed_file', 'is_deleted_file',
                'changes'],
                axis=1))

    @property
    def _get_git_commits(self) -> pd.DataFrame:
        """Busca os dados da API do Git Lab para efetuar os tratamentos necessários"""

        api_url = f"{GITLAB_URL}{self.project_id}/repository/commits/{self.commit_id}/diff"
        headers = {"Private-Token": GITLAB_TOKEN}
        field_map = {
            'diff': 'changes',
            'old_path': 'old_path',
            'new_path': 'new_path',
            'new_file': 'is_new_file',
            'renamed_file': 'is_renamed_file',
            'deleted_file': 'is_deleted_file'}
        try:
            response = httpx.get(api_url, headers=headers)

            if response.status_code == 200:
                return (
                    pd.DataFrame(response.json(), columns=field_map.keys())
                    .rename(columns=field_map))
            else:
                print(f"Erro na requisição: {response.status_code}")
                print(response.text)
                sys.exit(f"Erro na requisição: {response.status_code}")
        except httpx.RequestError as e:
            print(f"Erro na requisição HTTP: {e}")
            sys.exit(f"Erro na requisição HTTP: {e}")
        except Exception as e:
            print(f"Erro desconhecido: {e}")
            sys.exit(f"Erro desconhecido: {e}")
