# Project Structure

```yaml
myproject
|---database.py         # DB connection & base
|---models.py           # SQLAlchemy models
|---crud.py             # CRUD functions
|---mai.py              # main script
|---requirements.txt    # dependecnies

```


### Python virtual env
```bash
python -m venv venv
cd venv\Scripts
activate.bat
```

### install dependenices
```bash
pip install -r requirements.txt
```

### write dependencies
```
mysql-connector-python==8.0.33
SQLAlchemy==1.4.46
```

### Run the app
```bash
python main.py
```