# HW42
## Запуск сервера
python main.py
## Создание продукта
Invoke-WebRequest -Uri "http://localhost:5000/api/v1/product" -Method Post -ContentType "application/json" -Body '{"name": "Название продукта", "price": 10.0}' либо curl -X POST http://localhost:5000/api/v1/product -H "Content-Type: application/json" -d '{"name": "Название продукта", "price": 10.0}'
## Получение всех продуктов
curl http://localhost:5000/api/v1/product?page=0&limit=10
