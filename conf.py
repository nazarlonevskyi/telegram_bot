from enum import Enum


token = '1840540698:AAGKA7APuisEq7pGfvhqAMByeV502f92TXs'
db_file = 'database.vdb'
random_dog_api = 'https://random.dog/woof.json'
random_stats_api = 'https://api.thedogapi.com/v1/breeds/4'
random_stats_api_1 = 'https://api.thedogapi.com/v1/breeds/5'
random_stats_api_2 = 'https://api.thedogapi.com/v1/breeds/6'

# Образливі повідомлення
offensive_messages = ["поганий", "тупий", "нефункціональний", "дурний", "кончений",]
# Приємні повідомення
love_messages = ["крутий", "ти мені подобаєшся", "i love you", "дякую"]
class States(Enum):
    """
    Використовується БД Vedis, в якій всі збережені значеня,
    тому і тут будуть використовуватися також рядки (str)
    """
    S_START = "0"  # Початок нового діалогу
    S_ENTER_NAME = "1"  # Введення імені користувача
    S_SEND_PIC_FOR_AGE = "2"  # Введення фото для визначення віку
    S_ENTER_QUESTION = "3" # Введення питання для "так чи ні"