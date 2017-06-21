#print "Hello World"

from splinter import Browser

with Browser("chrome") as browser:
    # Visit URL
    url = "http://www.phptravels.net"
    browser.visit(url)
    # Find and click the 'search' button
    button = browser.find_link_by_href('http://www.phptravels.net/hotels/singapore/singapore/Rendezvous-Hotels').first
    # repr(button)
    # print (repr(button))
    # Interact with elements
    button.click()
    if browser.is_text_present("Rendezvous Hotels"):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... Try Try Again")

    button = browser.find_by_css(".rooms-update")[1]
    print (repr(button))

    browser.back()

    browser.visit(url)
    button = browser.find_link_by_href("http://www.phptravels.net/hotels/switzerland/messe-basel/Swissotel-Le-Plaza-Basel")
    button.click()
    if browser.is_text_present("Swissotel Le Plaza Basel"):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... Try Try Again")

    button = browser.find_by_css(".rooms-update")[0]
    print (repr(button))

    browser.back()

    browser.visit(url)
    button = browser.find_link_by_href("http://www.phptravels.net/hotels/united-arab-emirates/dubai/Hyatt-Regency-Perth").third
    button.click()
    if browser.is_text_present("Hyatt Regency Perth"):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... Try Try Again")

    button = browser.find_by_css(".rooms-update")[2]
    print (repr(button))


#    print (repr(button))
