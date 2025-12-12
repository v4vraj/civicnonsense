import os
import httpx

KESTRA_URL = os.getenv("KESTRA_URL", "http://localhost:8080")
KESTRA_NAMESPACE = os.getenv("KESTRA_NAMESPACE", "company.team")
KESTRA_FLOW_ID = os.getenv("KESTRA_FLOW_ID", "spider_641349")


async def trigger_kestra(post_id: str, image_url: str, timeout: int = 10):
    """
    Trigger a Kestra flow asynchronously.
    Safe: does not raise errors to the caller, only logs.
    """
    payload = {
        "namespace": KESTRA_NAMESPACE,
        "id": KESTRA_FLOW_ID,
        "inputs": {
            "post_id": post_id,
            "image_url": image_url
        }
    }

    headers = {"Content-Type": "application/json"}

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.post(
                f"{KESTRA_URL}/api/v1/executions",
                json=payload,
                headers=headers
            )
            resp.raise_for_status()
            data = resp.json()
            print(f"[Kestra] Execution started: {data.get('id')}")
            return data

    except Exception as e:
        print(f"[WARNING] Kestra trigger failed for post {post_id}: {e}")
        return None
