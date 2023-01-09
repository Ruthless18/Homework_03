from fastapi import APIRouter

router = APIRouter(
    prefix = "/items",
    tags = ["items"],
)

@router.get("")
def get_items():
    return {
        "data": [
            {
                "id": 1,
                "value": "qwerty",
            },
            {
                "id": 2,
                "value": "wasd",
            },

        ]
    }


@router.get("/{item_id}")
def get_item(item_id: int):
    return {
        "item": {"id": item_id},
    }

@router.post("")
def create_item(data: dict):
    return {
        "item": data,
    }