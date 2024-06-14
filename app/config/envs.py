from environs import Env

env = Env()
env.read_env()

JWT_SECRET = env.str("JWT_SECRET")
JWT_ALGORITHM = env.str("JWT_ALGORITHM")

PORT = env.int("PORT")
HOST = env.str("HOST")

DB_URL = env.str("DB_URL")