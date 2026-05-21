# Backend Auth API

🚀 **Swagger UI:** https://backendtask-wc13.onrender.com/docs

REST API с системой аутентификации и разграничения прав доступа на основе ролей.

## Стек

- **FastAPI** — веб-фреймворк
- **PostgreSQL** — база данных
- **SQLAlchemy** — ORM
- **Alembic** — миграции
- **JWT (python-jose)** — токены авторизации
- **bcrypt** — хэширование паролей
- **Docker / Docker Compose** — контейнеризация

## Демо

Swagger UI: https://backendtask-production-1024.up.railway.app/docs

## Запуск локально

```bash
docker compose -p auth up --build
```

Swagger UI: http://localhost:8000/docs

При старте автоматически применяются миграции и заполняются тестовые данные.

## Схема базы данных

| Таблица | Описание |
|---------|----------|
| `users` | Пользователи (email, hashed_password, role_id, is_active) |
| `roles` | Роли (admin, manager, user, guest) |
| `business_element` | Бизнес-объекты системы (users, products, orders, access_rules) |
| `access_role_rule` | Матрица прав: какая роль что может делать с каждым объектом |
| `token_blacklist` | Отозванные JWT токены (logout) |

## Система прав доступа

Каждая роль имеет набор прав на каждый бизнес-объект. Права делятся на:
- `read` / `read_all` — чтение своих / всех записей
- `create` — создание
- `update` / `update_all` — изменение своих / всех записей
- `delete` / `delete_all` — удаление своих / всех записей

| Роль    | products read | products create | orders read | orders read_all |
|---------|:---:|:---:|:---:|:---:|
| admin   | ✅ | ✅ | ✅ | ✅ |
| manager | ✅ | ✅ | ✅ | ✅ |
| user    | ✅ | ❌ | ✅ | ❌ |
| guest   | ✅ | ❌ | ❌ | ❌ |

## Эндпоинты

### Auth
| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/auth/register` | Регистрация |
| POST | `/auth/login` | Логин, возвращает JWT токен |
| POST | `/auth/logout` | Logout, токен добавляется в blacklist |

### Users
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/users/me` | Профиль текущего пользователя |
| PATCH | `/users/me` | Обновление профиля |
| DELETE | `/users/me` | Деактивация аккаунта (soft delete) |

### Mock ресурсы (требует авторизации)
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/mock/products/my` | Мои товары |
| POST | `/mock/products` | Создать товар |
| GET | `/mock/orders` | Мои заказы |
| GET | `/mock/orders/all` | Все заказы (admin / manager) |

### Admin (только для роли admin)
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/admin/users` | Список всех пользователей |
| PATCH | `/admin/users/{user_id}/role` | Изменить роль пользователя |
| GET | `/admin/permissions` | Список всех правил доступа |
| PATCH | `/admin/permissions/{rule_id}` | Изменить правило доступа |

## Тестовые пользователи

| Email | Пароль | Роль |
|-------|--------|------|
| admin@admin.com | admin123 | admin |

Остальных пользователей можно зарегистрировать через `/auth/register` (по умолчанию роль — user).
