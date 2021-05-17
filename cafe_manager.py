logo = """
()   ()      ()    /
  ()      ()  ()  /
   ______________/___
   \            /   /
    \^^^^^^^^^^/^^^/
     \     ___/   /
      \   (   )  /
       \  (___) /
        \ /    /
         \    /
          \  /
           \/
           ||
           ||
           ||
           ||
           ||
           /\\
          /;;\\
     ==============
"""
print(logo)
print("====== 카페 관리자 모드에 오신 것을 환영합니다. ======")

menu = ['사과주스', '오렌지주스', '복숭아주스', '키위주스']
user_input = 0
def show_menu(m):
    for i in range(len(m)): 
        print(i+1, m[i])

while True:
    print("""
================================================================
1. 메뉴 보기  2. 메뉴 추가  3. 메뉴 삭제  4. 메뉴 변경  5. 종료
================================================================
""")
    user_input = input("어떤 작업을 하시겠습니까?(1,2,3,4,5) >>> ")

    if user_input == '1':
        print("====== 총 %d 개의 메뉴가 있습니다. ======" % len(menu))
        show_menu(menu)
        print("\n")

    if user_input == '2':
        print("====== 메뉴를 추가합니다. ======")        
        new_item = input("추가할 메뉴를 입력해 주세요. >>>  ")
        menu.append(new_item)
        print("====== 메뉴를 추가하였습니다. ======")
        show_menu(menu)
        print("\n")

    if user_input == '3':
        print("====== 메뉴를 삭제합니다. ======")
        del_item = input("삭제할 메뉴를 입력해 주세요. >>>  ")
        menu.remove(del_item)
        print("====== 메뉴를 삭제하였습니다. ======")
        show_menu(menu)
        print("\n")

    if user_input == '4':
        print("====== 메뉴를 변경합니다. ======")
        show_menu(menu)
        exit_item = input("변경할 메뉴의 번호를 선택해 주세요.>>>  ")
        mod_item = input("변경할 메뉴를 입력해 주세요. >>>  ")
        menu[int(exit_item)-1] = mod_item
        print("====== 메뉴가 변경되었습니다. ======")
        show_menu(menu)        
        print("\n")

    if user_input == '5':
        confirm = input("관리자 모드를 종료합니다(y/n) >>>  ")
        if confirm.lower() == 'y':
            break

