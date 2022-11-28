<h1 align="center">Morgan & Co</h1>

The Full Testing documentation, following on from the README [found here](README.md)

# Testing Table of Contents

1. [Features Testing](#features-testing)
2. [User-Related Image Testing](#user-related-image-testing)
3. [Validation](#validation)
4. [Testing Original User Stories](#testing-original-user-stories)
    - [As a New Visitor](#as-a-new-visitor)
    - [As an Unregistered User](#as-an-unregistered-user-including-all-prior-stories)
    - [As a Shopper](#as-a-shopper-including-all-prior-stories)
    - [As a Registered User](#as-a-registered-user-including-all-prior-stories)
    - [As a Store Owner](#as-a-store-owner-including-all-prior-stories)
5. [Lighthouse](#lighthouse)
6. [Further Testing](#further-testing)
7. [Bug Fixes](#bug-fixes)
8. [Known Bugs](#known-bug)
9. [Testing Credits](#testing-credits)
    - [Reading and Guidence](#reading-and-guidence)
    - [Code](#code)

[Back to table of contents](#table-of-contents)

# Features Testing

[Back to table of contents](#table-of-contents)

# User-Related Image Testing

[Back to table of contents](#table-of-contents)

# Validation

[Back to table of contents](#table-of-contents)

# Testing Original User Stories

Following are the original User Stories set out in the early design stages of the project found on the [README](README.md) page. They were individually tested to see if each goal was satisfied against the completed project.

### As a New Visitor
| User Story ID | I want to: | So that I can: |
| ------------- | ----------| ------------- |
| 001           | Be able to access and view the website on the device I'm using. | View the website without having to change my device. |
| 001 Result    | The website has been tested for ease of access and responsiveness on dozens of devices (handheld devices such as mobile phones and tablets, laptops, desktop computers and larger Samsung TVs) and is fully responsible from at least a minimum of 320px up to at least 1200px. |
| 002           | Immediately understand the purpose of the website. | Decide if it's something I'm interested in. |
| 002 Result    | The background-image, titles, links and other written information along with the products list on display enable first-time users to easily understand the website, the theme and it's purpose. |
| 003           | Be able to navigate the website with ease. | Discover what the website is about and find all that I need. |
| 003 Result    | The website's intuitive design, responsive nav bar with clear and obvious menu options, colour contrast between text and the use of images, interactive prompts and layout make it very easy to navigate for first-time users. |
| 004           | Find the website design visually pleasing. | Have a pleasant experience. |
| 004 Result    | The use of imagery, clean and sophisticated design and pleasant colour palette creates a very enjoyable browsing experience for the user. |
| 005           | Be able to find help and information about the website and company. | Decide if the company is trustworthy and reputable. |
| 005 Result    | General information and links can be found in the website footer, along with the company's dedicated About page and other helpful customer information. |
| 006           | Be able to contact the company if I wish to, by my prefer method. | Easily contact the company and better understand any further queries I have. |
| 006 Result    | The footer contains the company address, email, telephone number and social media links, which is present on every page of the website. Minimal styling ensures that the links and contact info are displayed clearly and to not overwhelm users. All social media links open to a new tab where the user can decide on contacting the company through their desired social media platform. All contact information can also be found on the company's dedicated Contact page.
| 007           | Have a reason to return. | Explore the website further. |
| 007 Result    | There are a number of reasons to return to the Morgan & Co website. Visitors have the option to register for free and have a profile. Registered users with then have exclusive access to the wishlist and review features. To keep up to date with the newest arrivals, new sale products. To quickly purcahse products with or without being a registered user. To easily contact the company. |

### As an Unregistered User (including all prior stories)
| User Story ID | I want to: | So that I can: |
| ------------- | ----------| ------------- |
| 101           | Access and view the website on a number of different devices. | Visit the website from any device I'm currently using or would like to use in the future. |
| 101 Result    | The website has been tested for ease of access and responsiveness on dozens of devices (handheld devices such as mobile phones and tablets, laptops, desktop computers and larger Samsung TVs) and is fully responsible from at least a minimum of 320px up to at least 1200px. |
| 102           | Be able to easily register for an account. | Have my own profile, manage all that I wish from there and make it easier to return to the website. |
| 102 Result    | Anyone can register for free as long as they have an email address and correctly fill the register form. Once this has been confirmed, the registered user can view their profile and have access to all of the website's exclusive features |
| 103           | Buy products without registering. | Save time without needing or wanting to create an account. |
| 103 Result    | Any visitor can go through the process of purchasing products from the website, without the need to register. The checkout form must be filled in correctly and to prodivde a valid and acceptable form of payment. |

### As a Shopper (including all prior stories)
| User Story ID | I want to: | So that I can: |
| ------------- | ----------| ------------- |
| 201           | View a list of all products. | See every item that the company sells. |
| 201 Result    | All products can be viewed by either selecting 'Shop by Items' then 'All Furniture' or by selecting 'Shop by Room' then 'All Rooms' from the navigation bar at the top of the page. Both routes will give you a list of every product on the website |
| 202           | View specific product details. | To gather all information that I need about a certain product e.g price, description, rating and reviews. |
| 202 Result    | Product images can be clicked on (or pressed on) to advance to that specific products product detail page, where further infomation regarding that product is listed such as price, description, rating and reviews. |
| 203           | To quickly search for products by my preferred criteria e.g. name, description. | So that I can quickly find products that suit my desires. |
| 203 Result    | A saerch bar is avaiable on all screen sizes (or through the search icon on mobile), allowing users to search by their preference on names, descriptive words etc. |
| 204           | Easily see what I've searched for and the number of results found. | Quickly see whether the product I want is available. |
| 204 Result    | Once a search is made, a new page informes the user of the number of results found for their search term. This is seen towards the top of the page - just before any products are listed |
| 205           | Easily sort products by name, price and more. | To save time and better my decision-making. |
| 205 Result    | A sorting dropdown is present on every porduct list page. Users can sort products in alphabetical order, price, categories, rooms and specials. These sorting options are in both acending and decending order |
| 206           | Be able to filter products by items. | Find specific items I need without searching the entire product range. |
| 206 Result    | All items can be viewed by selecting 'Shop by Items' > 'All Furniture' from the navigation bar at the top of the page. Specific items can be filtered by selecting 'Shop by Item' then 'Chairs', 'Sofas', 'Tables', 'Cabinets' from the top of the page. This can also be done from the footer at the bottom of every page. |
| 207           | Be able to filter products by different rooms. | Find a range of items that suit a specific room. |
| 207 Result    | All products can be filtered by selecting 'Shop by Room' > 'All Rooms' from the navigation bar at the top of the page. Specific products can be filtered by their rooms by selecting 'Shop by Room' then 'Bedroom', 'Kitchen', 'Dining Room', 'Living Room' from the top of the page. |
| 208           | Find new items. | So that I can find what products are new to the store. |
| 208 Result    | New items to the store can be found be selecting the 'New Arrivals' link at the top of the page in the navigation bar. |
| 209           | Find clearance items. | So that I can find what products are on sale to be cleared and take advantage of the savings. |
| 209 Result    | Clearance products can be found be selecting the red 'Clearance' link towards the top of the page in the navigation bar. |
| 210           | Quickly find out about delivery details. | So that I gather information about cost and when I should receive my order. |
| 210 Result    | The delivery cost is given on the bag and checkout pages. Users are informed of the Free Delivery promotion via the banner found on every page. They are also informed of how much they need to spend to trigger the free delivery promotion whenever they update their bag, via on-screen popups. Delivery details can also be found in the footer links under 'Information'. |
| 211           | Read product reviews. | So that I make a better decision about each product. |
| 211 Result    | Product reviews left by other registered users can be found on product detail pages, underneath the product information. |
| 212           | Select the quantity of items I wish to purchase. | Easily make changes without unnecessary steps/clicks to alter the quantity. |
| 212 Result    | This can be done via the quantity selector on the product detail page before adding to the product to the shopping bag, and again at the shopping bag page before advncing to the checkout page. |
| 213           | Be informed of my bag total. | So that I can be easily informed of how much I'm spending and control that. |
| 213 Result    | Users are informed of their bag total cost by the shopping bag icon located in the navigation bar at the top of the page. An on-screen popup also gives a brief review of the products and cost. These are updated with every change made to their shopping bag. Total cost is also found on the shopping bag page and at the checkout page. |
| 214           | Easily view my bag. | So that I can see what products I have in my bag, the cost and the quantity before checkout. |
| 214 Result    | Simply click on the shopping bag icon within the navigation bar at the top of the webiste at any time. |
| 215           | Know that my information and payment details are safe and secure. | So that I can shop with confidence and feel safe about giving my personal details. |
| 215 Result    | All company information and contact information is provided. Payment details are secured using _____ and handled via stripes ______. |
| 216           | Easily enter my payment information. | Check out quickly without needing to create an account or following numerous steps. |
| 216 Result    | Users can buy products without creating an account by just filling in the necessary delivery and payment information. |
| 217           | Recieve an order review after checkout. | So that I can quickly see my purchase and check if I purchased all that I needed. |
| 217 Result    | Once checkout is complete, the user is met with an order review. This specifies the users name, the order number, order date, products bought, the quantity, the individiual and total price, delivery cost if applicatable and delivery address. The user email is also given. |
| 218           | Recieve a confirmation via email of my order. | Keep the order confirmation as proof of purchase. |
| 218 Result    | An email is automatically sent out the the users email address given at the checkout form. This is directed personally to the user and specifies an order number, date, address to be delivered to and the cost details. The company email is given incase the customer wishes to contact Morgan & Co. |


### As a Registered User (including all prior stories)
| User Story ID | I want to: | So that I can: |
| ------------- | ----------| ------------- |
| 301           | Have my own personal profile with some management options. | Manage my own personal information. |
| 301 Result    | Registed users can view their profile from the 'My Account' logo then select 'My Profile'. Their default delivery address is saved here and can be updated too. An order history and a link to their wishlist is also present. |
| 302           | Have access to more features. | Justfiy registering to the website. |
| 302 Result    | Registered users have profile management, a wishlist feature and a review feature. |
| 303           | Recieve an email confirmation after registering. | Verify that my account registration was successful. |
| 303 Result    | Newly registered users will receieve an email that they must confirm (by clicking the link) to complete their registration and have access to their account. |
| 304           | Be able to edit my personal information e.g. address, email. | Manage my own personal information in case they change. |
| 304 Result    | This is all done in the My Profile section of their account. Users can also choose to save their current information at the checkout page if they wish |
| 305           | Easily sign in and sign out of my account. | Quickly access or leave my personal profile when using the website. |
| 305 Result    | This is done through the 'My Account' logo, then selecting 'Sign In'/'Sign Out'. They will be asked if they are sure they want to sign out before confirm it. Whenever a non-registered or even an user that's not currently signed in attempts to use or access an exclusive feature or part of the website (e.g reviews) they will be informed of this and asked to sign up or sign in. |
| 306           | Be able to recover my password in case I forget it. | Recover access to my account and all my personal information. |
| 306 Result    | . |

| 307           | Have access to my order history. | Can view all previous orders. |
| 307 Result    | . |

| 308           | Add product reviews. | Leave reviews on specific products. |
| 308 Result    | . |

| 309           | Edit product reviews. | Edit reviews on specific products. |
| 309 Result    | . |

| 310           | Delete product reviews. | Delete reviews on specific products. |
| 310 Result    | . |

| 311           | Add items to my wishlist. | Easily access a list of products I'm interested in viewing again and/or purchasing. |
| 311 Result    | . |

| 312           | Delete specific products from my wishlist. | Delete specific products that I no longer wish to have. |
| 312 Result    | . |

| 313           | Choose whether to save my delivery information. | For ease of future use and security reasons. |
| 313 Result    | Users can tick a box on the checkout form to save their personal info for the next time they visit. |



### As a Store Owner (including all prior stories)
| User Story ID | I want to: | So that I can: |
| ------------- | ----------| ------------- |
| 401           | Have more control and features than any other user. | Manage my store easily. |
| 401 Result    | . |

| 402           | Have access to an admin portal. | Access and manage all store tasks in greater depth. |
| 402 Result    | . |

| 403           | Be able to create other super user accounts. | Create super user accounts with advanced control. |
| 403 Result    | . |

| 404           | Be able to add a product to my store. | Add new product to my store. |
| 404 Result    | . |

| 405           | Be able to edit/update a specific product. | Change product prices, descriptions, images and other product criteria. |
| 405 Result    | . |

| 406           | Be able to delete a product from my store. | Remove items that are no longer for sale. |
| 406 Result    | . |

| 407           | Be able to add product categories (including basic Catgegory, Room and Specials.) | Add new categories to my store. |
| 407 Result    | . |

| 408           | Be able to edit/update product categories (including basic Catgegory, Room and Specials.) | Edit/Update any current store categories. |
| 408 Result    | . |

| 409           | Be able to delete product categories (including basic Catgegory, Room and Specials.) | Delete any current categories. |
| 409 Result    | . |

| 410           | Be able to add product reviews to any specific product. | Leave storeowner reviews on any specific products. |
| 410 Result    | . |

| 411           | Be able to edit/update all product reviews. | Edit/Update any user reviews on any specific products. |
| 411 Result    | . |

| 412           | Be able to delete any specific product reviews. | Delete any user reviews on specific products. |
| 412 Result    | . |

| 413           | Be able to add user wishlist. | Add new wishlists for any registered user. |
| 413 Result    | . |

| 414           | Be able to edit/update all user wishlsts. | Edit/Update any current user wishlist. |
| 414 Result    | . |

| 415           | Be able to delete user wishlists. | Delete any user wishlist from their profile. |
| 415 Result    | . |

| 416           | Be able to add user account and info. | Create and control user account and info on my website. |
| 416 Result    | . |

| 417           | Be able to edit/update all user account and info. | Edit/Update any current user account and 
info on my website. |
| 417 Result    | . |

| 418           | Be able to delete user accounts and info. | Delete any current user account and info from my website. |
| 418 Result    | . |

[Back to table of contents](#table-of-contents)

# Lighthouse

[Back to table of contents](#table-of-contents)

# Further Testing

[Back to table of contents](#table-of-contents)

# Bug Fixes

[Back to table of contents](#table-of-contents)

# Known Bugs

[Back to table of contents](#table-of-contents)

# Testing Credits
## Reading and Guidence
## Code

[Back to table of contents](#table-of-contents)