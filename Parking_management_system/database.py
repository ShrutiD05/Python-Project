import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vehicle_management"
    )

def add_vehicle_to_db(vehicle_name, owner_name, contact_number, vehicle_type, charges):
    """Function to add a new vehicle to the database."""
    connection = connect_db()
    cursor = connection.cursor()
    query = "INSERT INTO vehicles (vehicle_name, owner_name, contact_number, vehicle_type, charges) VALUES (%s, %s, %s, %s, %s)"
    values = (vehicle_name, owner_name, contact_number, vehicle_type, charges)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def exit_vehicle_from_db(vehicle_name):
    """Function to remove a vehicle from the database."""
    connection = connect_db()
    cursor = connection.cursor()
    query = "DELETE FROM vehicles WHERE vehicle_name = %s"
    values = (vehicle_name,)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

def get_all_vehicles_from_db():
    """Function to get all vehicles from the database."""
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT vehicle_name, owner_name, contact_number, vehicle_type, charges FROM vehicles")
    vehicles = cursor.fetchall()
    cursor.close()
    connection.close()
    return vehicles

def get_vehicle_count():
    """Function to count the total number of vehicles in the database."""
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM vehicles")
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count

def vehicle_exists(vehicle_name):
    """Function to check if a vehicle exists in the database by name."""
    connection = connect_db()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM vehicles WHERE vehicle_name = %s"
    values = (vehicle_name,)
    cursor.execute(query, values)
    exists = cursor.fetchone()[0] > 0
    cursor.close()
    connection.close()
    return exists

def duplicate_vehicle_exists(vehicle_name, owner_name):
    """Function to check if a duplicate vehicle (same name and owner) exists in the database."""
    connection = connect_db()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM vehicles WHERE vehicle_name = %s AND owner_name = %s"
    values = (vehicle_name, owner_name)
    cursor.execute(query, values)
    exists = cursor.fetchone()[0] > 0
    cursor.close()
    connection.close()
    return exists