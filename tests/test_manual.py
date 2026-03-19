def test_login(page):

    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    # After logging in, checks whether the inventory page is actually displayed
    assert page.locator(".inventory_list").is_visible()