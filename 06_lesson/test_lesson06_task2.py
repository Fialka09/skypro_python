from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        driver.get("https://gitflic.ru/")
        driver.delete_all_cookies()
        driver.add_cookie(
            {"name": "SESSION",
             "value": "NWRlNjg2NzgtMTRjMC00MGU2LTk4YjktMWU4YTc2Y2ZmZTEx",
             "domain": "gitflic.ru"})
        driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
        })
        driver.refresh()
        driver.get("https://gitflic.ru/user/test09072026")
        url1 = driver.current_url
        driver.delete_all_cookies()
        driver.add_cookie(
            {"name": "SESSION",
             "value": "ODIwMmI0NmUtYjYxZS00ZmI0LThiOWItNzRlZDU3YzA1OGM5",
             "domain": "gitflic.ru"})
        driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
        })
        driver.refresh()

        driver.get("https://gitflic.ru/user/fialka")
        url2 = driver.current_url

        assert url1 != url2, "URL пользователей должны различаться"
        driver.delete_all_cookies()

    finally:
        driver.quit()
