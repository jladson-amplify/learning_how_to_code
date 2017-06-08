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
