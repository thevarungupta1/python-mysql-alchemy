from database import SessionLocal, engine, Base
from crud import (
    create_user,
    get_user,
    get_users,
    update_user,
    delete_user
)

def init_db():
    """Create the database tables."""
    Base.metadata.create_all(bind=engine)
    
def demo_crud():
    db = SessionLocal()
    
    print("--- Creating User ---")
    mark = create_user(db, name = "Mark", email= "m@gmail.com")
    paul = create_user(db, name = "paul", email= "p@gmail.com")
    print(mark, paul, sep="\n")
    
    print("\n --- Reading Users ---")
    print("All User: ", get_users(db))
    print("Get User #1:", get_user(db, mark.id))
    
    print("\n --- Upating User ---")
    updated = update_user(db, mark.id, name = "John", email = "j@gmail.com")
    print("After updated: ", updated)
    
    print("\n --- Deleting User ---")
    success = delete_user(db, paul.id)
    print(f"Deleting Paul? {success}")
    
    print("\n --- Final Users ---")
    print(get_users(db))
    
    db.close()
    
if __name__ == "__main__":
    init_db()
    demo_crud()