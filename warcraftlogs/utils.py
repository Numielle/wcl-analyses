from requests import Response


def api_error_msg(function_name: str, r: Response) -> str:
    return f'{function_name} failed with status code {r.status_code}. ' \
           f'Error {r.json()["error"]}: {r.json()["message"]}. {r.json()["hint"]}.'
