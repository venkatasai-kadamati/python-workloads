1. If issue of onedrive sync is noticed when installing packages in venv. Then use the below command

```python
uv pip install fastapi uvicorn --link-mode copy
```

2.Understand the below block clearly

```python
# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```
