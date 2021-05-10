# Shopify Image Repository Fall 2021 Intern Challenge
### Made by Tristan Martinuson

## Description
This image repository uses Flask/SQLAlchemy/HTML for the stack.



## Running
To run this application, open the repo fold in your IDE of choice (I used PyCharm and Visual Studio Code) and run 'app.py', you may need to pip install any missing dependencies
or you can cd to the download folder and type 'python3 app.py' from the command line.

Flask will respond in cmd with a development server link which should be 'http://127.0.0.1:5000'. Click that link or type it in your web browser and you should be welcomed by the web app!


## Features
From the main page you are greeted by a couple of options and a nice gallery of the images already pre-loaded for you in the database!
### Uploading/Adding Images
To upload your own images to the image repository, first click the 'Choose File' button within the 'Upload here:' section. You are then able to choose
a photo from your desktop that you wish to upload to the repository. Once chosen, click the 'Upload a picture' button right beside the latter button to upload your 
image to the repository. You will be brought to a page confirming successful uploading and the option to return to the main page. Once you return you will notice your newly
minted image uploaded within the gallery on the main page!
### Deleting Images
To delete a image, follow the 'Go to delete page' button under the 'Delete here:' heading. You will be greeted with a list of the same pictures from the main page with associated values
that you will use to delete an image from the repository. Choose one of the image's number that you would like to delete and type it within the text box at the top of the page.
Once typed, click Delete and the image will be successfully deleted from the repository! You will then be brought to a page confirming successful deletion and the option to return
to the main page. Once you return to the main page you will notice the image is no longer showing with the rest of the gallery.

## Testing
This application has been tested manually for extreme values in cases of deletion where the backend handles exception handling for non existent image entries.
The text box for the deletion page uses numerical entries only which prevents users from breaking the application with SQL Injection.
The images are stored on a local database created on application run (or as there is already a given db with images stored) and therefore are only as secure as the user's computer
running the application.

## Implementations for the future
First of all, I would like to include a feature where the user can search for their images within the repository. I also
would like to include an ecommerce aspect of being able to purchase photos from a 'fake' bank account where you gain ownership of that photo and the image is then deleted from the
repository (or by the stock of the image thats left). Finally I think I would want to clean up the UI so it looks nicer! 

## Final notes
I hope you enjoyed my application Shopify and I'm really glad to do this mini-project. I learned a lot by doing it and its really helped me gain more confidence as a programmer with my projects :) Thank you Shopify!
