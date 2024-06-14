run:
	uvicorn main:app --port 8000 --reload 

revision:
	alembic revision --autogenerate -m "注释"

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade base
