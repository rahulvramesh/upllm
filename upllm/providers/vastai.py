import httpx
from upllm.providers.provider import Provider
from typing import Optional
from vastai import VastAI


class VastAIProvider(Provider):

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or "YOUR_VASTAI_API_KEY"

    def create_instance(self, model: str, gpu_type: str = "RTX 3090") -> int:
        vast_sdk = VastAI(api_key=self.api_key)

        msg = vast_sdk.launch_instance(
            num_gpus="1",
            gpu_name="RTX_3090",
            image="pytorch/pytorch"
        )

        print(msg)

    def terminate_instance(self, instance_id: int) -> None:
        vast_sdk = VastAI(api_key=self.api_key)

        msg = vast_sdk.terminate_instance(instance_id)

        print(msg)

    def get_instance_status(self, instance_id: int) -> str:
        vast_sdk = VastAI(api_key=self.api_key)

        msg = vast_sdk.get_instance_status(instance_id)

        print(msg)
