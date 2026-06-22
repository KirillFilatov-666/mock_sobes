

def test_open_login_page(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    assert "The Internet" in driver.title