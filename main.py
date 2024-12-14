import time
import ccxt
from termcolor import cprint
import random

# Начало отсчета времени
start_time = time.time()

def binance_withdraw(address, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET):
    account_binance = ccxt.binance({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

    try:
        account_binance.withdraw(
            code=symbolWithdraw,
            amount=amount_to_withdrawal,
            address=address,
            tag=None,
            params={
                "network": network
            }
        )
        cprint(f">>> Успешно | {address} | {amount_to_withdrawal}", "green")
    except Exception as error:
        cprint(f">>> Неудачно | {address} | ошибка : {error}", "red")

if __name__ == "__main__":
    with open("wallets.txt", "r") as f:
        wallets_list = [row.strip() for row in f]

    # Перемешиваем список случайным образом
    random.shuffle(wallets_list)

    symbolWithdraw = 'SOL'
    network = 'SOL'  # ETH | BSC | AVAXC | MATIC | ARBITRUM | OPTIMISM | APT | BASE

    # api_keys of binance
    API_KEY = "API_KEY"
    API_SECRET = "API_SECRET"
    AMOUNT_FROM = 0.15
    AMOUNT_TO = 0.2

    cprint('\a\n/// start withdrawing...', 'white')
    for wallet in wallets_list:
        amount_to_withdrawal = round(random.uniform(AMOUNT_FROM, AMOUNT_TO), 6)
        binance_withdraw(wallet, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET)

        # Время ожидания перед следующей задачей
        wait_time = random.randint(6000, 9000)
        wait_hours, remainder = divmod(wait_time, 3600)
        wait_minutes, wait_seconds = divmod(remainder, 60)
        print(f"Ожидание {wait_hours} часов, {wait_minutes} минут, {wait_seconds} секунд до следующей задачи.")
        
        # Обратный отсчет
        for remaining in range(wait_time, 0, -1):
            remaining_hours, rem = divmod(remaining, 3600)
            remaining_minutes, remaining_seconds = divmod(rem, 60)
            print(f"До следующей задачи осталось: {remaining_hours} часов, {remaining_minutes} минут, {remaining_seconds} секунд", end="\r")
            time.sleep(1)
        print()  # Переход на новую строку после завершения отсчета

# Завершение задачи
end_time = time.time()

# Вычисление прошедшего времени
elapsed_time = end_time - start_time
hours, remainder = divmod(elapsed_time, 3600)
minutes, seconds = divmod(remainder, 60)

# Вывод результата
print(f"Время выполнения: {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд")
print("Конец")
