from fastapi import FastAPI

# Создаем экземпляр приложения
app = FastAPI()

# Декоратор определяет HTTP-метод (GET) и путь (корневой "/")
@app.get("/00")
def read_root():
    # Возвращаем JSON-ответ
    return {"Hello": "World"}

