from . import models


def catch(values: str) -> list[int]:
    values = values.split(", ")
    return [int(value) for value in values]


def delete_objs(ids):
    counter, not_found = 0, []
    
    for todo_id in ids:
        queryset = models.ToDo.objects.filter(id=todo_id)
        
        if queryset.exists():
            queryset.delete()
            counter += 1
        else:
            not_found.append(todo_id)
    
    return counter, not_found


def construct_message(todo_ids: list[int],  not_found: list[int], counter: int) -> str:
    message = "All elements deleted successfully"
    
    if len(todo_ids) != counter:
        
        has, item, ids = "has", "item", "id"
        if counter > 1:
            has, item = "have", "items"
        elif len(todo_ids) - counter > 1:
            ids = "ids"
        
        message = f"{counter} {item} {has} been deleted, this {ids} {not_found} doesn't exist in the database"
    
    return message
