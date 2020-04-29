# Tabula Rasa

![Paper Plane Image](https://i.imgur.com/ykieeb4.png)

## What is this thing?

This is a blog-template which uses an EF Core database for persistence of Articles, Authors and their relevant Sources data. It furthermore saves Articles serialized as XML, mainly for content-related and safety purposes. This application is still in development.

## Tech Used

- C#
- Entity Framework
- JavaScript
- React.js
- Python

## Planned Features

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

A similar thing in python, the instantiated item's values are set.
```
def set_attributes(obj, data):
	for k, v in data.items():
		setattr(obj, k, v)
	return obj
```
## Python Data Handler

Imported:<br>
- Flask for request/response handling
- PSQL for database access and edition
- Flask_jwt for authentication via JWT
- Bcrypt used for password hashing
- Stdiomask for simple PSQL-password hiding

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

Alternatively, you can change it to Manual using Powershell:<br>
- Run PS as admin
- Write the following: `Get-Servie | where Name -Ilike "*postgresql*" | Set-Service -StartupType Manual`
- Hit enter to run, this will change the startup type of said service to manual

Now you can add the script below to a .txt file and save it with a .ps1 extension. Just start up PS and run the script with the path itself.

You might need to change the execution-policy, for which you can use `Set-ExecutionPolicy RemoteSigned` which will enable the running of scripts.
Powershell script to toggle the service:
```
$psql = Get-Service | where Name -ILike "*postgresql*"
$psqlService = $psql.Status
Write-Output "PSQL service is currently $psqlService"

$toggleType = $psqlService -eq "Stopped"
$runToggle = if ($toggleType) {$psql | Start-Service} else {$psql | Stop-Service}
$writeOut = if ($toggleType) {'PSQL service started'} else {'PSQL service stopped.'}

$runToggle
$writeOut
```

## Miscellaneous

[Img Source](https://wallhaven.cc/w/ne533o)

## Disclaimer

### This project is purely for practice and educational purposes.
