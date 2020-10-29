# Django Starter Application

## Pages app

- The 'Pages' app allows a user to create model-based pages from the admin.
- The 'Status' of a page by default is set to 'Draft' making it unavailable to visitors. In order for visitors to view a page, the 'Status' must be set to 'Published'.
- A page's 'Slug' is used as it's url path.
- Pages can be added to the website's main menu by selecting the option in the page form. The order of the menu items is filtered by the pages' primary keys. So menu items will be populated in the order the pages are created.
