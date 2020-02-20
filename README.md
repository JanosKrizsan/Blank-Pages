# Tabula Rasa

![Paper Plane Image](https://i.imgur.com/ykieeb4.png)

## What is this thing?

This is a blog-template which uses an EF Core database for persistence of Articles, Authors and their relevant Sources data. It furthermore saves Articles serialized as XML, mainly for content-related and safety purposes. This application is still in development.

## Tech Used

- C#
- Entity Framework
- JavaScript
- React.js

## Features

- Is a single-page web application
- Hidden login, authentication, JWT token
- Author(s) are able to create, edit, post new articles
- Saves information of an article into the database
- Articles are stored in an XML serialized format, which is deserialized for publication
- Retrieves articles from related, database-saved file-names from the local host
- Lazy loading of article data, upon viewing them

### Further Planned Features

- Anonymous commenting on articles
- Human authentication to filter out bots for commenting
- Certain words, and links are censured or changed to other words in comments

## Site Structure

Main Page:<br>
  Includes the list of newest articles posted, in descending order.
  
Search:<br>
  A page for sorting and searching articles based on pre-determined categories.

Library:<br>
  Contains references and source materials with additional links for download if available.
  
## Code Example

None yet.

## Miscellaneous

[Img Source](https://wallhaven.cc/w/ne533o)
