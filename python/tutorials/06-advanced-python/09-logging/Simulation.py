import logging

logging.basicConfig(
    filename= "app.log_2",
    level= logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s'
)

def login(username):
    logging.info(f"User {username} logged in")

def process_data(data):
    try:
        if data == "bad_data":
            raise ValueError("Invalid Data")
        logging.info(f"Data Processed : {data}")
    except ValueError as e:
        logging.error(f"Error processing the data : {e}",exc_info=True)

def logout(username):
    logging.info(f"User {username} logged out")

if __name__ == "__main__":
    login("Ansh")
    process_data("bad_data")
    logout("Ansh")