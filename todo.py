import json
import os # 파이썬을 이용해서 시스템 내부에 접근이 가능하다. 

task_file = 'task.json'

def load_task():
    if os.path.exists(task_file): #파일이 있는경우
        with open(task_file, 'r', encoding='utf-8') as file: #->file open(task_file, 'r' encoding='utf-8')
            return json.load(file) #json.() 함수라고 안하고 메소드는 클래스 안에 구현된 함수다.
    return []

def save_task(tasks): #add_task를 통해 전달받은 일들을 저장하는 기능
    with open(task_file, 'w', encoding='utf-8') as file: #->file open(task_file, 'w' encoding='utf-8')
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def add_task(task_name):  # add_task를 통해 전달받은 할 일 추가하는 함수
    tasks = load_task() #파일이 있다면 가져온다.
    tasks.append({"task": task_name, "completed": False})  #task_name에 대한 데이터가 들어감.
    save_task(tasks)
    print(f"'{task_name}' 할 일이 추가되었습니다.")

def view_task():  # 할 일 목록보기
    tasks = load_task() 
    if not tasks:  
        print("할 일이 없습니다.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "완료" if task["completed"] else "미완료"
            print(f"{idx}. {task['task']} [{status}]")

def complete_task(task_number): # 할 일 완료
    tasks = load_task() 
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_task(tasks)
        print(f"'{tasks[task_number - 1]['task']}' 할 일이 완료되었습니다.")
    else:
        print("잘못된 번호입니다.")

def delete_task(task_number): # 할 일 삭제
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_task(tasks)
        print(f"'{removed_task['task']}' 할 일이 삭제되었습니다.")
    else:
        print("잘못된 번호입니다.")

def show_menu():  # 메뉴를 보여주는 함수
    print("작업 관리 애플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")

def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ") #1
        if choice == '1':
            task_number = input("추가할 할 일을 입력하세요: ") # 파이썬 공부하기 
            add_task(task_number)
        elif choice == '2':
            view_task()
        elif choice == '3':
            task_number = int(input("완료할 할 일 번호를 입력하세요: "))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input("삭제할 할 일 번호를 입력하세요: "))
            delete_task(task_number)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 1~5번까지 다시 시도하세요.")

if __name__ == "__main__":
    main()
