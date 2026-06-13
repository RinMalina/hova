# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: IdeaVault
def delete_record(record_id: int, collection_name: str) -> bool:
    if not _validate_collection(collection_name):
        print(f"Ошибка: коллекция '{collection_name}' не найдена.")
        return False
    
    try:
        index = records_by_collection[collection_name].index(record_id)
        del records_by_collection[collection_name][index]
        
        # Очистка связей, где эта запись была источником или целью
        for other_col in list(records_by_collection.keys()):
            if record_id not in records_by_collection[other_col]:
                continue
            
            # Удаляем связи, где удаляемая запись была 'from' (source)
            new_connections = [c for c in records_by_collection[other_col] 
                              if c['to'] != record_id and c.get('from') != record_id]
            
            # Удаляем связи, где удаляемая запись была 'to' (target), но только если она не source в другой коллекции
            # Логика: связь A -> B. Если удаляем A, то связь исчезает. Если удаляем B, то связь исчезает.
            # Здесь мы просто фильтруем связи, где одна из сторон - это удаляемая запись.
            
            # Пересобираем список связей для текущей коллекции с учетом удаления
            current_connections = records_by_collection[other_col]
            filtered_connections = []
            for conn in current_connections:
                if conn['from'] != record_id and conn['to'] != record_id:
                    filtered_connections.append(conn)
            
            # Если коллекция связей отличается от текущей, обновляем её (упрощенная модель хранения)
            # В данной реализации records_by_collection хранит сами записи. 
            # Связи должны быть отдельной структурой или частью записи.
            # Предположим, что связи хранятся в отдельном словаре connections_db: {(from_id, to_id): {data}}
            
            if 'connections_db' not in globals():
                print("Ошибка: структура связей не инициализирована.")
                return False
                
            keys_to_remove = [k for k in connections_db.keys() 
                             if record_id == int(k[0]) or record_id == int(k[1])]
            for key in keys_to_remove:
                del connections_db[key]
            
        # Обновление метаданных (если используется)
        metadata['deleted_count'] = metadata.get('deleted_count', 0) + 1
        
        print(f"Запись с ID {record_id} успешно удалена из коллекции '{collection_name}'.")
        return True
        
    except ValueError:
        print(f"Ошибка: запись с ID {record_id} не найдена в коллекции '{collection_name}'.")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка при удалении: {e}")
        return False
