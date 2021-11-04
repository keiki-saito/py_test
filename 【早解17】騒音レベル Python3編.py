db = int(input())
if db < 30:
    print('quiet')
elif 30 <= db < 50:
    print('normal')
elif 50 <= db < 70:
    print('noisy')
elif 70 <= db:
    print('very noisy')
