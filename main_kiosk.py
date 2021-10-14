############
#### CNU 버거 키오스크 프로그램
#### 일자 : 2021.10.12
#### 작성자 : 박지원
#### 내용 : Console 기반의 햄버거를 판매하는 키오스크 프로그램

# 조건
# 사용자는 최대로 버거 1개, 사이드 1개, 음료 1개를 주문할 수 있습니다.

# 메뉴와 가격표
burger_name = {1: '믹맥', 2 : '화퍼', 3 : '사이버거'}
side_name = {1: '프렌치프라이', 2 : '치킨너겟'}
drink_name = {1:'코카콜라', 2:'커피', 3:'주스'}

#고객 주문 기록 저장 변수
menu_save = {}  # 고객 주문 기록
price_save = {} # 고객 주문 금액 기록

#######################################
# >> View단 : 메뉴 선택(최초)
print('--------------------------')
print('-- == CNU 버거(Ver.01) ==')
print('-- CNU 버거에 오신 것을 환영합니다.')
print('--------------------------')
print('-- 메뉴')
print('-- 1. 햄버거 세트')
print('-- 2. 햄버거 단품')
print('-- 3. 사이드 메뉴')
print('-- 4. 음료')
print('--------------------------')
########################################

###############################################################
while True:
    print('-- 원하시는 메뉴의 번호를 입력해주세요.')
    menu_number = int(input('>> 번호 :')) ## 사용자로부터 입력 받음

    if menu_number >= 1 and menu_number <= 4:
        break
    else:
        print('# MSG : 1~4의 번호만 입력해주세요. :)')
################################################################

################################################################
##
if menu_number == 1:       # 햄버거 세트
    print('------------------------------')
    print('-- 햄버거 메뉴 ---')
    print('-- 1. 믹맥')
    print('-- 2. 화퍼')
    print('-- 3. 사이버거')
    print('-- 원하시는 메뉴의 번호를 입력해주세요.')
    print('-------------------------------')
    while True:
        choice_num = int(input('>> 번호 : '))
        if choice_num >= 1 and choice_num <= 3:
            menu_save['burger'] = burger_name[choice_num]
            price_save['burger'] = burger_name[choice_num]
            break
        else:
            print('-- MSG : 1~3의 번호만 입력해주세요 :)')

    print('-------------------------')
    print('-- SIDE MENU')
    print('-- 1.프렌치프라이: 1,500원')
    print('-- 2.치킨너겟: 2,000원')
    print('-- 원하시는 메뉴의 번호를 입력해주세요.')
    print('-------------------------')
    while True:
        choice_num = int(input('>> 번호:'))
        if choice_num >= 1 and choice_num <= 2:
            menu_save['side_menu'] = side_name[choice_num]
            price_save['side_menu'] = side_name[choice_num]
            break
        else:
            print('-- MSG : 1~2의 번호만 입력해주세요 :)')

    print('-------------------------')
    print('DRINK MENU')
    print('-- 1.코카콜라: 1,000원')
    print('-- 1.커피 : 1,200원')
    print('-- 3.주스 : 1,500원')
    print('-- 원하시는 메뉴의 번호를 입력해주세요.')
    print('--------------------------')
    while True:
        choice_num = int(input('>> 번호 :'))
        if choice_num >= 1 and choice_num <= 2:
            menu_save['drink'] = drink_name[choice_num]
            price_save['drink'] = drink_name[choice_num]
            break
        else:
            print('-- MSG : 1~3의 번호만 입력해주세요.')

elif menu_number == 2:    # 햄버거 단품
    pass
elif menu_number == 3:    # 사이드 메뉴
    pass
elif menu_number == 4:    # 음료
    pass
################################################################

###########################3####
## 3. 주문 메뉴와 금액을 정산 및 출력

# Total 주문 금액 계산
total_price = # ㅆotal 주문 금액

for price in price_save.values():
    total_price += price

price('--------------------------')
print('ㅇ')
price('--------------------------')
for i, menu in enumerate('고객님이 주문하신 메뉴는'):
    print('-- {}'.format(i+1, menu))
print('-- 으로 총 주문금액은 {}원 입니다.'.format(total_price))
print('---------------------------------------------------')
print('-- 이용해주셔서 감사합니다. 또 방문해주세요.')
################################

print('total ', total_price)