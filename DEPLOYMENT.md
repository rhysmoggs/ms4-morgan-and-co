<h1 align="center">Morgan & Co</h1>

The Full Deployment documentation, following on from the README [found here](README.md)

# Table of Contents
* [Deployment](#deployment)
* [ElephantSQL Setup](#elephantsql-setup)
* [Creating Heroku App](#creating-heroku-app)
* [Deploying to Heroku](#deploying-to-heroku)
* [AWS Setup](#aws-setup)
* [Deployed Site Webhook Setup](#deployed-site-webhook-setup)
* [Google and Django Email Setup](#google-and-django-email-setup)
* [Stripe Setup](#stripe-setup)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Making a Local Clone](#making-a-local-clone)

# Deployment

The following assumes that you have or are able to register to the services mentioned and used in developing and deploying the Morgan & Co website. The majority of these services are free to use, to register or have tiers avaiable.

During the development time it took to create this project, Heroku decided to end their free tier service for database and dynos, support and la la. link to news here.
Due to this, and with Code Institute's help, the change was dealt with by migrating the postgres database over to use elephantSQL instead of Heroku's postgres Add-On.
credit/link here.
Here's a list of all necessary services where account registation is required:
- Heroku
- ElephantSQL
- Stripe
- AWS
- Google



- The Code Institute's template was used for basic setup, found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- This was used to start a Gitpod workspace.
- Create "env.py" file.
- Create a ".gitignore" file if you choose not to use Code Institute's template. Add `env.py` and the soon to be generated `__pyache__/` to it. All hidden and sensitive files/folders to be added here.
- In "env.py", type following:
    ```
    import os

    os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY_HERE")
    os.environ.setdefault("STRIPE_PUBLIC_KEY", "YOUR_STRIPE_PUBLIC_KEY_HERE")
    os.environ.setdefault("STRIPE_SECRET_KEY", "YOUR_STRIPE_SECRET_KEY_HERE")
    os.environ.setdefault("STRIPE_WH_SECRET", "YOUR_STRIPE_WH_SECRET_HERE")
    os.environ.setdefault("DATABASE_URL", "YOUR_DATABASE_URL_HERE")
    ```

    The `SECRET_KEY` was created using a django secret key generator found [here](https://miniwebtool.com/django-secret-key-generator/).  

    The `"STRIPE_PUBLIC_KEY"`, `"STRIPE_SECRET_KEY"` and `"STRIPE_WH_SECRET"` are expalined in the Stripe Setup below.  

    `"YOUR_DATABASE_URL_HERE"` points to the ElephantSQL databse link to be created.  

[Back to table of contents](#table-of-contents)

## ElephantSQL Setup

- Create an account by selecting 'Create a managed database today' [link](https://www.elephantsql.com/) on their home page and choosing their free tier. Alternatively, sign in with your github account via the link.
- Click 'Create a New Instance'
- Name it - 'morgan-and-co' in this case.
- Choose the Tiny Turtle (Free) plan.
- Select your region and data center - 'EU-West-1 (Ireland)' in this case. If "Error: No cluster available in your-chosen-data-center yet" appears, choose another region.
- Click 'Review'
- Click 'Create Instance'
- Return to dashboard, click on the newly created database instance, morgan-and-co.
- Copy the postgres database URL found in the URL section.

[Back to table of contents](#table-of-contents)

## Creating Heroku App
Following is a way of creating a heroku app, and avoiding using their postgres Add-Ons.

- Log In to Heroku website.
- 'Create new app'.
- Choose closest region (Europe for this project).
- Name the app. Must be unique.
- Go to Settings tab
- In Config Vars, add DATABASE_URL and the ElephantSQL URL value previously copied from the newly created database instance copied from the website (usually begins with ```postgres://```)

- In Gitpod, install ```pip3 install dj_database_url``` and ```pip3 install psycopg2-binary```.
- Freeze requirements with ```pip3 freeze > requirements.txt```.

- In Gitpod, go to morgan_and_co > "settings.py", add ```import dj_database_url``` to the bottom of the list of imports, under ```import os``` then, comment out the 'DATABASES' section: 
```
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
```
and add:
```
DATABASES = {
    'default': dj_database_url.parse()
}
```
- Paste the database URL from ElephantSQL (previously copied and added to the Heroku Config Vars) so that it looks like:
```
DATABASES = {
    'default': dj_database_url.parse('your_elephantSQL_db_URL_here')
}
```
- Save, but don't commit as this is a temporary change.

- Due to this change, the ElephantSQL datatbase is now being targeted and thus migrations must be made.

- ```python3 manage.py showmigrations``` then ```python3 manage.py migrate```.

- Import all the product data. See [here](https://docs.djangoproject.com/en/4.1/ref/django-admin/#dumpdata) for guidence on dumpdata and [here](https://docs.djangoproject.com/en/4.1/ref/django-admin/#loaddata) for loaddata.

- In this case, due to the size of the current product range, all product data was added manually via the admin portal.

- Create a super user to log in with." ```python3 manage.py createsuperuser```. Enter details.

- Un-comment the 'DATABASES' section in morgan_and_co > "settings.py" that we commented out earlier. (make it active now) and delete:
```
DATABASES = {
    'default': dj_database_url.parse('your_elephantSQL_db_URL_here')
}
```
- This is to avoid adding it to version control. 

- git add, commit, git push.

[Back to table of contents](#table-of-contents)

## Deploying to Heroku

- In GitPod, morgan_and_co > "settings.py", update the 'DATABASES' section to be:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
- ```pip3 install gunicorn pip3 freeze > requirements.txt```

- Create a file named "Procfile" (outside of all the apps. so, create it where requirements.txt, gitignore etc are) and add this to it, making sure you use your gitpod repo name: ```web: gunicorn your_gipod_repo_name.wsgi:application``` (no empty space below) so: ```web: gunicorn morgan_and_co.wsgi:application``` (no empty space below).

- in CLI ```heroku login -i```, and log in with ```heroku info heroku config:set DISABLE_COLLECTSTATIC=1``` (if only one heroku app) OR ```heroku config:set DISABLE_COLLECTSTATIC=1 --app your-heroku-app-name-here``` (if more than one heroku app on website) e.g. ```heroku config:set DISABLE_COLLECTSTATIC=1 --app morgan-abd-co```, for this example.

- morgan_and_co > "settings.py", update ```ALLOWED_HOSTS = []``` to be  
```ALLOWED_HOSTS = ['your-heroku-app-name-here.herokuapp.com', 'localhost']```  
e.g. ```ALLOWED_HOSTS = ['morgan-and-co.herokuapp.com', 'localhost']``` for this example.

- ```ACCOUNT_EMAIL_VERIFICATION = 'none'``` (make sure- to change this back to ```ACCOUNT_EMAIL_VERIFICATION = 'mandatory'``` before production/launching website)

- git add, commit, push.

- Click 'Open App' in Heroku, and your project will be displayed here - no styling, but will add static files later.

- For automatic deployment: in Heroku > Deploy > Deployment Method, choose GitHub Connect to Github, search for your repository e.g. m4-morgan-and-co, then select it and click Connect. Enable Automatic Deploys.

- Google django secret key generator website, generate one then copy it. Go to Heroku website > Settings > Reveal Config Vars, add a new one: "SECRET_KEY": "paste-your-django-secret-key-here".

- morgan_and_co > "settings.py", change the SECRET_KEY = 'your-previous-secret-key' to be: ```SECRET_KEY = os.environ.get('SECRET_KEY', '')``` and change ```DEBUG = True``` to be ```DEBUG = 'DEVELOPMENT' in os.environ```.

- git add, commit, git push.

[Back to table of contents](#table-of-contents)

## AWS Setup

Used to store the static files and images.

- Register for a free account [here](https://aws.amazon.com/). If you alread have one, ignore the Regisration steps.

- Click 'Create an AWS account' button.

- Click 'Create a new AWS account' on the next page and enter an email in the 'Root user email address' and an username for 'AWS account name'.

- Click 'Verify email address' and verify your email and continue, enter and confirm password.

- Choose 'Personal', then enter your details.

- Enter your Billing information. You may need to approve this payment. Confirm your identity.

- Select your support plan - choose free for this project.

- Go to AWS Management Console, and sign in.

- Go to 'Services' and either use the search bar or find 'S3' in the list of all services.

- Select 'Buckets' in the left-hand side menu (it may be hidden, so reveal it with the button on left) Click 'Create Bucket' and name it whatever you wish, although it's good practice to name it the same as your heroku app name. Select the Region closest to you, if it doesn't automatically do so.

- Follow [this](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf) guide for an updated process. Essentially, check 'ACLs enabled' and 'Bucket owner preferred'.

- Uncheck 'Block all public access', Tick the box with the warning "I acknowledge that the current settings might result in this bucket and the objects within becoming public."

- 'Create Bucket'.

- Select the newly created bucket from the list. 'Properties' tab > scroll to bottom to find 'Static website hosting' and click 'Edit' then 'Enable' it. Make sure 'Host a static website' is active, then in 'Index document' type "index.html" and in 'Error document - optional' type "error.html". Click 'Save changes'.

- 'Permissions' tab > scroll down to 'Cross-origin resource sharing (CORS)' and click 'Edit', paste the following into the empty space:
```
[
  {
    "AllowedHeaders": [
      "Authorization"
    ],
    "AllowedMethods": [
      "GET"
    ],
    "AllowedOrigins": [
      "*"
    ],
    "ExposeHeaders": []
  }
]
```

- Click 'Save changes' Next, find the 'Bucket policy' section within the 'Permissions' tab, click 'Edit' Click 'Policy generator' Step 1: Select Policy Type = 'S3 Bucket Policy', from the dropdown, select this. Effect = Allow Principal = * Actions = GetObject ARN = copy abnd paste it from the previous page in the 'Edit Bucket Policy' page, under 'Bucket ARN' Click 'Add Statement' then 'Generate Policy'. Copy the Policy (the code text), paste it into the Bucket Policy Editor on the previous page. Then add `/*` to the end of the 'Rescource' key (basically, the end of your app name add '/*') Click 'Save changes'.

- 'Permissions' tab > scroll down to 'Access control list (ACL)' and click 'Edit' make sure 'Everyone (public access)' > 'Objects' > 'List' box is ticked and tick the warning box "I understand the effects of these changes on my objects and buckets." Click 'Save changes'

- Go back to 'Services' on top left, search or find 'IAM' Select 'User groups' on left-hand-side menu > 'Create group' and name the group, in this case "manage-morgan-and-co" then 'Create group' Select 'Policies' on the left-hand-side menu then 'Create policy' and then 'JSON' tab then 'Import managed policy' and in the search input type 's3' and choose 'AmazonS3FullAccess' Click 'Import'

- In a sperate tab, open the S3 again, go to your Bucket > Permissions > Bucket Policy > Edit and copy the Bucket ARN.

- Back to the IAM tab, instead of `"*"` in the "Resources" JSON code, paste the Bucket ARN inside a list so that "Resource" now looks like:
```
"Resource": [
    "your-Bucket-ARN-here",
    "your-Bucket-ARN-here/*"
]
```
(above, one item is the bucket itelf, and the `/*` is for all files and folders in the bucket)

- Click 'Next:tags' then 'Next:review' Review policy > Name = whatever you wish, in this case "morgan-and-co-policy" Description = "Access to S3 bucket for Morgan and Co static files" 'Create policy'.

- On left-hand-side menu, click 'User Groups', select your group > Permissions > Add Permissions dropdown towards the right and select 'Attach Policies' Search for the policiy we just created, tick the box to select it, then 'Add permissions'

- Left-hand-side menu select 'Users' > Add Users > name it "morgan-and-co-staticfiles-user" and tick "Access key - Programmatic access" box. Click 'Next: Persmissions' > tick box for our group in the list then 'Next:tags' > 'Next:review' > 'Create user' > 'Download .csv' (very important to do so, as you can't download it again). Close.

- Back in gitpod CLI `pip3 install boto3` `pip3 install django-storages` `pip3 freeze > requirements.txt`.

- "morgan_and_co" folder in gitpod > "settings.py", add `'storages'`, to our 'INSTALLED_APPS', under the 'other' section also, a space under MEDIA URL section add this new section:
```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'morgan-and-co'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
(use your bucket name and your region name accordingly)
```

- in Heroku, go to your Config Vars, and add these variables - the values can be found in the csv document downloaded from AWS earlier: 
```
AWS_ACCESS_KEY_ID = (input value from csv download)
AWS_SECRET_ACCESS_KEY = (input value from csv download)
USE_AWS = True
```

- Also, remove DISABLE_COLLECTSTATIC variable.

- In gitpod, morgan_and_co > settings.py add the following to the bottom, under USE_AWS:

```AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'```

- Create a file named 'custom_storages' in the root (same place as README, Procfile, requirements.txt etc) and add the following to it:

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- morgan_and_co > settings.py, update the if statement so it finally looks like (use your bucket name and your region name accordingly):

```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'morgan-and-co'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
- git add, commit and push.

- It should build in Heroku and copy the static files. open app in Heroku. Also, check the s3 bucket in AWS. It should contain the static files and folders.

MEDIA FILES

in morgan_and_co > settings.py, add the following on top of ```# Bucket Config``` witin the ```if 'USE_AWS' in os.environ: ```statement:
```
# Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```
- add, commit, push.

- In AWS > s3, choose your bucket, then click 'Create folder' button. Name it "media".
Inside the newly formed "media" folder, click 'Upload' button then click "Add files" button.
Choose all of your product images (you can download from your repo or from source).
Under the 'Permissions' section, tick the "Grant public-read access" option and "I understand..."
for the warning.

- Click 'Upload' button.

- Next, confirm the superuser email address on the deployed website's database. In Heroku, 'Open App' and go to /admin in the url.
if "CSRF verification failed. Request aborted." error appears, close/refresh and open app again.
Under Accounts, click Email Addresses, and select your email
-if you dont see your email in the list, log in on website and then go back to admin. in gitpod > 
morgan_and_co > settings.py, make sure `ACCOUNT_EMAIL_VERIFICATION = 'mandatory'` instead of `'none'`
(you'll need to add commit and push after the settings.py change)

- Next, go to Stripe website > Developers > API keys.
- Copy the Publishable Key token.
- Go to your Heroku Config Vars and add STRIPE_PUBLIC_KEY and the copied token.
- Then, repeat the same process but for copying the Secret key token and create the STRIPE_SECRET_KEY variable in Heroku.

[Back to table of contents](#table-of-contents)

## Deployed Site Webhook Setup
- Create a new webhook endpoint for the deployed website.

- Stripe website > Developers > Webhooks > Add Endpoint button.

- Add the url for our Heroku app (followed by /checkout/wh/ - just like before) so it follows this pattern: https://your-app-name-here.herokuapp.com/checkout/wh/

- Click Select Events > tick Select All Events > click Add Events button.

- Reveal the Signing secret key, copy it, and add it to the Heroku Config Vars as 'STRIPE_WH_SECRET' and paste the Signing secret key.

- Test by purchasing a product through the Heroku app.

[Back to table of contents](#table-of-contents)

## Google and Django Email Setup

- Create a [Gmail](https://www.google.com/intl/en-GB/gmail/about/) account.
- Go to Settings > See all Settings > Accounts and Imports > Other Google Account settings.
- on the left, Security > Signing in to Google > 2-Step Verification > Get Started.
- Enter password > Next > Choose how to verify (text chosen) > Enter code > Turn On.
- Press the back arrow (on google, next to 2-Step Verification) to go back to the 'Security' page.
- Under 'Signing in to Google' again, click 'App passwords' > Enter password.
- 'Select app' = Mail. 'Select device' = Other (Custom name), and name it: Django > Generate button.
- Copy the app password > Done.
- Heroku > Config Vars > add "EMAIL_HOST_PASS" with the copied app password.
- add another variable named "EMAIL_HOST_USER" and your email as the value.

- In gitpod, go to boutique-ado > "settings.py", delete `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
- Scroll down to the ```#Stripe section```, and update it to be:
```
# Stripe
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
STRIPE_CURRENCY = 'usd'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'boutiqueado@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```
and make sure `ACCOUNT_EMAIL_VERIFICATION = 'mandatory'` instead of `'none'`

- git add, commit, push

"To test it out let's head to our Heroku app. And try to register for an account.
I'll use a temporary email from tempmail.org. I've got the confirmation email which means email 
is being sent properly. And now I can verify my account. And I'm able to login."

[Back to table of contents](#table-of-contents)

## Stripe Setup

1. Register for an account [here]()

[Back to table of contents](#table-of-contents)

## Forking the GitHub Repository

The following instructions are taken from Code Institutes [README.md template](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md)

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

[Back to table of contents](#table-of-contents)

## Making a Local Clone

- Log in to GitHub and locate the [GitHub Repository](https://github.com/rhysmoggs/ms4-morgan-and-co)
- Under the repository name, click the "code" dropdown menu.
- To clone the repository using HTTPS, under "HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory to be made.
- Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/rhysmoggs/ms4-morgan-and-co
```

- Press Enter. Your local clone will be created.
- Create "env.py" file.
- Add `env.py` and the soon to be generated `__pyache__/` to it. All hidden and sensitive files/folders to be added here.
- In "env.py", add the following:
    ```
    import os

    os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY_HERE")
    os.environ.setdefault("STRIPE_PUBLIC_KEY", "YOUR_STRIPE_PUBLIC_KEY_HERE")
    os.environ.setdefault("STRIPE_SECRET_KEY", "YOUR_STRIPE_SECRET_KEY_HERE")
    os.environ.setdefault("STRIPE_WH_SECRET", "YOUR_STRIPE_WH_SECRET_HERE")
    os.environ.setdefault("DATABASE_URL", "YOUR_DATABASE_URL_HERE")
    ```

    The `SECRET_KEY` was created using a django secret key generator found [here](https://miniwebtool.com/django-secret-key-generator/).  

    The `"STRIPE_PUBLIC_KEY"`, `"STRIPE_SECRET_KEY"` and `"STRIPE_WH_SECRET"` are expalined in the Stripe Setup below.  

    `"YOUR_DATABASE_URL_HERE"` points to the ElephantSQL databse URL address (explained [here](#elephantsql-setup)).  

- In the CLI, type ```pip3 install -r requirements.txt``` to install the redquired dependencies.


Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

[Back to table of contents](#table-of-contents)