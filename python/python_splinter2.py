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
        print("No, it wasn't found... Try Try Again")


    button = browser.find_link_by_text('Games')
    # Interact with elements
    button.click()
    if browser.is_text_present("Touch Press Games for Schools via Amplify"):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... Try Try Again")


    button = browser.find_link_by_text('Assessment')
    # Interact with elements
    button.click()
    if browser.is_text_present("Assessment"):
        print("Yes, the official Amplify website was found!")
    else:
        print("No, it wasn't found... Try Try Again")

    #button = browser.find_by_text('#pop-up')
    #button.click()


    button = browser.find_link_by_text('Services')
    # Interact with elements
    button.click()
    if browser.is_text_present("Services"):
        print("Yes, the official Amplify website was found!")
    else:
        print("No, it wasn't found... Try Try Again")


    button = browser.find_link_by_text('Blog')
    # Interact with elements
    button.click()
    if browser.is_text_present("Amplify Blog"):
        print("Yes, the official Amplify website was found!")
    else:
        print("No, it wasn't found... Try Try Again")

    browser.back()

    button = browser.find_link_by_text('Assessment')
    button.click()
    if browser.is_text_present("Amplify"):
        print("Yes, the official Amplify website was seen!")
    else:
        print("No, it wasn't found... Try Try Again")


    button = browser.find_link_by_href('/company')
    button.click()
    if browser.is_text_present("Company"):
        print("Yes, the official Amplify website is displaying correctly!")
    else:
        print("No, it wasn't found... Please Try Try Again")


    button = browser.find_link_by_href('/leadership')
    button.click()
    if browser.is_text_present("Amplify"):
        print("If Correct, lebron will win the championship")
    else:
        print("No, it wasn't found... You lose -_-")


    button = browser.find_link_by_href('/partners')
    button.click()
    if browser.is_text_present("Clever"):
        print("If Correct, partners are important to have")
    else:
        print("No, it wasn't found... Partners are not around")


    button = browser.find_link_by_href('/newsroom')
    button.click()
    if browser.is_text_present("announcement"):
        print("If Correct, we will be in the CNN newsroom")
    else:
        print("No, it wasn't found... The newsrooms are closed")
