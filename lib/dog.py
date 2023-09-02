


from models import Dog  # Import your Dog model here

def create_table(base, db_url):
    # Create the database table if it doesn't exist
    engine = create_engine(db_url)
    base.metadata.create_all(engine)

def save(session, dog):
    # Save a Dog instance to the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Retrieve and return a list of all Dog instances
    return session.query(Dog).all()

def find_by_name(session, name):
    # Find and return a Dog instance by name (or None if not found)
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # Find and return a Dog instance by ID (or None if not found)
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    # Find and return a Dog instance by name and breed (or None if not found)
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    # Update the breed of a Dog instance and save it to the database
    dog.breed = new_breed
    session.commit()






