import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def main():
    # 1️⃣ Chrome 옵션 설정
    options = Options()
    options.add_argument("--start-maximized")  # 브라우저 창 최대화
    options.add_argument("--disable-notifications")  # 알림 비활성화

    # 3️⃣ Chrome WebDriver 시작
    driver = webdriver.Chrome(options=options)
    
    try:
        # 4️⃣ www.google.co.kr로 이동
        driver.get('https://www.google.co.kr')
        print("🔗 구글 페이지로 이동했습니다.")

        # 5️⃣ 검색창 찾기 (name 속성이 "q"인 입력 필드)
        search_box = driver.find_element(By.NAME, 'q')

        # 6️⃣ "python" 입력 후 Enter 키 누르기
        search_box.send_keys('python')
        search_box.send_keys(Keys.RETURN)  # 또는 search_box.submit()

        print("🔍 'python' 검색어를 입력했습니다.")

        # 7️⃣ 잠시 대기 (검색 결과 페이지 로딩 대기)
        time.sleep(5)  # 필요에 따라 조정 가능

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

    finally:
        # 8️⃣ 브라우저 종료
        print("🚪 브라우저를 종료합니다.")
        driver.quit()


if __name__ == "__main__":
    main()