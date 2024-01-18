class Ai:
    
    def __init__(self, api):
        self.api = api
    
    def silmin_generate(self, prompt: str, sampler: str, gender: str, model: str, nsfw: bool) -> dict:
        return self.api.make_request('post', '/ai/silmin_generate', prompt=prompt, sampler=sampler, gender=gender, model=model, nsfw=nsfw)
    
    def silmin_task(self, task_id: str) -> dict:
        return self.api.make_request('post', '/ai/silmin_task', task_id=task_id)
