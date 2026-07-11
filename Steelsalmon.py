lose=0
#1장
while True :
    print("-"*100)
    print("====================1장 시작====================")
    print("엣날에 외계인이 죽었다.")
    print("근데 죽은 사람 DNA랑 외계인 DNA랑 합쳐졌다.")
    print("그래서...")
    print("그래서 새로운 생명체가 생겼다. 그의 이름은 강철연어")
    print("강철연어가 갑자기 심장병 때문에 죽었다.")
    name=input("당신은 의사고 연구원들이 당신에게 강철연어를 연구해야해서 다시 살려달라고 부탁했다. 당신의 이름은: ")
    answerone=input("a=강철을 분리한다음 심장을 고친다. b=그냥 고친다: ")
    if answerone=="a":
               print("강철이 터졌다.")
               print(name+"가 죽었다.")
               lose=lose+1
    if answerone=="b":
        print("근데 생각보다 고치는게 쉬웠다.")
        print("하지만 이제 다시"+name+"가 연구원에게 살아있는 연어를 줘야했다.")
        answertwo=input("a=물 안에 넣은다. b=모래에 넣은다음 연구원들에게 준다:")
        if answertwo=="a":
            print("강철연어는 물을 싫어한다. 강철연어가 "+name+"를 죽였다.")
            lose=lose+1
        if answertwo=="b":
            print("강철연어는 모래를 좋아한다.")
            print("강철연어의 가족이 당신에게 좀비 칼을 주었다")
            answerthree=input("a=받기 b=안받기: ")
            if answerthree=="a":
                print("좀비칼에서 갑자기 좀비가 스폰되었다."+name+"가 죽었다.")
                lose=lose+1
            if answerthree=="b":
                print("안 받았다.")
                print("하지만 무언가가 이상한 느낌이 든다.")
                print("어쨌든 "+name+"의 눈앞에 버튼이 두개 있었다")
                answerfour=input("a=왼쪽 버튼 누른다 b=오른쪽 *힌트= 지금까지 정답이 다 b였다. 이제 a가 나올 시간이 되지 않았는가?: ")
                if answerfour=="a":
                    print("정답은 또 b였다. 버튼이 터졌다."+name+"가 죽었다.")
                    lose=lose+1
                if answerfour=="b":
                    print(name+"는 화성으로 텔레포트 했다")
                    print("마침내 우주선이 있었다.")
                    answerfive=input("a=안탄다 b=탄다 힌트=c: ")
                    if answerfive=="c":
                        print("c는 선택지에 없었다. 언제나 힌트를 믿지말라.")
                        lose=lose+1
                    if answerfive=="b":
                        print("우주선이 터졌다."+name+"가 죽었다.")
                        lose=lose+1
                    if answerfive=="a":
                        print("갑자기 날는 하마가 "+name+"를 가지고 집으로 데려갔다.")
                        print("하지만 강철연어가 있었다.")
                        print("강철연어가 당신을 배신해서 당신에게 총을 쐈다.")
                        print("====================1장 끝 2장 시작====================")
                        break
                        
    else :
        print("선택지중 하나를 골라라. 아니면 강철연어가 너를 죽인다.")


