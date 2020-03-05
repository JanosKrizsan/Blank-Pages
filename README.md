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
  
Articles:<br>
  Articles, all of them.
  
Search:<br>
  A page for sorting and searching articles based on pre-determined categories.

Library:<br>
  Contains references and source materials with additional links for download if available.
  
## Code Example

Entry updater, it compares values and different ones are overwritten in the database on the tracked (State Modified) item.
```
        private void EntryUpdater(EntityEntry entry, object updatedEntry)
        {
            dynamic update;

            switch (updatedEntry.GetType().Name)
            {
                case nameof(Article):
                    update = (Article)updatedEntry;
                    break;
                case nameof(Author):
                    update = (Author)updatedEntry;
                    break;
                case nameof(Source):
                    update = (Source)updatedEntry;
                    break;
                default:
                    update = string.Empty;
                    break;
            }

            if (update is string)
            {
                return;
            }

            foreach (var prop in entry.Properties)
            {
                var newVal = update.GetType().GetProperty(prop.Metadata.Name).GetValue(update, null);
                var currentType = newVal.GetType();

                if (!Convert.ChangeType(prop.CurrentValue, currentType).Equals(newVal))
                {
                    prop.CurrentValue = (object)newVal;
                }
            }

            _context.SaveChanges();
        }
```

## Installation

To install the Python-Flask database backend, you will need to download the following:<br>

```
Python
Pip
PostgreSQL
```
Follow these steps for an better experience, do not forget to use an elevated command prompt.

- Download the Python version desired:<br>
(Python)[https://www.python.org/downloads/]

- After you installed Python, open cmd (Search > "cmd" > Run as Administrator)
- Copy-paste the following, and run:
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
- Then run:
`python get-pip.py`

To see which packages you have, you can use `pip list`. In order to download the packages needed, you can use
`pip install <name of package>`

There is a useful tool called "pipupgrade" which you can install via the above command. You can use it to view and update your
packages up to the latest version, calling `pipupgrade --latest`.<br>
To check outdated packages, use `pip list --outdated`.

- Now, we need PostgreSQL, which you can get and install from here:<br>
[PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

- Download and install the version you need, then after that's done, head to:<br>
  You can either open this window via (Search > Env > "Edit the system env variables" > Environment Variables)<br>
  Or (This Pc > Properties > Advanced Settings > Advanced >Environment Variables)
  
  Herein you must open the PATH variable, click on "New" which will start a new line. Copy-paste the past of your PostgreSQL
  installation's bin folder, which should look something like this: `C:\Program Files\PostgreSQL\12\bin`
  
  Now you can use commands such as `psq` from your command prompt.
  
One side-note, as PSQL has a service, we can switch that to Manual and stop it from executing each time we start Windows. To do that,
we need to to the following:<br>
- Go to (Run > services.msc), this will open the Services manager
- Find the service with the name "postgresql-x64-12" (this could change depending on your version)
- Double click on it, change "Startup type" to Manual
- If you want some convenience, copy the service's name

You could do this always, manually starting it from this window, then stopping it, but it would be a hassle.

So you could add this code to a newly created .txt file. Do not forget to change the `[SERVICE NAME]` part to the name of your
Postgres service name. After you added it, simply save, then rename the extension to .bat.

If you want to be a really awesome guy/gal, then you can also place this .bat file (let's say "togglepostgres.bat") into your already
added `C:\Program Files\PostgreSQL\12\bin` folder. Now if you just type in the name `togglepostgres.bat` to your command prompt, the service will toggle on-off every time. Remember, you need administrator privileges to do so!

```
@ECHO OFF
SET SvcName=[SERVICE NAME]

SC QUERYEX "%SvcName%" | FIND "STATE" | FIND /v "RUNNING" > NUL && (
    ECHO %SvcName% is currently not running 
    ECHO START %SvcName%

    NET START "%SvcName%" > NUL || (
        ECHO "%SvcName%" cannot be started 
        EXIT /B 1
    )
    ECHO "%SvcName%" has been started
    EXIT /B 0
) || (
    ECHO "%SvcName%" is running
    NET STOP "%SvcName%"
    ECHO "%SvcName%" has been stopped
    EXIT /B 0
)
```


## Miscellaneous

[Shell Script Source](https://www.brankovucinec.com/check-if-service-is-running-and-start-it-when-it-is-not-running/)
[Img Source](https://wallhaven.cc/w/ne533o)
