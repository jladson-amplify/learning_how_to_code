from splinter import Browser

with Browser("chrome") as browser:
    # Visit URL
    url = "https://www.amplify.com"
    browser.visit(url)
    # Find and click the 'search' button
    button = browser.find_link_by_text('Curriculum')
    # Interact with elements
    button.click()
    if browser.is_text_present("Amplify curriculum products"):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")

    button = browser.find_link_by_text('Games')
    # Interact with elements
    button.click()
    if browser.is_text_present("Touch Press Games for Schools via Amplify"):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
