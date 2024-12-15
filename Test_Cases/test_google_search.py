from selenium import webdriver
from ..Pages.google_home_page import GoogleHomePage
from ..Pages.google_results_page import GoogleResultsPage

def main():
    # WebDriver 초기화 (ChromeDriver가 PATH에 설정되어 있다고 가정)
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # 페이지 객체 초기화
        home_page = GoogleHomePage(driver)
        results_page = GoogleResultsPage(driver)

        # 1. Google 홈페이지로 이동
        home_page.load()

        # 2. "python" 검색
        home_page.search("python")

        # 3. 뒤로 가기
        results_page.navigate_back()

        print("테스트 성공적으로 완료되었습니다.")
    
    except Exception as e:
        print(f"테스트 중 오류 발생: {e}")
    
    finally:
        # WebDriver 종료
        driver.quit()

if __name__ == "__main__":
    main()