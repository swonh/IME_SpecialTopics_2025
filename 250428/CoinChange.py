def coin_change(money):
    coin = [7, 5, 1]
    count = 0
    for i in range(len(coin)):
        count = money // coin[i] # 동전 수
        money = money % coin[i] # 남은 돈
        if count != 0:
            print('{:3}원짜리 동전: {:2}개'.format(coin[i], count))

change = input('거스름돈을 입력하시요: ')
coin_change(int(change))
        