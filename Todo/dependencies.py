from typing import Mapping
import service


async def valid_task_id(task_id: int) -> Mapping:
    try:
        task = await service.get_task_by_id(task_id)
    except Exception:
        return 'There is no post with this ID'
    return task