#2장
while True:
    print("-"*100)
    print("====================2장 시작====================")
    print(name+"가 지옥으로 갔다.")
    print("지옥 신이 "+name+"를 지옥 안에 던졌다.")
    answersix=input("a=자폭하기 b=그냥기다리기: ")
    if answersix=="b":
        print("너무 뜨겁다."+name+"가 죽었다.")
        lose=lose+1
    if answersix=="a":
        print("지옥이 폭발했다. 다시 지구로 돌아왔다.")
        print("지구에서는 강철연어가 "+name+"을 기다리고 있었다")
        answerseven=input("a=싸우기(강철을 부수기) b=숨기: ")
        if answerseven=="a":
            print("기억을 해봐라. 1장에서 이미 힌트가 있었다.")
            print("이미 강철연어는 그의 강철이 분리되면 터진다고 나왔다.")
            print(name+"는 죽었다.")
            lose=lose+1
        if answerseven=="b":
            print(name+"가 숨었다.")
            answereight=input("a=동맹하자고 하기 b=심장을 공격하기: ")
            if answereight=="b":
                print("강철연어는 이미 알고 있었다.")
                print("강철연어가 "+name+"를 죽였다.")
                lose=lose+1
            if answereight=="a":
                print(name+"가 강철연어랑 동맹을 했다.")
                print("하지만 어느날, 강철연어가 아이돌 그룹에 들어갔다.")
                answernine=input("a=당신도 아이돌그룹에 들어가기 b=안들어가기: ")
                if answernine=="b":
                    print("강철연어가 슬퍼한다. 강철연어가 "+name+"을 죽였다.")
                    lose=lose+1
                if answernine=="a":
                    print("강철연어가 좋아한다. 강철연어가 보상으로 "+name+"에게 좀비칼을 주었다.")
                    answerten=input("a=받기 b=안받기: ")
                    print("갑자기 코끼리들이 공격한다.")
                    if answerten=="b":
                        print(name+"는 코끼리들을 공격할 무기가 없다.")
                        print(name+"는 죽었다.")
                        lose=lose+1
                    if answerten=="a":
                        print(name+"는 좀비칼에서 좀비를 스폰했다.")
                        print("그래서 좀비들을 죽일줄.... 알았는데,,,")
                        print("오히려 코끼리 좀비가 탄생했다.")
                        print("그 뉴스를 들은 강철연어는 "+name+"를 도와주고 좀비 코끼리들을 죽여준다.")
                        print("====================2장 끝 3장 시작====================")
                        break
    else:
        print("선택지중 하나를 골라라. 아니면 강철연어가 너를 죽인다.")

#3장
while True:
    print("-"*100)
    print("====================3장 시작====================")
    print("하지만 문제가 생겼다.")
    print("강철연어가 좀비한테 물렸다.")
    answereleven=input("a=치료 해주기 b=배신하고 도망가기: ")
    if answereleven=="a":
        print("치료를 하다가 "+name+"도 물렸다...")
        print("죽었다.")
        lose=lose+1
    if answereleven=="b":
        print(name+"가 도망쳤다.")
        print("쓰레기통 뒤에 숨었다.")
        print("하지만 거기에 쪽지가 있었다 <좀비칼을 부수면 좀비들이 없어진다.>라고 쓰여있었다.")
        answertwelve=input("a=좀비칼 부수기 b=아무것도 안하기: ")
        if answertwelve=="a":
            print(name+"가 좀비칼을 부시려 가고있었는데 강철연어가 당신을 찾고 죽였다.")
            lose=lose+1
        if answertwelve=="b":
            print("기다리고 있었다.")
            print("딱 그때, 강철연어가 좀비칼을 밟았다. 좀비칼이 부셔졌다.감염자들은 다 죽었다.")
            answerthirteen=input("a=자폭하기 b=집으로 가서 쉬기: ")
            if answerthirteen=="b":
                print("집에서는 부활한 강철연어가 기다리고 있었다.")
                print(name+"가 죽었다.")
                lose=lose+1
            if answerthirteen=="a":
                print(name+"가 지옥으로 텔레포트 되었다")
                print("보스가 기다리고 있었다. 보스는 마술로 다시 지옥을 고쳐놨다. ")
                print("보스가 "+name+"가 지옥을 폭발시켜서 화나있었다.")
                answerfourteen=input("a=싸우기 b=미안하다고 하기: ")
                if answerfourteen=="b":
                    print(name+"는 벌로 사형을 선고받았다")
                    print(name+"가 죽었다.")
                    lose=lose+1
                if answerfourteen=="a":
                    print("알고보니 형편없이 역한 괴물이었다.")
                    print("갑자기 집으로 테레포트 되었다.")
                    print(name+"는 잠시 생각했다.........")
                    print("이곳은 현실인가?")
                    print("현실이라는 곳이 아예 존재하나?")
                    print("이 신비로운 이야기는 여기서 끝난다.")
                    break
    else:
        print("선택지중 하나를 골라라. 아니면 강철연어가 너를 죽인다.")

#ending
print("====================3장 끝 <THE END>====================")
print("이 작품은 최민우라는 잘생기고 똑똑한 사람이 정성을 담고 만든 게임입니다.")
print("플레이 해주셔서 안 감사합니다.")
print("🎮")
print("진 횟수:", lose)
